'''
Router xử lý cho chức năng login
'''

from flask import Blueprint, request, render_template, redirect, session
<<<<<<< HEAD


=======
from BLL.user.user import UserBLL
>>>>>>> 4c5bc01aeb92f49e1a077189157f190198ed32e0

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
    try:
        data = request.form
        username = data["username"]
        password = data["password"]

        if username == "" or password == "":
            return render_template('login/index.html', error="Tên đăng nhập hoặc mật khẩu không được để trống.")
            
        current_user = dict(UserBLL.get_user_info(username, password))
        session['current_user'] = current_user

        return redirect('/')
    except Exception as err:
        return render_template('login/index.html', error=err)



@login_bp.route("/", methods=["GET"])
def homepage():
    return render_template('login/homepage.html')
 