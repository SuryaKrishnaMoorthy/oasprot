from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


Base = declarative_base()


class Protein(Base):
    __tablename__ = 'proteins'

    id = Column(String(255), primary_key=True)
    name = Column(String(255))


def init_db(uri):
    engine = create_engine(uri, convert_unicode=True, echo=False)
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    Base.query = db_session.query_property()
    Base.metadata.create_all(bind=engine)
    return db_session
