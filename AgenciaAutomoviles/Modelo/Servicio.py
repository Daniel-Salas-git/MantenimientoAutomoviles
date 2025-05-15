from Modelo.BaseDatos import BaseDatos

class Service:
    def __init__(self, folio=None, id_vehiculo=None, estatus=None, fecha_servicio=None, proximo_servicio=None, responsable=None, entregado_por=None, diagnostico=None):
        self.folio = folio
        self.id_vehiculo = id_vehiculo
        self.estatus = estatus
        self.fecha_servicio = fecha_servicio
        self.proximo_servicio = proximo_servicio
        self.responsable = responsable
        self.entregado_por = entregado_por
        self.diagnostico = diagnostico

    @staticmethod
    def get_all():
        """Obtiene todos los servicios de la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Servicios")
        rows = cursor.fetchall()
        return [Service(*row) for row in rows]

    def save(self):
        """Guarda un nuevo servicio en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO Servicios (id_vehiculo, estatus, fecha_servicio, proximo_servicio, responsable, entregado_por, diagnostico) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (self.id_vehiculo, self.estatus, self.fecha_servicio, self.proximo_servicio, self.responsable, self.entregado_por, self.diagnostico)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al guardar servicio: {e}")
            return False

    def update(self):
        """Actualiza un servicio existente en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                "UPDATE Servicios SET id_vehiculo = %s, estatus = %s, fecha_servicio = %s, proximo_servicio = %s, responsable = %s, entregado_por = %s, diagnostico = %s WHERE folio = %s",
                (self.id_vehiculo, self.estatus, self.fecha_servicio, self.proximo_servicio, self.responsable,self.entregado_por, self.diagnostico, self.folio)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar servicio: {e}")
            return False

    @staticmethod
    def delete(folio):
        """Elimina un servicio de la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM Servicios WHERE folio = %s", (folio,))
            db.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar servicio: {e}")
            return False
        
    @staticmethod
    def get_by_vehicle(id_vehiculo):
        """Obtiene los servicios asociados a un vehículo específico."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                """
                SELECT folio, estatus, fecha_servicio, proximo_servicio, diagnostico, responsable, entregado_por
                FROM Servicios
                WHERE id_vehiculo = %s
                """,
                (id_vehiculo,)
            )
            return cursor.fetchall()  # Retorna una lista de tuplas con los datos
        except Exception as e:
            print(f"Error al obtener servicios: {e}")
            return []
        
