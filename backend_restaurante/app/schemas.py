from flask_marshmallow import Marshmallow

ma = Marshmallow()

class EsquemaUsuario(ma.Schema):
    class Meta:
        campos = ('usuario_id', 'email', 'contraseña')

class EsquemaRestaurante(ma.Schema):
    class Meta:
        campos = ('restaurante_id','nombre_restaurante','lugar',
        'direccion','telefono','categoria','domicilio','fecha_creacion',
        'usuario_id')