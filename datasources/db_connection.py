from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert
from config import *
# DB connection
engine = create_engine('mysql+pymysql://'+db_user+':' +
                       db_pass+'@'+db_host+'/'+database+'?charset=utf8mb4')

meta = MetaData()

conn_mysql = engine.connect()
