'''
Chạy chương trình
'''
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

from UI import setup_app
app = setup_app()

if __name__ == "__main__":
    app.run(host=os.environ["HOST"],port=os.environ["PORT"],debug=os.environ["DEBUG"])
