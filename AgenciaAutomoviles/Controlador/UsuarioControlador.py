from Modelo.Usuario import User

class UserController:
    def get_all_users(self):
        """Obtiene todos los usuarios utilizando el modelo."""
        return User.get_all()

    def add_user(self, nombre, usuario, contraseña, rol):
        """Agrega un nuevo usuario utilizando el modelo."""
        user = User(nombre=nombre, usuario=usuario, contraseña=contraseña, rol=rol)
        return user.save()

    def update_user(self, user_id, nombre, usuario, contraseña, rol):
        """Actualiza un usuario existente utilizando el modelo."""
        user = User(id=user_id, nombre=nombre, usuario=usuario, contraseña=contraseña, rol=rol)
        return user.update()

    def delete_user(self, user_id):
        """Elimina un usuario utilizando el modelo."""
        return User.delete(user_id)