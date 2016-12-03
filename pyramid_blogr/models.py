from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


import datetime

from pyramid_sqlalchemy import BaseObject
from sqlalchemy import Column, ForeignKey, DateTime, Integer, Unicode, UnicodeText

#пользователи
class User(BaseObject):
    __tablename__ = 'users'
    id_U = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    last_logged = Column(DateTime, default=datetime.datetime.utcnow)
    child = relationship("user_status", uselist=False, back_populates="parent")
    child = relationship("art_user", uselist=False, back_populates="parent")

#статусы
class Status(Base):
    __tablename__ = 'status'
    id_S = Column(Integer, primary_key=True)
    name = Column(Unicode(255), nullable=False, unique=True)
    child = relationship("user_status", uselist=False, back_populates="parent")

#соединим Пользоваталей и Статусы
class UserStatus(Base):
    __tablename__ = 'user_status'
    sv_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey=('parent1.id_U'))
    parent1 = relationship("users", back_populates="child")
    status_id=Column(Integer, ForeignKey=('parent2.id_S'))
    parent2 = relationship("status", back_populates="child")

#статьи
class Article(BaseObject):
    __tablename__ = 'articles'
    id_A = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique=True, nullable=False)
    content = Column(UnicodeText, default=u'')
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)
    child = relationship("art_user", uselist=False, back_populates="parent")

    #соединим Статьи и их авторов:
class UserArticle(BaseObject):
    __tablename__ = 'art_user'
    id = Column(Integer, ForeignKey=('parent3.id_A'))
    parent3 = relationship("articles", back_populates="child")
    user_id = Column(Integer, ForeignKey=('parent4.id_U'))
    parent4 = relationship("users", back_populates="child")
