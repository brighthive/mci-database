from setuptools import setup, find_packages

setup(
    name='mci_database',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'flask-sqlalchemy',
        'flask-restful',
        'flask-migrate',
        'psycopg2-binary'
    ],
)