'''
Router xử lý cho chức năng login
'''

from flask import Blueprint, request, render_template, redirect, session


login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET"])
def login():
    return render_template('login/index.html')


@login_bp.route("/logout", methods=["GET"])
def logout():
    session.pop('current_user')
    return redirect("/login")


@login_bp.route("/login", methods=["POST"])
def auth():
    data = request.form
    username = data["username"]
    password = data["password"]

    if username == "" or password == "":
        # return render_template("login.html",error="Tên đăng nhập hoặc mật khẩu không được để trống.")
        print("Tên đăng nhập hoặc mật khẩu không được để trống.")
        return 'b'

    current_user = dict()
    current_user['image'] = "https://vcdn1-dulich.vnecdn.net/2022/09/14/4-1663171508.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=S06yaNXNAEw5yuUNPbsJYA"
    current_user['username'] = username
    current_user['password'] = password
    session['current_user'] = current_user
    return 'a'
    # return redirect()
