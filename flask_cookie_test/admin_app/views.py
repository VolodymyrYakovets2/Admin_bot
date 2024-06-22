import flask
from shop_app.models import Product
from project.settings import DATABASE
import os
import flask_login

def render_admin():
    # Якщо було передано серверу дані нового товару, то завантажити його дані до бази
    try:
        if flask.request.method == "POST":
            if flask.request.form.get("del") != None:

                product_id = int(flask.request.form["del"])
                product_to_delete = Product.query.get(product_id)
                if product_to_delete != None:
                    DATABASE.session.delete(product_to_delete)
                    DATABASE.session.commit()
                    os.remove(os.path.abspath(__file__ + f"/../../shop_app/static/images/{product_to_delete.name}.png"))

            elif flask.request.form.get("submit_changes") != None:

                button_value = flask.request.form["submit_changes"].split("-")
                product = Product.query.get(button_value[1])
                if button_value[0] == "image":
                    image = flask.request.files["image"]
                    image_path = os.path.abspath(__file__ + f"/../../shop_app/static/images/{product.name}.png")
                    os.remove(path = image_path)
                    image.save(dst = image_path)
            else:
                product = Product(
                    name = flask.request.form["name"],
                    description = flask.request.form["description"],
                    count = flask.request.form["count"],
                    price = flask.request.form["price"],
                    discount = flask.request.form["discount"]
                )
                DATABASE.session.add(product)
                DATABASE.session.commit()
                image_file = flask.request.files["image"]
                image_file.save(os.path.abspath(__file__ + f"/../../shop_app/static/images/{product.name}.png"))
                
    except Exception as e:
        print(e)
    #
    try:
        user_name = flask_login.current_user.name
    except:
        user_name = None

    # 
    if flask_login.current_user.is_authenticated and flask_login.current_user.is_admin:
        return flask.render_template(template_name_or_list = "admin.html", products = Product.query.all(), user_name= user_name, is_admin = flask_login.current_user.is_admin)
    else:
        return flask.redirect("/")
    