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

if __name__ == '__main__':
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(debug=True)