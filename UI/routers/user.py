'''
Router xử lý cho chức năng user
'''

from flask import Blueprint, request, render_template, redirect, g
from BLL.user.user import UserBLL

user_bp = Blueprint("user", __name__)

users = [
    {
        "id": "1",
        "username": "phongto",
        "tablespace": "temp01",
        "quota": "10M",
        "status": "lock",
        "profile": "default",
        "role": "admin",
    },
    {
        "id": "2",
        "username": "thach",
        "tablespace": "temp03",
        "quota": "20M",
        "status": "unlock",
        "profile": "admin",
        "role": "admin",
    },
    {
        "id": "3",
        "username": "phongdao",
        "tablespace": "temp03",
        "quota": "30M",
        "status": "lock",
        "profile": "",
        "role": "user",
    },
    {
        "id": "4",
        "username": "minhluan",
        "tablespace": "temp04",
        "quota": "100M",
        "status": "unlock",
        "profile": "",
        "role": "",
    },
    {
        "id": "5",
        "username": "hayhey",
        "tablespace": "temp05",
        "quota": "",
        "status": "lock",
        "profile": "",
        "role": "",
    },
    {
        "id": "6",
        "username": "ayahae",
        "tablespace": "",
        "quota": "",
        "status": "lock",
        "profile": "",
        "role": "",
    },
    {
        "id": "7",
        "username": "phongto",
        "tablespace": "temp01",
        "quota": "10M",
        "status": "lock",
        "profile": "default",
        "role": "admin",
    },
    {
        "id": "8",
        "username": "thach",
        "tablespace": "temp03",
        "quota": "20M",
        "status": "unlock",
        "profile": "admin",
        "role": "admin",
    },
    {
        "id": "9",
        "username": "phongdao",
        "tablespace": "temp03",
        "quota": "30M",
        "status": "lock",
        "profile": "",
        "role": "user",
    },
    {
        "id": "10",
        "username": "minhluan",
        "tablespace": "temp04",
        "quota": "100M",
        "status": "unlock",
        "profile": "",
        "role": "",
    },
    {
        "id": "11",
        "username": "hayhey",
        "tablespace": "temp05",
        "quota": "",
        "status": "lock",
        "profile": "",
        "role": "",
    },
    {
        "id": "12",
        "username": "ayahae",
        "tablespace": "",
        "quota": "",
        "status": "lock",
        "profile": "",
        "role": "",
    },
]


@user_bp.route("/users", methods=["GET"])
def list_user():
    return render_template('users/index.html', user=users)


@user_bp.route("/users/create", methods=['POST'])
def create_user():
    pass
