from pyramid.response import Response
from pyramid.view import view_config

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
@view_config(route_name='blog',
             renderer='../Сайт/index.html')
def index_page(request):
    page = int(request.params.get('page', 1))
    paginator = Article.get_paginator(request, page)
    return {'paginator': paginator}


@view_config(route_name='blog_article', renderer='../Сайт/Post.html')
def blog_view(request):
    id = int(request.matchdict.get('id', -1))
    article = Article.by_id(id)
    if not article:
        return HTTPNotFound()
    return {'article': article}


@view_config(route_name='blog_create',
             renderer='../Сайт/newPost.html')
def blog_create(request):
    form = get_form(request)
    if request.method == 'POST':
        try:
            values = form.validate(request.POST.items())
        except deform.ValidationFailure as e:
            return {'form': e.render(),
                    'action': request.matchdict.get('action')}


@view_config(route_name='auth', match_param='action=in', renderer='string',
             request_method='POST')
@view_config(route_name='auth', match_param='action=out', renderer='string')
def sign_in_out(request):
    return {}
