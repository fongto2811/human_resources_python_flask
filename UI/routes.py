from UI import ui
from flask import render_template, redirect

@ui.route('/')
def home():
    return render_template('users/index.html', page = 5)