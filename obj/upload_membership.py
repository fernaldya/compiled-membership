import os
import pymysql
from dotenv import load_dotenv


load_dotenv()

db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")
db_svc = os.getenv("DB_SRVC")


conn = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_pass,
    database=db_svc
)


cursor = conn.cursor()


cursor.close()
conn.close()
