'''
Router xử lý cho chức năng login
'''

from flask import Blueprint, request, render_template, redirect

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET"])
def login():
    return render_template('login/index.html')

@login_bp.route("/logout", methods=["GET"])
def logout():
    #logout, huy session
    pass
    #return redirect()

@login_bp.route("/login", methods=["POST"])
def auth():
    data = request.form
    username = data["username"]
    password = data["password"]

    if username == "" or password == "":
        #return render_template("login.html",error="Tên đăng nhập hoặc mật khẩu không được để trống.")
        pass
    
    pass
    #return redirect()