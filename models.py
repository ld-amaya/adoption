from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    """Creates the pets table"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    photo = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)

    def image_link(self):
        """Returns default image if not available"""

        return self.photo or "https://cdn.shopify.com/s/files/1/0799/9645/products/SmallPetLiner_large.jpg?v=1597352991"


def connect_db(app):
    """Connect to the database"""
    db.app = app
    db.init_app(app)
