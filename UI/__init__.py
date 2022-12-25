from flask import Flask
app = None

def setup_app(**config_overrides):
    
    global app
    app = Flask(__name__)

    # Load file config
    app.config.from_object("app.config")
    app.config.update(config_overrides)

    # Định nghĩa các đường dẫn
    register_path(app)
    # Định nghĩa các BLL
    register_bll(app)
    
    return app

def register_path(app):
    from UI.routers import login
    app.register_blueprint(login)

def register_bll(app):
    pass