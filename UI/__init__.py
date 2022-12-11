'''
Đăng ký các Blueprint templates
'''
from flask import Flask

ui = Flask(__name__)

from UI.errors import blue_print as errors
ui.register_blueprint(errors)

from UI import routes, models
