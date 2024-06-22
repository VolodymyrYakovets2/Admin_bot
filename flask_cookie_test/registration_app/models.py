from project.settings import DATABASE
from flask_login import UserMixin

class User(DATABASE.Model, UserMixin):

    id = DATABASE.Column(DATABASE.Integer, primary_key = True)

    name = DATABASE.Column(DATABASE.String(60), nullable = False)
    password = DATABASE.Column(DATABASE.String(60), nullable = False)
    is_admin = DATABASE.Column(DATABASE.Boolean, nullable = False)
    
    def __repr__(self):
        return f"id - {self.id}; name - {self.name}; password - {self.password}"