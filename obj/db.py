import os
from dotenv import load_dotenv
import pymysql


load_dotenv()
db_config = {
    'db_host': os.getenv("DB_HOST"),
    'db_user': os.getenv("DB_USER"),
    'db_pass': os.getenv("DB_PASS"),
    'db_svc': os.getenv("DB_SRVC")
}


# Database
def connect():
    conn = pymysql.connect(
        host=db_config['db_host'],
        user=db_config['db_user'],
        password=db_config['db_pass'],
        database=db_config['db_svc'],
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn
