from BaseDatos import BaseDatos

class ServicioRefaccion:
    def __init__(self, id_servicio=None, id_refaccion=None, cantidad=None):
        self.id_servicio = id_servicio
        self.id_refaccion = id_refaccion
        self.cantidad = cantidad

    def save(self):
        """Guarda la asociación de una refacción a un servicio en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO Servicio_Refacciones (id_servicio, id_refaccion, cantidad) VALUES (%s, %s, %s)",
                (self.id_servicio, self.id_refaccion, self.cantidad)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al asociar refacción: {e}")
            return False

    @staticmethod
    def get_by_service(id_servicio):
        """Obtiene las refacciones asociadas a un servicio."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT sr.id_servicio,r.nombre, sr.cantidad, r.precio
            FROM Servicio_Refacciones sr
            JOIN Refacciones r ON sr.id_refaccion = r.id
            WHERE sr.id_servicio = %s
            """,
            (id_servicio,)
        )
        return cursor.fetchall()

    @staticmethod
    def get_all():
        """Obtiene todas las asociaciones de servicios y refacciones."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT sr.id_servicio, r.nombre, sr.cantidad
            FROM Servicio_Refacciones sr
            JOIN Refacciones r ON sr.id_refaccion = r.id
            """
        )
        return cursor.fetchall()

    @staticmethod
    def delete_by_service_and_refaccion(id_servicio, nombre_refaccion):
        """Elimina una refacción asociada a un servicio."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                """
                DELETE sr
                FROM Servicio_Refacciones sr
                JOIN Refacciones r ON sr.id_refaccion = r.id
                WHERE sr.id_servicio = %s AND r.nombre = %s
                """,
                (id_servicio, nombre_refaccion)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar la refacción: {e}")
            return False
        