'''
Router xử lý cho chức năng role
'''

from flask import Blueprint, request, render_template, redirect

role_bp = Blueprint("role", __name__)

@role_bp.route("/roles", methods=["GET"])
def list_roles():
    return render_template('role/index.html', page = 'roles')