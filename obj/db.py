import os
from dotenv import load_dotenv
import pymysql
import psycopg2


load_dotenv()
db_config = {
    'db_host': os.getenv("DB_HOST_MS"),
    'db_user': os.getenv("DB_USER_MS"),
    'db_pass': os.getenv("DB_PASS_MS"),
    'db_svc': os.getenv("DB_SRVC_MS"),
    'db_port': os.getenv("DB_PORT_MS")
}

db_config_pg = {
    'db_host': os.getenv("DB_HOST_PG"),
    'db_user': os.getenv("DB_USER_PG"),
    'db_pass': os.getenv("DB_PASS_PG"),
    'db_svc': os.getenv("DB_SRVC_PG"),
    'db_data': os.getenv("DB_DATA")
}


# Database
## Mysql
def connect_mysql():
    conn = pymysql.connect(
        host=db_config['db_host'],
        user=db_config['db_user'],
        password=db_config['db_pass'],
        database=db_config['db_svc'],
        port=int(db_config['db_port'])
    )
    return conn

## Postgresql
def connect_pg():
    conn = psycopg2.connect(
        dbname=db_config_pg['db_data'],
        user=db_config_pg['db_user'],
        password=db_config_pg['db_pass'],
        host=db_config_pg['db_host'],
        port=5432
    )
    return conn


if __name__ == '__main__':
    print('Successfully connected to the database!')
