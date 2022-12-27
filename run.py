'''
Chạy chương trình
'''
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from UI import setup_app
app = setup_app(
    ENV=os.environ["FLASK_ENV"],
    DEBUG=os.environ["FLASK_DEBUG"],
    SECRET_KEY="T0Th@nhph0ngT0nTh!enTh@chd@0quyeTph0ng",
)

app.template_folder = join(dirname(__file__), 'UI/templates')
app.static_folder = join(dirname(__file__), 'UI/static')

if __name__ == "__main__":
    app.run(host=os.environ["HOST"], port=os.environ["PORT"])
