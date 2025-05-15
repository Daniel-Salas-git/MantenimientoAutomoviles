from Modelo.Refaccion import Refaccion

class RefaccionController:
    def get_all_refacciones(self):
        """Obtiene todas las refacciones desde el modelo."""
        return Refaccion.get_all()

    def add_refaccion(self, nombre, precio):
        """Agrega una nueva refacción."""
        refaccion = Refaccion(nombre=nombre, precio=precio)
        return refaccion.save()

    #def update_refaccion(self, refaccion_id, nombre, precio):
     #   """Actualiza una refacción existente."""
      #  refaccion = Refaccion(id=refaccion_id, nombre=nombre, precio=precio)
       # return refaccion.update()

    def delete_refaccion(self, refaccion_id):
        """Elimina una refacción por su ID."""
        refaccion = Refaccion(id=refaccion_id)
        return refaccion.delete()
    
    def update_refaccion_pieza(self, refaccion_id, nombre, precio):
        """Actualiza una refacción existente."""
        print(f"ID recibido en el controlador: {refaccion_id}")  # Depuración
        refaccion = Refaccion(id=refaccion_id, nombre=nombre, precio=precio)
        return refaccion.update()
    
    def add_refaccion_pieza(self, nombre, precio):
        """Agrega una nueva refacción."""
        refaccion_pieza = Refaccion(nombre=nombre, precio=precio)
        return refaccion_pieza.add_refaccion_pieza(nombre, precio)
    
    def get_refaccion_id_by_name(self, nombre):
        """Obtiene el ID de una refacción por su nombre."""
        return Refaccion.get_id_by_name(nombre)