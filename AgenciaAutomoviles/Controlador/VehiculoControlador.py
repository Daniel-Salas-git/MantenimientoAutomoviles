from Modelo.Vehiculo import Vehicle
from Modelo.Servicio import Service

class VehicleController:
    def get_all_vehicles(self):
        """Obtiene todos los vehículos utilizando el modelo."""
        return Vehicle.get_all()

    def add_vehicle(self, marca, modelo, año, placa, cliente, telefono):
        """Agrega un nuevo vehículo utilizando el modelo."""
        vehicle = Vehicle(marca=marca, modelo=modelo, año=año, placa=placa, cliente=cliente, telefono=telefono)
        return vehicle.save()

    def update_vehicle(self, vehicle_id, marca, modelo, año, placa, cliente, telefono):
        """Actualiza un vehículo existente utilizando el modelo."""
        vehicle = Vehicle(id=vehicle_id, marca=marca, modelo=modelo, año=año, placa=placa, cliente=cliente, telefono=telefono)
        return vehicle.update()

    def delete_vehiculo(self, vehiculo_id):
        """Elimina un vehículo por su ID."""
        vehicle = Vehicle(id=vehiculo_id)
        return vehicle.delete(vehiculo_id)
    
    def get_services_by_vehicle(self, id_vehiculo):
        """Obtiene los servicios asociados a un vehículo específico."""
        return Service.get_by_vehicle(id_vehiculo)  # Llama al método del modelo