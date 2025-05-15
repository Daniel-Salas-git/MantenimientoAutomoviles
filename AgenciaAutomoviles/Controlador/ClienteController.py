from Modelo.Cliente import Cliente

class ClienteController:
    def get_all_clientes(self):
        """Obtiene todos los clientes desde el modelo."""
        return Cliente.get_all()

    def add_cliente(self, nombre, telefono, email, direccion):
        """Agrega un nuevo cliente."""
        cliente = Cliente(nombre=nombre, telefono=telefono, email=email, direccion=direccion)
        return cliente.save()

    def update_cliente(self, cliente_id, nombre, telefono, email, direccion):
        """Actualiza un cliente existente."""
        cliente = Cliente(id=cliente_id, nombre=nombre, telefono=telefono, email=email, direccion=direccion)
        return cliente.update()

    def delete_cliente(self, cliente_id):
        """Elimina un cliente por su ID."""
        cliente = Cliente(id=cliente_id)
        return cliente.delete()
    
    def get_clientes_con_telefonos(self):
        """Obtiene una lista de clientes con sus teléfonos."""
        clientes = Cliente.get_all()
        print(f"Clientes obtenidos desde el modelo: {clientes}")  # Depuración
        return [(cliente.id, f"{cliente.nombre} - {cliente.telefono}") for cliente in clientes]