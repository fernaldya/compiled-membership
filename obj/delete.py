from obj.db import connect_pg


def delete_membership_pg(membership_name):
    conn = connect_pg()
    try:
        with conn.cursor() as cursor:
            sql_fetch = 'SELECT id FROM memberships WHERE name = %s'
            cursor.execute(sql_fetch, (membership_name,))
            membership_id = cursor.fetchone()[0]
            if not membership_id:
                return 'Membership not found!'
            else:
                sql_delete = 'DELETE FROM memberships WHERE id = %s'
                cursor.execute(sql_delete, (membership_id,))
                conn.commit()
                return 'Membership deleted!'
    finally:
        conn.close()

def delete_owner_pg(owner_name):
    conn = connect_pg()
    try:
        with conn.cursor() as cursor:
            sql_delete = 'delete from owners where owner = %s'
            cursor.execute(sql_delete, (owner_name,))
            conn.commit()
            return 'Owner deleted!'
    finally:
        conn.close()
