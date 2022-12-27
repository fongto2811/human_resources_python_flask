'''
Router xử lý cho chức năng login
'''

from flask import Blueprint, request, render_template, redirect

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET"])
def login():
    pass
    #return render_template("login.html",error=None)

@login_bp.route("/logout", methods=["POST"])
def logout():
    #logout, huy session
    pass
    #return redirect()

@login_bp.route("/login", methods=["POST"])
def auth():
    data = request.form
    username = data["username"]
    password = data["password"]

    # kiểm tra dữ liệu đầu vào
    if username == "" or password == "":
        #return render_template("login.html",error="Tên đăng nhập hoặc mật khẩu không được để trống.")
        pass
    
    # gọi tới BLL xử lí chức năng login
    pass
    #return redirect()