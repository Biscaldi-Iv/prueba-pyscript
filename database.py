from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("sqlite:////tmp/test.db",
                       connect_args={'check_same_thread': False})

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """you will have to import all modules that
     might define models before calling init_db()"""
    Base.metadata.create_all(bind=engine)
