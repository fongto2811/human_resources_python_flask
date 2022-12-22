'''
Đăng ký các Blueprint templates
'''
from flask import Flask

ui = Flask(__name__)

from UI import routes, models
