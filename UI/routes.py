from UI import ui
from flask import render_template, redirect
import json

@ui.route('/users')
def user():
    users =[
        {
        "username" : "phongto",
        "tablespace" : "temp01",
        "quota" : "10M",
        "status" : "lock",
        "profile" : "default",
        "role" : "admin",
        },
        {
        "username" : "thach",
        "tablespace" : "temp03",
        "quota" : "20M",
        "status" : "unlock",
        "profile" : "admin",
        "role" : "admin",
        },
        {
        "username" : "phongdao",
        "tablespace" : "temp03",
        "quota" : "30M",
        "status" : "lock",
        "profile" : "",
        "role" : "user",
        },
        {
        "username" : "minhluan",
        "tablespace" : "temp04",
        "quota" : "100M",
        "status" : "unlock",
        "profile" : "",
        "role" : "",
        },
        {
        "username" : "hayhey",
        "tablespace" : "temp05",
        "quota" : "",
        "status" : "lock",
        "profile" : "",
        "role" : "",
        },
        {
        "username" : "ayahae",
        "tablespace" : "",
        "quota" : "",
        "status" : "lock",
        "profile" : "",
        "role" : "",
        },
    ]
    print(users[0]["username"])
    return render_template('users/index.html', page = 5)
@ui.route('/profiles')
def profile():
    return render_template('profiles/index.html', page = 5)