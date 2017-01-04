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
     config.add_route('blog', '/') #главная
    config.add_route('registration', '/')#регистрация
    config.add_route('my', '/')#статьи пользователя
    config.add_route('blog_article', '/article/{id:\d+}')#отобразить статью
    config.add_route('blog_action', '/article/{id:\d+}/{action}')#создать/удалить статью
    config.add_route('auth', '/sign/{action}')#вход/выход
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
