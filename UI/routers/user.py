'''
Router xử lý cho chức năng user
'''

from flask import Blueprint, request, render_template, redirect, g, session
from BLL.user.user import UserBLL

user_bp = Blueprint("user", __name__)


@user_bp.route("/users", methods=["GET"])
def list_user():
    list_users = UserBLL.list_user()
    return render_template('users/index.html', user=list_users)


@user_bp.route("/users/create", methods=['POST'])
def create_user():
    try:
        data = request.form
        username = data["username"]
        password = data["password"]
        temp_table_space = data["temp_table_space"]
        table_space = data["table_space"]
        quota = data["quota"]

        if username == "" or password == "":
            pass
            # return render_template('login/index.html', error="Tên đăng nhập hoặc mật khẩu không được để trống.")
        print('router')
        if UserBLL.create_user(username, password,
                               temp_table_space, table_space, quota):
            return redirect('/users')
            
    except Exception as err:
        return err
        # return render_template('login/index.html', error=err)
