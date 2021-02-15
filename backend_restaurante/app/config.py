class Config(object):
    SECRET_KEY = 'tecnologias_emergentes'

class DevelopmentConfig(Config):
    DEBUG = True
    #Conexión base de datos MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/db_restaurante'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

