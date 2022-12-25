from cx_Oracle import connect, DatabaseError, makedsn, SYSDBA

dsn_tns = makedsn('localhost','1521',service_name='orclpdb.localdomain')
class UserDAL:
    def __init__(self, username, password) -> None:
        try:
            conn = connect(user=username, password=password, dsn=dsn_tns, encoding="UTF-8")
            cursor = conn.cursor()
            sql = "select user from dual"
            cursor.execute(sql)
            for row in cursor:
                print(row)
        except DatabaseError as error:
            print("There is a problem with Oracle", error)

if __name__ == '__main__':
    UserDAL('phong','123')