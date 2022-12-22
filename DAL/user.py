from cx_Oracle import connect

class UserDAL:
    def __init__(self, username, password) -> None:
        connect_string = '{0}/{1}@localhost:1521/xe'
        try:
            conn = connect(connect_string.format(username,password))
        except:
            pass