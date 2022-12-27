from flask import Flask
app = None

def setup_app(**config_overrides):
    
    global app
    app = Flask("human_resources")

    # Load file config
    app.config.update(config_overrides)

    # Định nghĩa các đường dẫn
    register_path(app)
    # Định nghĩa các BLL
    register_bll(app)

    return app

def register_path(app):
    from UI.routers.login import login_bp
    from UI.routers.user import user_bp
    from UI.routers.profile import profile_bp
    app.register_blueprint(login_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(profile_bp)

def register_bll(app):
    pass