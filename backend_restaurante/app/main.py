from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

#Conexión base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymsql://root@localhost/db_restaurante'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Usuario(db.Model):
    usuario_id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), unique=True, nullable = False)
    contraseña = db.Column(db.String(30), nullable = False)

class Restaurante(db.Model):
    restaurante_id = db.Column(db.Integer, primary_key = True)
    nombre_restaurante = db.Column(db.String(50), nullable = False)
    lugar = db.Column(db.String(40), nullable = False)
    direccion = db.Column(db.String(50), nullable = False)
    telefono = db.Column(db.BigInteger, nullable= False)
    categoria = db.Column(db.String(14), nullable = False)
    domicilio = db.Column(db.Bool, nullable = False)
    fecha_creacion = db.Column(db.Date, nullable = False)
    usuario_id = db.Column(db.Integer, nullable = False, db.ForeignKey('usuario.usuario_id'))
    usuario = db.relationship('Usuario')

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)