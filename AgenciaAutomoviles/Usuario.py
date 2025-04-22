from BaseDatos import BaseDatos

class User:
    def __init__(self, id=None, nombre=None, usuario=None, contraseña=None, rol=None):
        self.id = id
        self.nombre = nombre
        self.usuario = usuario
        self.contraseña = contraseña
        self.rol = rol

    @staticmethod
    def get_all():
        """Obtiene todos los usuarios de la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Usuarios")
        rows = cursor.fetchall()
        return [User(*row) for row in rows]

    def save(self):
        """Guarda un nuevo usuario en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO Usuarios (nombre, usuario, contraseña, rol) VALUES (%s, %s, %s, %s)",
                (self.nombre, self.usuario, self.contraseña, self.rol)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al guardar usuario: {e}")
            return False

    def update(self):
        """Actualiza un usuario existente en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                "UPDATE Usuarios SET nombre = %s, usuario = %s, contraseña = %s, rol = %s WHERE id = %s",
                (self.nombre, self.usuario, self.contraseña, self.rol, self.id)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar usuario: {e}")
            return False

    @staticmethod
    def delete(user_id):
        """Elimina un usuario de la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM Usuarios WHERE id = %s", (user_id,))
            db.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            return False