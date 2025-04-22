from BaseDatos import BaseDatos

class Refaccion:
    def __init__(self, id=None, nombre=None, precio=None):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    @staticmethod
    def get_all():
        """Obtiene todas las refacciones de la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Refacciones")
        rows = cursor.fetchall()
        return [Refaccion(*row) for row in rows]

    def save(self):
        """Guarda una nueva refacción en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO Servicio_Refacciones (nombre, precio) VALUES (%s, %s)",
                (self.nombre, self.precio)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al guardar refacción: {e}")
            return False
    
    @staticmethod
    def get_by_service(id_servicio):
        """Obtiene las refacciones asociadas a un servicio."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        cursor.execute(
            """
            SELECT r.nombre, sr.cantidad
            FROM Servicio_Refacciones sr
            JOIN Refacciones r ON sr.id_refaccion = r.id
            WHERE sr.id_servicio = %s
            """,
            (id_servicio,)
        )
        return cursor.fetchall()