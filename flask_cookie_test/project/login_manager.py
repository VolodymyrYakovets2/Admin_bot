import flask_login

from .settings import shop_project

from registration_app.models import User

login_manager = flask_login.LoginManager(app = shop_project)

shop_project.secret_key = "test_secret_key"

@login_manager.user_loader

def load_user(id):
    return User.query.get(id)