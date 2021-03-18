from . import db
from flask_login._compat import unicode


class PropertyMod(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True, unique=True)
    title = db.Column(db.String(225))
    bedrooms = db.Column(db.String(20))
    bathrooms = db.Column(db.String(20))
    location=db.Column(db.String(225))
    price= db.Column(db.String(225))
    type= db.Column(db.String(80))
    desc= db.Column(db.String(225))
    filename=db.Column(db.String(225))

    def __init__(self, title, bedrooms, bathrooms, location, price, type, desc, filename):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.location = location
        self.price = price
        self.type = type
        self.desc = desc
        self.filename=filename
    '''
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    '''
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<PropertyMod %r>' % (self.title)

