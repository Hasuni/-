from pyramid.response import Response
from pyramid.renderers import render
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from sqlalchemy.exc import DBAPIError
from sqlalchemy import desc
from models import DBSession, User, Article, Base
from datetime import *

def get_user(user_name):
    if user_name!=None:
        return DBSession.query(User).filter(User.name==user_name).first()
    else:return None

@view_config(route_name='home', renderer='/')
def home(request):
    return HTTPFound(location='/login')

@view_config(route_name='about',renderer='templates/contact.jinja2')
def about(request):
    return {}
    
@view_config(route_name='view_blog',renderer='templates/index.jinja2')
def view_blog(request):
    posts=DBSession.query(Article).order_by(desc(Article.id_A))    
    return {'posts':posts}

@view_config(route_name='view_my',renderer='templates/my.jinja2')
def view_my(request):
    thisU_id=request.matchdict['id_U']
    posts=DBSession.query(Article).filter(u_id=thisU_id).order_by(desc(Article.id_A))    
    return {'posts':posts}


@view_config(route_name='blog_article', renderer='templates/post.jinja2')
def blog_article(request):
    DBSession=Session(bind=engine)
    id = request.matchdict['postid']
    post=DBSession.query(Article).filter(id_A==postid).first()
    title= post.title
    content= post.content   
    if (post is None):
        return HTTPNotFound('No such page')
    else:
        return {'post':post,
                'ouser': get_user(request.authenticated_userid)}


@view_config(route_name='blog_create', renderer='templates/newPost.jinja2')
def blog_create(request):
        if 'form.submitted' in request.params:
            Ptitle = request.params['title']
            Pcontent = request.params['content']
            article= Article(title=Ptitle, content=Pcontent, u_id=get_user(request.authenticated_userid).id, Cdate=datetime.now())
            DBSession.add(article)
            DBSession.commit
            return HTTPFound(location = '/post/'+str(article.id))
        else: return{}

@view_config(route_name='login', renderer='templates/autorisation.jinja2')
def login(request):
    header_s=forget(request)
    HTTPFound(location='/login')
    if 'POST'==request.method:
        login = request.params['login']
        password_ = request.params['password']
        user = DBSession.query(User).filter(User.name==login).first()
        if user!=None and user.password == password_:
            header_s = remember(request, login)
            return HTTPFound(location='/index', headers=header_s)
        else:
            return {'message':"Incorrect"}
    return{}

@view_config(route_name='logout')
def logout(request):
    header_s=forget(request)
    return HTTPFound(location = '/', headers=header_s)
        
@view_config(route_name='register', renderer='templates/registration.jinja2')
def register(request):
    if (get_user(request.authenticated_userid)!=None):
        headers=forget(request)
    if request.method =='POST':
        Uname = request.params['username']
        Upassword = request.params['password']
        Uabout = request.params['aboutme']
        user = DBSession.query(User).filter(User.name==Uname).first()
        if user==None:
            if Uname!=None and Uname!="" and Upassword!=None and Upassword!="":
                DBSession.add(User(name=Uname, password=Upassword, aboutme=Uabout))
                DBSession.commit
                header_s = remember(request, User.name)
                return HTTPFound(location='/index', headers=header_s)
            else: return {'message':"notenough"}
        else: return {'message':"login"}
    return{}
