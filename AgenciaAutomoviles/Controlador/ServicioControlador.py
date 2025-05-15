from Modelo.Servicio import Service
from Modelo.BaseDatos import BaseDatos
from Modelo.ServicioRefaccion import ServicioRefaccion
from Modelo.Usuario import User  # Importar el modelo User
from Modelo.Vehiculo import Vehicle  # Importar el modelo Vehicle
from Modelo.Cliente import Cliente  # Importar el modelo Cliente



class ServiceController:
    def get_all_services(self):
        """Obtiene todos los servicios utilizando el modelo."""
        return Service.get_all()

    def add_service(self, id_vehiculo, estatus, fecha_servicio, proximo_servicio, responsable, entregado_por, diagnostico):
        """Agrega un nuevo servicio utilizando el modelo."""
        service = Service(id_vehiculo=id_vehiculo, estatus=estatus, fecha_servicio=fecha_servicio, proximo_servicio=proximo_servicio, responsable=responsable, entregado_por=entregado_por, diagnostico=diagnostico)
        return service.save()

    def update_service(self, folio, id_vehiculo, estatus, fecha_servicio, proximo_servicio, responsable, entregado_por, diagnostico):
        """Actualiza un servicio existente utilizando el modelo."""
        service = Service(folio=folio, id_vehiculo=id_vehiculo, estatus=estatus, fecha_servicio=fecha_servicio, proximo_servicio=proximo_servicio, responsable=responsable, entregado_por=entregado_por, diagnostico=diagnostico)
        return service.update()

    def delete_service(self, folio):
        """Elimina un servicio utilizando el modelo."""
        return Service.delete(folio)
    
    def get_status_counts(self, fecha=None):
        """Obtiene el conteo de servicios por estatus, opcionalmente filtrados por fecha."""
        services = Service.get_all()
        status_counts = {"En espera": 0, "En proceso": 0, "Finalizado": 0}

        for service in services:
            if fecha:
                if str(service.fecha_servicio) == fecha:
                    status_counts[service.estatus] += 1
            else:
                status_counts[service.estatus] += 1

        return status_counts
    def get_all_service_refacciones(self):
        """Obtiene todas las refacciones asociadas a los servicios."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        cursor.execute("""
            SELECT sr.id_servicio, r.nombre, sr.cantidad
            FROM Servicio_Refacciones sr
            JOIN Refacciones r ON sr.id_refaccion = r.id
        """)
        return cursor.fetchall()
    
    def add_refaccion_to_service(self, id_servicio, id_refaccion, cantidad):
        """Asocia una refacción a un servicio."""
        servicio_refaccion = ServicioRefaccion(id_servicio=id_servicio, id_refaccion=id_refaccion, cantidad=cantidad)
        return servicio_refaccion.save()
    
    def get_refacciones_by_service(self, id_servicio):
        """Obtiene las refacciones asociadas a un servicio especifico."""
        return ServicioRefaccion.get_by_service(id_servicio)
    
    def delete_refaccion_from_service(self, id_servicio, nombre_refaccion):
        """Elimina una refacción asociada a un servicio."""
        return ServicioRefaccion.delete_by_service_and_refaccion(id_servicio, nombre_refaccion)
    
    def get_all_users(self):
        """Obtiene todos los usuarios desde el modelo User."""
        return User.get_all()  # Llama al método estático del modelo User
    
    def get_all_id_vehicles(self):
        """Obtiene todos los usuarios desde el modelo Vehicle."""
        return Vehicle.get_all()  # Llama al método estático del modelo Vehicle
    
    def get_all_clientes(self):
        """Obtiene todos los clientes registrados."""
        return Cliente.get_all()  # Llama al método del modelo para obtener los clientes