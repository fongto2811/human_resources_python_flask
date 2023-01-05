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
