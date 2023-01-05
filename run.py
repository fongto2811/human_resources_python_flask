'''
Chạy chương trình
'''
from flask import session, redirect, url_for, request
from UI import setup_app
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = setup_app(
    ENV=os.environ["FLASK_ENV"],
    DEBUG=os.environ["FLASK_DEBUG"],
    SECRET_KEY="T0Th@nhph0ngT0nTh!enTh@chd@0quyeTph0ng",
    SESSION_PERMANENT=os.environ["SESSION_PERMANENT"],
    SESSION_TYPE=os.environ["SESSION_TYPE"],
)


# @app.before_request
# def check_login():
#     if 'current_user' not in session and '/login' not in request.path:
#         return redirect('/login')

@app.context_processor
def global_variables():
    current_user = None
    if 'current_user' in session:
        current_user = session['current_user']
    return dict(current_user=current_user)


app.template_folder = join(dirname(__file__), 'UI/templates')
app.static_folder = join(dirname(__file__), 'UI/static')

if __name__ == "__main__":
    app.run(host=os.environ["HOST"], port=os.environ["PORT"])
