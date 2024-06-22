import flask
from .models import Product
from project.settings import DATABASE
import flask_login

def show_shop_page():   
    try:
        user_name = flask_login.current_user.name
        is_admin = flask_login.current_user.is_admin
    except:
        user_name = None
        is_admin = False
    return flask.render_template(template_name_or_list = "shop.html", products = Product.query.all(), user_name = user_name, is_admin = is_admin)