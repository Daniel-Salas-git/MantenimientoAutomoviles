from Vehiculo import Vehicle

class VehicleController:
    def get_all_vehicles(self):
        """Obtiene todos los vehículos utilizando el modelo."""
        return Vehicle.get_all()

    def add_vehicle(self, marca, modelo, año, placa):
        """Agrega un nuevo vehículo utilizando el modelo."""
        vehicle = Vehicle(marca=marca, modelo=modelo, año=año, placa=placa)
        return vehicle.save()

    def update_vehicle(self, vehicle_id, marca, modelo, año, placa):
        """Actualiza un vehículo existente utilizando el modelo."""
        vehicle = Vehicle(id=vehicle_id, marca=marca, modelo=modelo, año=año, placa=placa)
        return vehicle.update()

    def delete_vehiculo(self, vehiculo_id):
        """Elimina un vehículo por su ID."""
        vehicle = Vehicle(id=vehiculo_id)
        return vehicle.delete()