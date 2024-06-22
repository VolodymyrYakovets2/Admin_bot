import flask 
from flask_login import login_user, current_user
from registration_app.models import User

def show_login_page():
    if flask.request.method == "POST":
        name = flask.request.form["name"]
        password = flask.request.form["password"]
        users = User.query.all()
        for user in users:
            if user.name == name and user.password == password:
                login_user(user)
                return flask.redirect("/")
            
    is_admin = False
    if current_user.is_authenticated:
        is_admin = current_user.is_admin
    
    
    return flask.render_template(template_name_or_list = "login.html", is_admin = is_admin)