import flask
import flask_login
from .models import User
from project.settings import DATABASE

def registration_page():
    # 
    if flask_login.current_user.is_authenticated == False:
        is_admin = False
        # Чи відправив користувач якісь данні 
        if flask.request.method == "POST":
            new_user = User(
                name = flask.request.form["name"], 
                password = flask.request.form["password"],
                is_admin = False
            )
            DATABASE.session.add(new_user)
            DATABASE.session.commit()
            is_registered = True
        else:
            is_registered = False
    else:
        is_registered = True
        is_admin = flask_login.current_user.is_admin
        
    return flask.render_template(template_name_or_list = "registration.html", is_registered = is_registered, is_admin = is_admin)