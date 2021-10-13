"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


default = 'https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png'


class users(db.Model):
    __tablename__ = 'users'

    def __repr__(self):
        return f'id: {self.id} firstName: {self.first_name} lastName: {self.last_name} profilePic: {self.image_url}'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    image_url = db.Column(
        db.String, nullable=False, default=default)

    def greet(self):
        return f'Hello, my name is {self.first_name} {self.last_name}.'

    def update_image(self, url=default):
        self.image_url = url
