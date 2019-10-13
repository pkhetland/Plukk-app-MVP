from app import db


class Contact(db.Model):
    __tablename__ = 'app_contacts'

    name = db.Column(db.String(), primary_key=True)
    email = db.Column(db.String())

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Name {}>'.format(self.name)

    def serialize(self):
        return {
            'name': self.name,
            'email': self.email
        }
