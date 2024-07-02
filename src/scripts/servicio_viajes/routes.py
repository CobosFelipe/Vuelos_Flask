""" rutas del servicio 1 """

from flask import Blueprint

from . import controllers


servicio_viajes = Blueprint(
    "servicio_viajes",
    __name__,
    url_prefix='/vuelos',
)

servicio_viajes.add_url_rule(
    "/all",
    view_func=controllers.get_vuelos,
    methods=["GET"]
)

servicio_viajes.add_url_rule(
    "/resultados",
    view_func=controllers.get_vuelos_por_origen,
    methods=["GET"]
)

servicio_viajes.add_url_rule(
    "/resultados/<origen>",
    view_func=controllers.get_vuelos_por_destino,
    methods=["GET"]
)

servicio_viajes.add_url_rule(
    "/reservas",
    view_func=controllers.get_reservas,
    methods=["GET"]
)

servicio_viajes.add_url_rule(
    "/ruta/<origen>/<destino>",
    view_func=controllers.get_rutas,
    methods=["GET"]
)

servicio_viajes.add_url_rule(
    "/add/reserva",
    view_func=controllers.agregar_reservas,
    methods=["POST"]
)

servicio_viajes.add_url_rule(
    "/put/<id_reserva>",
    view_func=controllers.editar_reservas,
    methods=["PUT"]
)
