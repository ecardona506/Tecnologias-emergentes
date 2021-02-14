from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

app = Flask(__name__)

#Conexión base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/db_restaurante'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Usuario(db.Model):
    usuario_id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(30), unique=True, nullable = False)
    contraseña = db.Column(db.String(30), nullable = False)

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
    fecha_creacion = db.Column(db.Date, nullable = False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.usuario_id'), nullable = False)
    usuario = db.relationship('Usuario')

    def __init__(self, nombre, lugar, direccion, telefono, categoria, domicilio, usuario_id):
        self.nombre_restaurante = nombre
        self.lugar = lugar
        self.direccion = direccion
        self.telefono = telefono
        self.categoria = categoria
        self.domicilio = domicilio
        self.fecha_creacion = datetime.now()
        self.usuario_id = usuario_id

db.create_all()

class EsquemaUsuario(ma.Schema):
    class Meta:
        campos = ('usuario_id', 'email', 'contraseña')

class EsquemaRestaurante(ma.Schema):
    class Meta:
        campos = ('restaurante_id','nombre_restaurante','lugar',
        'direccion','telefono','categoria','domicilio','fecha_creacion',
        'usuario_id')

UserSchema = EsquemaUsuario()
RestaurantSchema = EsquemaRestaurante()

@app.route('/registro', methods = ['POST'])
def registrar():
    email = request.json['email']
    contraseña = request.json['contraseña']
    new_user = Usuario(email,contraseña)
    db.session.add(new_user)
    db.session.commit()
    return UserSchema.jsonify(new_user)

if __name__ == '__main__':
    app.run(debug=True)