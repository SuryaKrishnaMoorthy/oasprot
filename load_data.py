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


DB_USER = 'micro'
DB_SERVER = 'db'
DB_NAME = 'micro'

# uri for PostgreSQL
uri = f'postgres+psycopg2://{DB_USER}@{DB_SERVER}:5432/{DB_NAME}'

db = init_db(uri)

proteins = [
    Protein(id='Q14765', name='STAT4_HUMAN'),
    Protein(id='P42228', name='STAT4_MOUSE'),
    Protein(id='F1M9D6', name='F1M9D6_RAT'),
    Protein(id='A0A0G2JX93', name='A0A0G2JX93_RAT'),
]

r = db.bulk_save_objects(proteins, return_defaults=True)
db.commit()
print(r)
