import flask
from project.settings import DATABASE
from shop_app.models import Product
import flask_login

def show_home_app():
    # if flask.request.method == "POST":
        # new_product = Product(
            # name = flask.request.form["name"],
            # description = flask.request.form["description"],
            # price = flask.request.form["price"],
            # count = flask.request.form["count"]
        # )
        # DATABASE.session.add(new_product)
        # DATABASE.session.commit()
    try:
        user_name = flask_login.current_user.name
        is_admin = flask_login.current_user.is_admin
    except:
        user_name = None
        is_admin = False
    return flask.render_template("index.html", user_name = user_name, is_admin = is_admin)