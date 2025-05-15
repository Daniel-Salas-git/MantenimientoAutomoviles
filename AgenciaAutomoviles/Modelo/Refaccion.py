from Modelo.BaseDatos import BaseDatos

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
   
    def add_refaccion_pieza(self, nombre, precio):
        """Agrega una nueva refacción."""
        try:
            db = BaseDatos().get_connection()
            cursor = db.cursor()
            cursor.execute(
                "INSERT INTO Refacciones (nombre, precio) VALUES (%s, %s)",
                (nombre, precio)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al guardar refacción: {e}")
            return False
        
    def update(self):
        """Actualiza una refacción existente en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            print(f"Actualizando refacción con ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}")  # Depuración
            cursor.execute(
                "UPDATE Refacciones SET nombre = %s, precio = %s WHERE id = %s",
                (self.nombre, self.precio, self.id)
            )
            db.commit()
            return cursor.rowcount > 0  # Retorna True si se afectó al menos una fila
        except Exception as e:
            print(f"Error al actualizar refacción: {e}")
            return False
        
    def get_id_by_name(nombre):
        """Obtiene el ID de una refacción por su nombre."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute("SELECT id FROM Refacciones WHERE nombre = %s", (nombre,))
            result = cursor.fetchone()
            if result:
                return result[0]  # Retorna el ID
            return None
        except Exception as e:
            print(f"Error al obtener el ID de la refacción: {e}")
            return None
        
    def delete(self):
        """Elimina una refacción de la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM Refacciones WHERE id = %s", (self.id,))
            db.commit()
            return cursor.rowcount > 0  # Retorna True si se afectó al menos una fila
        except Exception as e:
            print(f"Error al eliminar refacción: {e}")
            return False