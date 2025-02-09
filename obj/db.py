import os
from dotenv import load_dotenv
import psycopg2


load_dotenv()
db_config_pg = {
    'db_host': os.getenv("DB_HOST_PG"),
    'db_user': os.getenv("DB_USER_PG"),
    'db_pass': os.getenv("DB_PASS_PG"),
    'db_svc': os.getenv("DB_SRVC_PG"),
    'db_data': os.getenv("DB_DATA")
}


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
