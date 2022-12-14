from UI import ui
from flask import render_template, redirect

@ui.route('/users')
def user():
    return render_template('users/index.html', page = 5)
@ui.route('/profiles')
def profile():
    return render_template('profiles/index.html', page = 5)