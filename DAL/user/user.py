from DAL import db, dsn, config
from datetime import datetime
from flask_bcrypt import check_password_hash, generate_password_hash
from flask import session


class UserDAL:
    def __init__(self) -> None:
        conn = db.connect(user=session['current_user']['username'],
                          password=session['raw_pwd'], dsn=dsn, encoding="UTF-8")
        self.conn = conn

    def check_privilege(self, privilege) -> tuple:
        with self.conn.cursor() as cursor:
            sql = "select * from SESSION_PRIVS WHERE privilege=':privilege'"
            cursor.execute(sql, privilege=privilege)
            result = cursor.fetchone()
        return result

    def check_object_privilege(self, object, privilege) -> tuple:
        with self.conn.cursor() as cursor:
            sql = "SELECT * FROM user_tab_privs_recd WHERE table_name=:object and privilege=:privilege"
            cursor.execute(sql, object=object, privilege=privilege)
            result = cursor.fetchone()
        return result

    def get_user_info(username, password) -> dict:
        try:
            conn = db.connect(user=config.ORACLE_SYS_USERNAME,
                              password=config.ORACLE_SYS_PASSWORD, dsn=dsn, encoding="UTF-8", mode=db.SYSDBA)

            with conn.cursor() as cursor:
                sql = "select * from admin.user_info where username=:username"
                cursor.execute(sql, username=username)

                key = tuple(('id', 'first_name', 'last_name',
                            'username', 'password', 'email', 'phone', 'address', 'img'))
                value = cursor.fetchone()

                if value is None:
                    print("{}: Tên đăng nhập không đúng.".format(
                        datetime.utcnow()))
                    raise Exception('Tên đăng nhập không đúng.')
                else:
                    result = dict(zip(key, value))
                    if not check_password_hash(result['password'], password):
                        raise Exception('Mật khẩu không đúng.')
            session['raw_pwd'] = password
            return result

        except db.DatabaseError as err:
            error = "{}".format(err)
            if 'ORA-01017' in error:
                raise Exception('Tên đăng nhập hoặc mật khẩu không đúng.')

        except Exception as error:
            raise error

    def create_user(self, username, password, temp_table_space, table_space, quota) -> bool:
        try:
            with self.conn.cursor() as cursor:
                sql = """CREATE USER :username IDENTIFIED BY :password
                        TEMPORARY TABLESPACE :temp_table_space
                        DEFAULT TABLESPACE :table_space
                        QUOTA :quota ON :table_space"""
                cursor.execute(sql, username=username, password=password,
                               temp_table_space=temp_table_space, table_space=table_space, quota=quota)
        except db.DatabaseError as err:
            error = "{}".format(err)
            if 'ORA-01920' in error:
                raise Exception(
                    'Tên đăng nhập bị trùng. Vui lòng nhập tên khác.')
            if 'ORA-10615' in error:
                raise Exception(
                    'TABLESPACE hoặc TEMPORARY TABLESPACE không tồn tại.')
        # tao user
        try:
            with self.conn.cursor() as cursor:
                sql = "INSERT INTO ADMIN.USER_INFO(USERNAME,PASSWORD) VALUES(:username,:password)"
                cursor.execute(sql, username=username,
                               password=generate_password_hash(password))
        except db.DatabaseError as err:
            error = "{}".format(err)
            raise error
        return True

    def list_user(self) -> list:
        with self.conn.cursor() as cursor:
            sql = """
            SELECT DBA_USERS.user_id,DBA_USERS.username,DBA_USERS.default_tablespace,dba_ts_quotas.max_bytes,DBA_USERS.account_status,DBA_USERS.profile,dba_ROLE_PRIVS.granted_role
            FROM DBA_USERS
            LEFT JOIN dba_ts_quotas
            ON dba_ts_quotas.tablespace_name = DBA_USERS.default_tablespace and dba_ts_quotas.username = DBA_USERS.username
            LEFT JOIN dba_ROLE_PRIVS
            ON dba_role_privs.grantee = DBA_USERS.username
            """
            cursor.execute(sql)
            result = cursor.fetchall()

            key = tuple(('id', 'username', 'tablespace',
                         'quota', 'status', 'profile', 'role'))

            list_result = [dict(zip(key, value)) for value in result]
        return list_result
