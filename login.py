from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import Flask, redirect, render_template, abort, request
from data import db_session
from data.users import User
from data.history import History
from forms.loginform import LoginForm
from forms.job import JobsForm
from forms.registerform import RegisterForm
from forms.searchform import SearchForm
from functions.entertainments import GetEntertainments
from functions.plane import GetTickets
from functions.hotel import GetHotel

app = Flask(__name__)
app.config['SECRET_KEY'] = '9vTgySlnihdzBGrf'

login_manager = LoginManager()
login_manager.init_app(app)
name = ''

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    global name
    if current_user.is_authenticated:
        return redirect('/result')
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            name = User.email
            return redirect("/result")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/result', methods=['GET', 'POST'])
def search():
    global name
    form = SearchForm()
    if form.validate_on_submit():
        list_tickets = ' '.join(GetTickets(form.city_start.data, form.city_end.data, form.time.data))
        list_entrers = ' '.join(GetEntertainments(form.city_end.data))
        list_hotel = ' '.join(GetHotel(form.city_end.data))
        db_sess = db_session.create_session()
        history = History(
            tickets=list_tickets,
            enter=list_entrers,
            hotel=list_hotel,
            city_start=form.city_start.data,
            city_end=form.city_end.data,
            date=form.time.data
        ) 
        db_sess.add(history)
        db_sess.commit()
        return render_template('search.html', flag=0, tickets=list_tickets, hotel=list_hotel, enter=list_entrers, form=form)
    return render_template('search.html', flag=0, tickets='', hotel='', enter='', form=form)

@app.route('/history', methods=['GET', 'POST'])
def result():
    db_sess = db_session.create_session()
    query_history = db_sess.query(History)
    query = db_sess.query(User)
    for user in db_sess.query(User).all():
        if user.email == current_user.name.data:
            user_id = user.id
    history = db_sess.query_history(History).filter(History.name == user_id)

    return render_template('jobs.html', history=history)


@app.route('/authorized', methods=['GET', 'POST'])
def main():
    db_sess = db_session.create_session()
    query_history = db_sess.query(History)
    query = db_sess.query(User)
    for user in db_sess.query(User).all():
        if user.email == current_user.name.data:
            user_id = user.id
    history = db_sess.query_history(History).filter(History.name == user_id)

    return render_template('jobs.html', history=history)


@app.route('/add_jobs', methods=['GET', 'POST'])
@login_required
def add_jobs():
    form = JobsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        jobs = Jobs()
        jobs.job = form.job.data
        jobs.team_leader = form.team_leader.data
        jobs.work_size = form.work_size.data
        jobs.collaborators = form.collaborators.data
        jobs.is_finished = form.is_finished.data
        current_user.jobs.append(jobs)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/authorized')
    return render_template('add_jobs.html', title='Постановка задачи',
                           form=form)


# @app.route('/add_jobs/<int:id>', methods=['GET', 'POST'])
# @login_required
# def edit_news(id):
#     form = JobsForm()
#     if request.method == "GET":
#         db_sess = db_session.create_session()
#         jobs = db_sess.query(Jobs).filter(Jobs.id == id,
#                                           ).first()
#         if jobs:
#             form.job.data = jobs.job
#             form.team_leader.data = jobs.team_leader
#             form.work_size.data = jobs.work_size
#             form.collaborators.data = jobs.collaborators
#             form.is_finished.data = jobs.is_finished
#         else:
#             abort(404)
#     if form.validate_on_submit():
#         db_sess = db_session.create_session()
#         jobs = db_sess.query(Jobs).filter(Jobs.id == id,
#                                           ).first()
#         if jobs:
#             jobs.job = form.job.data
#             jobs.team_leader = form.team_leader.data
#             jobs.work_size = form.work_size.data
#             jobs.collaborators = form.collaborators.data
#             jobs.is_finished = form.is_finished.data
#             db_sess.commit()
#             return redirect('/authorized')
#         else:
#             abort(404)
#     return render_template('add_jobs.html',
#                            title='Редактирование задания',
#                            form=form
#                            )


@app.route('/', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.hashed_password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            email=form.email.data,
        )
        user.set_password(form.hashed_password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


# @app.route('/jobs_delete/<int:id>', methods=['GET', 'POST'])
# @login_required
# def news_delete(id):
#     db_sess = db_session.create_session()
#     jobs = db_sess.query(Jobs).filter(Jobs.id == id,
#                                       ).first()
#     if jobs:
#         db_sess.delete(jobs)
#         db_sess.commit()
#     else:
#         abort(404)
#     return redirect('/authorized')


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
