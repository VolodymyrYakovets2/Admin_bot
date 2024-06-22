import flask
from shop_app.models import Product
import flask_login


def show_cart_page():
    list_products = []
    list_ids = []
    if flask.request.cookies:
        if flask.request.cookies.get("product") != None and flask.request.cookies.get("product") != "":
            list_id_products = flask.request.cookies.get("product").split(" ")
            for product_id in list_id_products:
                if product_id not in list_ids:
                    count_products = list_id_products.count(product_id)
                    list_products.append(Product.query.get(int(product_id)))
                    list_ids.append(product_id)
                    if list_products[-1].count <= count_products:
                        list_products[-1].count = count_products

    try:
        user_name = flask_login.current_user.name
        is_admin = flask_login.current_user.is_admin
    except:
        user_name = None
        is_admin = False

    return flask.render_template(template_name_or_list = "cart.html", products = list_products, user_name = user_name, is_admin = is_admin)
