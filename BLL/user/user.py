from DAL.user.user import UserDAL


class UserBLL:
    def __init__(self) -> None:
        return None

    def get_user_info(username, password) -> dict:
        return UserDAL.get_user_info(username, password)

    def create_user(username, password, temp_table_space, table_space, quota):
        if UserDAL().check_privilege('CREATE USER') is None:
            raise Exception('Bạn không có quyền tạo người dùng.')
        return UserDAL().create_user(username, password, temp_table_space, table_space, quota)

    def list_user():
        userdal = UserDAL()
        if userdal.check_object_privilege('DBA_USERS', 'SELECT') is None or userdal.check_object_privilege('DBA_TS_QUOTAS', 'SELECT') is None or userdal.check_object_privilege('DBA_ROLE_PRIVS', 'SELECT') is None:
            raise Exception('Bạn không có quyền.')
        return userdal.list_user()
