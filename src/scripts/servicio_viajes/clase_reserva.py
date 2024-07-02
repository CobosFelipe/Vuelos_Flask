""" Ejemplo clase ejercicio """

class NotFoundArgs(Exception):
    """ Excepcion customizada para informar la falta de parametros """

class Clase_t_reserva:
    """ Clase de ejemplo """
    def __init__(self) -> None:
        self.id_reserva = None
        self.id_viaje = None
        self.fecha = None

    def validar(self, args):
        """ funcion para validar las entradas del controlador """

        if not "id_reserva" in args:
            raise NotFoundArgs("No se ha encontrado el id de la reserva en las entradas")
        if not "id_viaje" in args:
            raise NotFoundArgs("No se ha encontrado el id del viaje en las entradas")
        if not "fecha" in args:
            raise NotFoundArgs("No se ha encontrado la fecha del viaje en las entradas")

        self.id_reserva = args["id_reserva"]
        self.id_viaje = args["id_viaje"]
        self.fecha = args["fecha"]
