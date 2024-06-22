import flask
import os
import flask_sqlalchemy
import flask_migrate

shop_project = flask.Flask(
    import_name = "project",
    instance_path = os.path.abspath(__file__ + "/..")
)

shop_project.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

DATABASE = flask_sqlalchemy.SQLAlchemy(app = shop_project)

migrate = flask_migrate.Migrate(app = shop_project, db = DATABASE)