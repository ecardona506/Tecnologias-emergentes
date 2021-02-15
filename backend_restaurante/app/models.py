from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    usuario_id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), unique=True, nullable = False)
    contraseña = db.Column(db.String(30), nullable = False)
    restaurantes = db.relationship('Restaurante')

    def __init__(self, email, contraseña):
        self.email = email
        self.contraseña = contraseña

class Restaurante(db.Model):
    restaurante_id = db.Column(db.Integer, primary_key = True)
    nombre_restaurante = db.Column(db.String(50), nullable = False)
    lugar = db.Column(db.String(40), nullable = False)
    direccion = db.Column(db.String(50), nullable = False)
    telefono = db.Column(db.BigInteger, nullable= False)
    categoria = db.Column(db.String(14), nullable = False)
    domicilio = db.Column(db.Boolean, nullable = False)
    fecha_creacion = db.Column(db.DateTime, default = datetime.now())
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.usuario_id'), nullable = False)

    def __init__(self, nombre, lugar, direccion, telefono, categoria, domicilio, usuario_id):
        self.nombre_restaurante = nombre
        self.lugar = lugar
        self.direccion = direccion
        self.telefono = telefono
        self.categoria = categoria
        self.domicilio = domicilio
        self.usuario_id = usuario_id