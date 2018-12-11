# Standard Libraries
import os

# External Libraries
import connexion
from flask_cors import CORS
from .schemas.orm import init_db, Protein
import requests


# environment variables
DB_USER = os.environ['DB_USER']
DB_SERVER = os.environ['DB_SERVER']
DB_NAME = os.environ['DB_NAME']

# uri for PostgreSQL
uri = f'postgres+psycopg2://{DB_USER}@{DB_SERVER}:5432/{DB_NAME}'


def get_protein(proteinId) -> dict:
    r = db.query(Protein).filter(Protein.id == proteinId).one()

    return {'id': r.id, 'name': r.name}


def get_protein_seq(proteinId) -> dict:
    r = requests.get(f'https://www.uniprot.org/uniprot/{proteinId}.fasta')

    return {'fasta': r.content.decode('utf-8'), 'id': proteinId}


def get_protein_features(proteinId) -> dict:
    pass


# options
options = {'swagger_ui': False}

# create flask app
app = connexion.FlaskApp(__name__, port=7878, specification_dir='schemas/')
app.add_api('api.yaml', strict_validation=True, options=options)
CORS(app.app)

db = init_db(uri)
