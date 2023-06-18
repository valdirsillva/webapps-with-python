from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    name = db.Column(db.String(30))
    phone_number = db.Column(db.String(15))
    address = db.Column(db.String(45))
    cpf = db.Column(db.String(11))

    def serialize():
        return {
            'id': self.id,
            'username': self.username,
            'name': self.name,
            'phone_number': self.phone_number,
            'address': self.address,
            'cpf': self.cpf,
        }
