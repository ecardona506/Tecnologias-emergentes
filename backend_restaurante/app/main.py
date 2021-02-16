#Librerias
from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
#Recursos propios
from config import Config, DevelopmentConfig
from models import db, Usuario, Restaurante
from schemas import ma
from api import api

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

@app.route('/registro', methods = ['POST'])
def registrar():
    email = request.json['email']
    contraseña = request.json['contraseña']
    new_user = Usuario(email,contraseña)
    db.session.add(new_user)
    db.session.commit()
    return UserSchema.jsonify(new_user)

@app.route('/crear_restaurante', methods = ['POST'])
def crear_restaurante():
    if "usuario" in session:
        nombre = request.json['nombre_restuarante']
        lugar = request.json['lugar']
        direccion = request.json['direccion']
        telefono = request.json['categoria']
        domicilio = request.json['domicilio']
        usuario_id = session['usuario']
        new_restaurant = Restaurante(nombre, lugar, direccion, telefono, domicilio, usuario_id)
        db.session.add(new_restaurant)
        db.commit()
        return "Restaurante agregado satisfactoriamente"

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)