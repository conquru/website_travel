from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask import Flask, redirect, render_template, abort, request
from data import db_session
from data.users import User
from data.history import History
from forms.loginform import LoginForm
from forms.history import JobsForm
from forms.registerform import RegisterForm
from forms.searchform import SearchForm
from functions.entertainments import GetEntertainments
from functions.plane import GetTickets
from functions.hotel import GetHotel
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = '9vTgySlnihdzBGrf'

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/result')
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/result")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/result', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    
    if form.validate_on_submit():
        tickets = []
        result = GetTickets(form.city_start.data, form.city_end.data, form.time.data)
        for i in result:
            tickets.append(' '.join(i))
        print(tickets)
        if tickets == []:
            time.sleep(10)
            tickets = []
            result = GetTickets(form.city_start.data, form.city_end.data, form.time.data)
            for i in result:
                tickets.append(' '.join(i))
            if tickets == []:
                list_tickets = 'Мы не смогли найти нужные билеты, можете обратится в службу поддержкии(которой нет)'
            else:
                list_tickets = ' '.join(tickets)
        else:
            list_tickets = ' '.join(tickets)
        
        entrers = []
        result = GetEntertainments(form.city_end.data)
        for i in result:
            entrers.append(' '.join(i))
        print(entrers)
        if entrers == []:
            time.sleep(10)
            entrers = []
            result = GetEntertainments(form.city_end.data)
            for i in result:
                entrers.append(' '.join(i))
            if entrers == []:
                list_entrers = 'Мы не смогли найти нужную информацию, можете обратится в службу поддержкии(которой нет)'
            else:
                list_entrers = ' '.join(entrers)
        else:
            list_entrers = ' '.join(entrers)

        hotel = []
        result = GetHotel(form.city_end.data)
        for i in result:
            hotel.append(' '.join(i))
        print(hotel)
        if hotel == []:
            time.sleep(10)
            hotel = []
            result = GetHotel(form.city_end.data)
            for i in result:
                hotel.append(' '.join(i))
                hotel = GetHotel(form.city_end.data)
            if hotel == []:
                list_hotel = 'Мы не смогли найти нужную информацию, можете обратится в службу поддержкии(которой нет)'
            else:
                list_hotel = ' '.join(hotel)
        else:
            list_hotel = ' '.join(hotel)
        # tickets = ['test', 'test', 'test']
        # list_tickets = ' '.join(tickets)
        # hotel = ['test', 'test', 'test']
        # list_hotel = ' '.join(hotel)
        # entrers = ['test', 'test', 'test']
        # list_entrers = ' '.join(entrers)
        db_sess = db_session.create_session()
        user = User()
        now_user = db_sess.query(User).filter(User.name == current_user.name).first()
        history = History()
        history.name = now_user.id
        history.tickets = list_tickets
        history.enter = list_entrers
        history.hotel = list_hotel
        history.city_start = form.city_start.data
        history.city_end = form.city_end.data
        history.date = form.time.data
        # current_user.history.append(history)
        db_sess.add(history)
        db_sess.commit()
        return render_template('search.html', tickets=tickets, hotel=hotel, enter=entrers, form=form)
    return render_template('search.html', form=form)

@app.route('/history', methods=['GET', 'POST'])
def history():
    db_sess = db_session.create_session()
    user = User()
    history = History()
    query = db_sess.query(User)
    list_history = []
    for user in db_sess.query(User).all():
        if user.name == current_user.name:
            user_id = user.id
            print(user_id)
    query = db_sess.query(History)
    for i in db_sess.query(History).filter(History.name == user_id):
        list_history.append(i)
    return render_template('history.html', history=list_history)


@app.route('/registr', methods=['GET', 'POST'])
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
            name=form.name.data,
            email=form.email.data
        )
        user.set_password(form.hashed_password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', title='Регистрация', form=form)


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8080, host='127.0.0.1')
