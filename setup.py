from setuptools import setup, find_packages


APP_NAME = 'rssapi'
VERSION = '0.1.0'
AUTHOR = 'Surya Krishna Moorthy'

setup(
    name=APP_NAME,
    version=VERSION,
    author=AUTHOR,
    description='API server for ssgcid login',
    license='MIT',
    install_requires=[
        'Flask==1.0.2',       # dependency of connexion
        'connexion==2.0.2',
        'Flask-Cors==3.0.7',
        'SQLAlchemy==1.2.14',
        'requests==2.20.1',
        'gunicorn==19.9.0',
        'psycopg2-binary==2.7.6.1',
    ],
    packages=find_packages(),
)
