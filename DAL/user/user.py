from DAL import db, dsn


class User:
    def __init__(self) -> None:
        pass

    def get_role(self, username) -> dict:
        # SELECT * FROM SESSION_PRIVS;
        # SELECT * FROM SESSION_ROLES;
        pass

    def login(self, username, password) -> None:
        try:
            conn = db.connect(user=username, password=password,
                              dsn=dsn, encoding="UTF-8")
            self.conn = conn
        except db.DatabaseError as err:
            print("There is a problem with Oracle", err)

    def create_user(self, username, password):
        # check quyen
        # tao user
        pass
