from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('view_blog', '/') #главная
    config.add_route('register', '/register')#регистрация
    config.add_route('view_my', '/')#статьи пользователя
    config.add_route('blog_article', '/')#отобразить статью
    config.add_route('blog_create','/{postid}')#создать статью
    config.add_route('login')#вход
    config.add_route('logout')#выход
    config.scan()
    return config.make_wsgi_app()
