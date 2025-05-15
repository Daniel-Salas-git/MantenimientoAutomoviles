from Modelo.BaseDatos import BaseDatos

class Cliente:
    def __init__(self, id=None, nombre=None, telefono=None, email=None, direccion=None):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion

    @staticmethod
    def get_all():
        """Obtiene todos los clientes."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute("SELECT id, nombre, telefono, email, direccion FROM Clientes")
            rows = cursor.fetchall()
            return [Cliente(id=row[0], nombre=row[1], telefono=row[2], email=row[3], direccion=row[4]) for row in rows]
        except Exception as e:
            print(f"Error al obtener clientes: {e}")
            return []

    def save(self):
        """Guarda un nuevo cliente en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO Clientes (nombre, telefono, email, direccion) VALUES (%s, %s, %s, %s)",
                (self.nombre, self.telefono, self.email, self.direccion)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al guardar cliente: {e}")
            return False

    def update(self):
        """Actualiza un cliente existente en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                "UPDATE Clientes SET nombre = %s, telefono = %s, email = %s, direccion = %s WHERE id = %s",
                (self.nombre, self.telefono, self.email, self.direccion, self.id)
            )
            db.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False

    def delete(self):
        """Elimina un cliente de la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM Clientes WHERE id = %s", (self.id,))
            db.commit()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Error al eliminar cliente: {e}")
            return False