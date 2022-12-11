'''
Khởi tạo Blueprint
'''
from flask import Blueprint

blue_print = Blueprint('errors',__name__)

from UI.errors import handlers