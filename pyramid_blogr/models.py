import datetime
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
from sqlalchemy.orm import relationship, backref

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()



class User(Base):
    __tablename__ = 'users'
    id_U= Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True, nullable=False)
    password = Column(Unicode(255), nullable=False)
    aboutme = Column(UnicodeText, default='')


    def _repr_(self):
        return self.name+" "+self.password+" "+str(self.access)
    

class Article(Base):
    __tablename__ = 'articles'
    id_A = Column(Integer, primary_key=True)
    title = Column(UnicodeText, nullable=False)
    content = Column(UnicodeText, default=u'')
    u_id = Column(Integer, ForeignKey('users.id_U'), primary_key=True)
    Cdate = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, title, content, u_id, Cdate):
        self.title=title
        self.content=content
        self.u_id=u_id
        self.Cdate=Cdate
    def _repr_(self):
        return self.title+" "+self.content+" "+self.u_id+ " "+self.Cdate

class UserArticle(Base):
    __tablename__ = 'art_user'
    id = Column(Integer, ForeignKey('articles.id_A'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id_U'), primary_key=True)
