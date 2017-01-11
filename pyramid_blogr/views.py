from pyramid.response import Response
from pyramid.renderers import render
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.security import remember, forget
from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    User,
    Article
    # MyModel,
    )

@view_config(route_name='home', renderer='templates/autorisation.jinja2')
def home(request):
    if 'form.submitted' in request.params:
        login=request.params['login']
        password = request.params['password']
        DBSession = Session(bind=engine)
        user = DBSession.query(User).filter(login==User.name).first()
        if user!=None and user.passwordget(login) == password:
            headers = remember(request.login)
            return HTTPFound(location=index.jinja2, headers=headers)
        else:
            return HTTPNotFound('incorrect login or password')



@view_config(route_name='view_blog',renderer='templates/index.jinja2')
def view_blog(request):
    posts=DBSession.query(Article).order_by(desc(Post.id))    
    return dict(posts=posts)

@view_config(route_name='view_my',renderer='templates/my.jinja2')
def view_my(request):
    posts=DBSession.query(Article).filter_by(id=user_id).order_by(desc(Post.id))    
    return dict(posts=posts)


@view_config(route_name='blog_article', renderer='templates/post.jinja2')
def blog_article(request):
    DBSession=Session(bind=engine)
    id = request.matchdict['postid']
    post=DBSession.query(Article).filter_by(id=postid).first()
    title= post.title
    content= post.content   
    if (post is None):
        return HTTPNotFound('No such page')
    else:
        return {'post':post,
                'ouser': get_user(request.authenticated_userid)}


@view_config(route_name='blog_create', renderer='templates/newPost.jinja2')
def blog_create(request):
    form = get_form(request)
    if 'form.submitted' in request.params:
        Ptitle = request.params['title']
        Pcontent = request.params['content']
        article= Article(title=Ptitle, content=Pcontent, u_id=get_user(request.authenticated_userid).id, Cdate=datetime.now())
        DBSession.add(article)
        DBSession.commit()
        return HTTPFound(location = '/post/'+str(article.id))

@view_config(route_name='login', renderer='templates/autorisation.jinja2')
def login(request):
    if 'form.submitted' in request.params:
        login=request.params['login']
        password = request.params['password']
        DBSession = Session(bind=engine)
        user = DBSession.query(User).filter(login==User.name).first()
        if user!=None and user.passwordget(login) == password:
            headers = remember(request.login)
            return HTTPFound(location=index.jinja2, headers=headers)
        else:
            return HTTPNotFound('incorrect login or password')
        
@view_config(route_name='logout')
def logout(request):
    headers=forget(request)
    return HTTPFound(location=autorisation.jinja2, headers=headers)
        
@view_config(route_name='register', renderer='templates/registration.jinja2')
def register(request):
    form=RegistrationForm(request.POST)
    if request.method =='POST' and form.validate():
        Uname = request.params['username']
        Upassword = request.params['password']
        Uabout= request.params['aboutme']
        DBSession = Session(bind=engine)
        if DBSession.query(User).filter_by(name=Uname).first==None:
            if Uname!=None and Upassword!=None:
                new_user=User(name=Uname, password=Upassword,aboutme=Uabout)
                DBSession.add(new_user)
                DBSession.commit()
                headers = remember (request, Uname)
                return HTTPFound(location=index.jinja2, headers=headers)