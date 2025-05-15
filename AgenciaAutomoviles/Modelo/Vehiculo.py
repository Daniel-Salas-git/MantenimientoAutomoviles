from Modelo.BaseDatos import BaseDatos

class Vehicle:
    def __init__(self, id=None, marca=None, modelo=None, año=None, placa=None, cliente=None, telefono=None):
        self.id = id
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.placa = placa
        self.cliente = cliente
        self.telefono = telefono

    @staticmethod
    def get_all():
        """Obtiene todos los vehículos de la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM Vehiculos")
        rows = cursor.fetchall()
        return [Vehicle(id=row[0], marca=row[1], modelo=row[2], año=row[3], placa=row[4], cliente=row[5], telefono=row[6]) for row in rows]

    def save(self):
        """Guarda un nuevo vehículo en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                "INSERT INTO Vehiculos (marca, modelo, año, placa, cliente, telefono) VALUES (%s, %s, %s, %s, %s, %s)",
                (self.marca, self.modelo, self.año, self.placa, self.cliente, self.telefono)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al guardar vehículo: {e}")
            return False

    def update(self):
        """Actualiza un vehículo existente en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute(
                "UPDATE Vehiculos SET marca = %s, modelo = %s, año = %s, placa = %s, cliente = %s, telefono = %s WHERE id = %s",
                (self.marca, self.modelo, self.año, self.placa, self.cliente, self.telefono, self.id)
            )
            db.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar vehículo: {e}")
            return False

    @staticmethod
    def delete(vehicle_id):
        """Elimina un vehículo de la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute("DELETE FROM Vehiculos WHERE id = %s", (vehicle_id,))
            db.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar vehículo: {e}")
            return False
        
    def get_all_id_vehicles():
        """Obtiene todos los vehiculos registrados en la base de datos."""
        db = BaseDatos().get_connection()
        cursor = db.cursor()
        try:
            cursor.execute("SELECT id FROM Vehiculo")  
            return [row[0] for row in cursor.fetchall()]  # Retorna una lista con los nombres de los usuarios
        except Exception as e:
            print(f"Error al obtener vehiculos: {e}")
            return []