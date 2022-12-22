from cx_Oracle import connect, DatabaseError

class UserDAL:
    def __init__(self, username, password) -> None:
        try:
            conn = connect(user=username, password=password,host="localhost", port=1521, service_name="ORCLPDB.LOCALDOMAIN")
            print(conn.version)
        except DatabaseError as e:
            print("There is a problem with Oracle", e)

if __name__ == '__main__':
    UserDAL('amy','amy')