import os
import sys
import transaction
from sqlalchemy import engine_from_config
from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )
from pyramid.scripts.common import parse_vars
from ..models import DBSession, Base, User, Article 


def main(argv=sys.argv):
    DBSession = Sessipn(bind=engine)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    user = User(name="admin",password="123456")
    DBSession.add(user)
    DBSession.commit()
