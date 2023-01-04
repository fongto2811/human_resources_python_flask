'''
Router xử lý cho chức năng login
'''

from flask import Blueprint, request, render_template, redirect, session
from BLL.login import 


login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET"])
def login():
    if 'current_user' in session and session['current_user'] != None:
        return redirect('/')
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
        return render_template('login/index.html', error="Tên đăng nhập hoặc mật khẩu không được để trống.")

    
    current_user = dict()
    
    return 'a'
