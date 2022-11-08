from flask import Blueprint, flash, render_template, request, session, abort, redirect, url_for
import os
from app import app

module = Blueprint('pages', __name__, url_prefix='/pages')

@module.route("/hello")
def hello():
    return render_template('pages/hello.html')