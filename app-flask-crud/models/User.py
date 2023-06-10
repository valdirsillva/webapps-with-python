
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Recebe uma instância do db.model
class User(db.Model):
    # nome da tabela que será criada no banco de dados
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.String(30))
    address = db.Column(db.String(120))

    # Método para serializar os dados
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'address': self.address
        }
