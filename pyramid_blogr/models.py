# standard library
import datetime

# SQLAlchemy
from sqlalchemy import (
    Text,
    Index,
    Column,
    Integer,
    Unicode,
    DateTime,
    ForeignKey,
    UnicodeText
)
from sqlalchemy.orm import sessionmaker, scoped_session
from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.ext.declarative import declarative_base

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


#пользователи
class User(Base):
    __tablename__ = 'users'
    id_U = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)

#статусы
class Status(Base):
    __tablename__ = 'status'
    id_S = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False, unique=True)

#соединим Пользоваталей и Статусы
class UserStatus(Base):
    __tablename__ = 'user_status'
    user_id = Column(Integer, ForeignKey('users.id_U'), primary_key=True)
    status_id=Column(Integer, ForeignKey('status.id_S'), primary_key=True)

#статьи
class Article(Base):
    __tablename__ = 'articles'
    id_A = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    content = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

#соединим Статьи и их авторов:
class UserArticle(Base):
    __tablename__ = 'art_user'
    id = Column(Integer, ForeignKey('articles.id_A'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id_U'), primary_key=True)
