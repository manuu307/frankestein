from db_connection import *

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('username', String(255), nullable=False),
)

meta.create_all(engine)
