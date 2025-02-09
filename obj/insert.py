from psycopg2.errors import UniqueViolation
from obj.db import connect_pg


class MembershipExistsError(Exception):
    pass

def insert_data_pg(name, file_path=None, number=None, owner=None):
    conn = connect_pg()
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO memberships (name, membership_uri, membership_number, owner) values (%s, %s, %s, %s)'
            cursor.execute(sql, (name, file_path, number, owner))
        conn.commit()
    except UniqueViolation as exc:
        conn.rollback()
        print(f'Uniqueviolation error: {exc}')
        raise MembershipExistsError('Membership has already been uploaded before!') from exc
    finally:
        conn.close()

def add_owner_pg(owner):
    conn = connect_pg()
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO owners (owner) values (%s)'
            cursor.execute(sql, (owner,))
        conn.commit()
    except UniqueViolation as exc:
        conn.rollback()
        print(f'Uniqueviolation error: {exc}')
        raise MembershipExistsError('Owner has already been added before!') from exc
    finally:
        conn.close()

if __name__ == '__main__':
    try:
        insert_data_pg('qwerty')
        print('Data inserted successfully!')
    except MembershipExistsError as e:
        print('Error:', e)
