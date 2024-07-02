""" Queries del servicio 1 """

from src.scripts.connection import Connection
import datetime


class Query(Connection):
    """> The Query class is a subclass of the Connection class"""

    # Metodos GET
    def buscar_vuelo(self, limit, offset):

        query = """
            SELECT * FROM t_viaje ORDER BY id_viaje ASC OFFSET %s LIMIT %s
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [int(offset), int(limit)])

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_viajes = [
                    {
                        columnas[index]: self._convert_value(item)
                        for index, item in enumerate(tupla)
                    }
                    for tupla in response
                ]

                print(objeto_viajes)

                return objeto_viajes

    # funcion para convertir el tipo de dato Date a un string para pasarlo a Json
    def _convert_value(self, value):
        if isinstance(value, (datetime.date, datetime.datetime)):
            return value.isoformat()
        elif isinstance(value, datetime.time):
            return value.strftime("%H:%M:%S")
        return value

    def buscar_viaje_por_origen(self):

        query = """
            SELECT DISTINCT tv.origen FROM t_viaje tv ORDER BY tv.origen ASC
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query)

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_viajes = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_viajes)

                return objeto_viajes

    def buscar_viaje_por_destino(self, origen: str):

        primer_nombre = origen.split()[0]

        query = """
            SELECT DISTINCT tv.destino FROM t_viaje tv WHERE tv.origen = %s ORDER BY tv.destino ASC
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query, [primer_nombre]).decode())
                cursor.execute(query, [primer_nombre])

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_viajes = [
                    {columnas[index]: item for index, item in enumerate(tupla)}
                    for tupla in response
                ]

                print(objeto_viajes)

                return objeto_viajes
            
    def mostrar_rutas_filtradas(self, origen: str, destino: str, orden=None):
        # Construir la parte de la cláusula ORDER BY dependiendo del parámetro de orden
        if orden in ['precio', 'distancia', 'duracion']:
            order_clause = f"ORDER BY {orden} ASC"
        else:
            order_clause = ""

        query = f"""
            SELECT * FROM t_viaje 
            WHERE origen = %s AND destino = %s
            {order_clause}
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query, [origen, destino]).decode())
                cursor.execute(query, [origen, destino])

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_rutas = [
                    {
                        columnas[index]: self._convert_value(item)
                        for index, item in enumerate(tupla)
                    }
                    for tupla in response
                ]

                print(objeto_rutas)

                return objeto_rutas

    def buscar_reserva(self):

        query = """
            SELECT tr.id_reserva, tr.fecha, tv.id_viaje, tv.origen, tv.destino, tv.distancia, tv.duracion, tv.precio
            FROM t_reserva tr
	        INNER JOIN t_viaje tv ON tv.id_viaje = tr.id_viaje
	        ORDER BY id_reserva ASC
        """

        # contextos de python
        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query).decode())
                cursor.execute(query)

                response = cursor.fetchall()

                print(response)
                print(cursor.description)

                columnas = [columna.name for columna in cursor.description or []]

                # objeto_pk = []
                # for tupla in response:
                #     obj = {}
                #     for index, item in enumerate(tupla):
                #         obj[columnas[index]] = item
                #     objeto_pk.append(obj)
                objeto_viajes = [
                    {
                        columnas[index]: self._convert_value(item)
                        for index, item in enumerate(tupla)
                    }
                    for tupla in response
                ]

                print(objeto_viajes)

                return objeto_viajes

    # Metodo POST
    def agregar_reserva(self, id_reserva: int, id_viaje: str, fecha: str):
        query = """
            INSERT INTO t_reserva
            (id_reserva, id_viaje, fecha)
            VALUES(%s, %s, %s);
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                print(cursor.mogrify(query, [id_reserva, id_viaje, fecha]).decode())
                cursor.execute(query, [id_reserva, id_viaje, fecha])

    # Metodo PUT
    def editar_reserva(self, id_reserva: str, id_viaje: str, fecha: str):
        query = """
            UPDATE t_reserva
            SET id_viaje=%s, fecha=%s
            WHERE id_reserva=%s;
        """

        with self._open_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(query, [id_viaje, fecha, id_reserva])
