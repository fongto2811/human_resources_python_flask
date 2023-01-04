'''
Router xử lý cho chức năng profile
'''

from flask import Blueprint, request, render_template, redirect

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profiles", methods=["GET"])
def list_profile():
    return render_template('profiles/index.html', page = 'profile')