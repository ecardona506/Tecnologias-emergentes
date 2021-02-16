from flask_restful import Api, Resource
from models import db, Restaurante, Usuario
from schemas import restaurant_schema, restaurants_schema 

api = Api()

class RecursoRestaurante(Resource):
    def get(self):
        restaurantes = Restaurante.filter_by(Usuario.usuario_id == Restaurante.restaurante_id)\
            .order_by(Restaurante.fecha_creacion)
        return restaurants_schema.dump(restaurantes)
    
    def post(self):
        nombre = request.json['nombre_restuarante']
        lugar = request.json['lugar']
        direccion = request.json['direccion']
        telefono = request.json['categoria']
        domicilio = request.json['domicilio']
        usuario_id = session['usuario']
        new_restaurant = Restaurante(nombre, lugar, direccion, telefono, domicilio, usuario_id)
        db.session.add(new_restaurant)
        db.commit()
        return "Restaurante {} agregado satisfactoriamente".format(nombre)


api.add_resource(RecursoRestaurante, '/restaurantes')