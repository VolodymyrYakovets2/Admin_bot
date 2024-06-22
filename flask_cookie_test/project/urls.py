from cart_app import cart_app, show_cart_page
from shop_app import shop_app, show_shop_page
from home_app import home_app, show_home_app
from admin_app import admin, render_admin
from registration_app import registration, registration_page
from login_app import login, show_login_page
from .settings import shop_project


admin.add_url_rule(
    rule = "/admin/",
    view_func = render_admin,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = admin)

cart_app.add_url_rule(
    rule = "/cart/",
    view_func = show_cart_page,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = cart_app)

shop_app.add_url_rule(
    rule = "/shop/",
    view_func = show_shop_page,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = shop_app)

home_app.add_url_rule(
    rule = "/",
    view_func = show_home_app,
    methods = ["GET", "POST"]
)

shop_project.register_blueprint(blueprint = home_app)

registration.add_url_rule(
    rule = "/registration/", 
    view_func = registration_page,
    methods = ["GET", "POST"]
    )

shop_project.register_blueprint(blueprint = registration)

login.add_url_rule(
    rule = "/login/",
    view_func=show_login_page,
    methods = ["POST", "GET"]
)
shop_project.register_blueprint(blueprint=login)