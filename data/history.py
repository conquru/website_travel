import sqlalchemy
from data import db_session
from sqlalchemy import orm


class History(db_session.SqlAlchemyBase):
    __tablename__ = 'history'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    tickets = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    enter = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hotel = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    city_start = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    city_end = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relationship('User')
