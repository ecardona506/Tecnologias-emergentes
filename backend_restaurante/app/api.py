from flask_restful import Api, Resource
from models import db, Restaurante, Usuario
from schemas import restaurant_schema, restaurants_schema 

api = Api()

class RecursoRestaurante(Resource):
    def get(self):
        restaurantes = Restaurante.filter_by(Usuario.usuario_id == Restaurante.restaurante_id)\
            .order_by(Restaurante.fecha_creacion)
        return restaurants_schema.dump(restaurantes)

api.add_resource(RecursoRestaurante, '/restaurantes')