from flask import Flask, session
from flask_session import Session
from flask_bcrypt import Bcrypt
app = None


def setup_app(**config_overrides):

    global app
    app = Flask("human_resources")

    # Load file config
    app.config.update(config_overrides)

    # Session
    Session(app)
    # Hash password
    Bcrypt(app)
    # Định nghĩa các đường dẫn
    register_path(app)

    return app


def register_path(app):
    from UI.routers.login import login_bp
    from UI.routers.user import user_bp
    from UI.routers.profile import profile_bp
    from UI.routers.role import role_bp
    app.register_blueprint(login_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(role_bp)
