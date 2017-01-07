from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramod.security import remember, forget
from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    # MyModel,
    )


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    try:
        # one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
        one = 1;
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'pyramid_blogr'}


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_pyramid_blogr_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

@view_config(route_name='view_blog',renderer='../Сайт/index.html')
def view_blog(request):
    posts=DBSession.query(Article).order_by(desc(Post.id))    
    return dict(posts=posts)

@view_config(route_name='view_my',renderer='../Сайт/My.html')
def view_my(request):
    posts=DBSession.query(Article).filter_by(id=user_id).order_by(desc(Post.id))    
    return dict(posts=posts)


@view_config(route_name='blog_article', renderer='../Сайт/Post.html')
def blog_article(request):
    id = request.matchdict['postid']
    post=DBSession.query(Article).filter_by(id=postid).first()    
    if (post is None):
        return HTTPNotFound('No such page')


@view_config(route_name='blog_create',
             renderer='../Сайт/newPost.html')
def blog_create(request):
    form = get_form(request)
    if 'form.submitted' in request.params:
        title = request.params['title']
        content = request.params['content']
        article = Article(title,content)
        DBSession.add(article)
        return HTTPFound(location=request.route_url('view_blog'))
    article=Article('','')
    return dict(article=article, logged_in=authenticated_user_id(request))

@view_config(route_name='login', render='../Сайт/Autorisation.html')
def login(request)
    if 'form.submitted' in request.params:
        login=request.params['login']
        password = request.params['password']
        if User.get(login) == password:
            headers=remember(request.login)
            return HTTPFound(location=index.html, headers=headers)
        message = 'Fail'
    return dict(
        message=message,
        login=login,
        password=password,
    )
        
@view_config(route_name='logout')
def logout(request):
    headers=forget(request)
    return HTTPFound(location=Autorisation.html, headers=headers)
        
@view_config(route_name='register', render='../Сайт/Registration.html')
def register(request):
    form=RegistrationForm(request.POST)
    if request.method =='POST' and form.validate():
        new_user=User(name=form.username.data)
        new_user.set_password(form.password.data.encode('utf8'))
        new_user.aboutme(form.aboutme.data.)
        request.dbsession.add(new_user)
        return HTTPFound(location=request.rout_url('view_blog'))
    return {'form':form}
    
