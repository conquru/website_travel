from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

@app.route('/login', methods=['GET', 'POST'])
def login():
    
# def main():
#     # app.run()
#     db_session.global_init("db/user.db")
#     db_sess = db_session.create_session()
#     user = db_sess.query(User).filter(User.id == 1).first()
#     db_sess.add(job)
#     db_sess.commit()


# if __name__ == '__main__':
#     main()