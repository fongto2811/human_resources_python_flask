'''
Router xử lý cho chức năng user
'''

from flask import Blueprint, request, render_template, redirect

user_bp = Blueprint("user", __name__)

@user_bp.route("/users", methods=["GET"])
def list_user():
    return render_template('users/index.html', page = 5)