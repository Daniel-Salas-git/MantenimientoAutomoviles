from Refaccion import Refaccion

class RefaccionController:
    def get_all_refacciones(self):
        """Obtiene todas las refacciones desde el modelo."""
        return Refaccion.get_all()

    def add_refaccion(self, nombre, precio):
        """Agrega una nueva refacción."""
        refaccion = Refaccion(nombre=nombre, precio=precio)
        return refaccion.save()

    def update_refaccion(self, refaccion_id, nombre, precio):
        """Actualiza una refacción existente."""
        refaccion = Refaccion(id=refaccion_id, nombre=nombre, precio=precio)
        return refaccion.update()

    def delete_refaccion(self, refaccion_id):
        """Elimina una refacción por su ID."""
        refaccion = Refaccion(id=refaccion_id)
        return refaccion.delete()