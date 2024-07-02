""" entry point for flask app """

from src.settings import application
from src.scripts.routes import base_blueprint
from src.scripts.routes import servicio_viajes

application.register_blueprint(base_blueprint)
application.register_blueprint(servicio_viajes)


if __name__ == '__main__':
    application.run()
