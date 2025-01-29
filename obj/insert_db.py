from obj.db import connect_mysql, connect_pg


def insert_data_mysql(name, file_path=None, number=None):
    conn = connect_mysql()
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO memberships (name, membership_uri, membership_number) values (%s, %s, %s)'
            cursor.execute(sql, (name, file_path, number))
        conn.commit()
    finally:
        conn.close()

def insert_data_pg(name, file_path=None, number=None):
    conn = connect_pg()
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO memberships (name, membership_uri, membership_number) values (%s, %s, %s)'
            cursor.execute(sql, (name, file_path, number))
        conn.commit()
    finally:
        conn.close()

if __name__ == '__main__':
    print('Data uploaded!')
