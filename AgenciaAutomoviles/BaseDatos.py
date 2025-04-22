import mysql.connector

class BaseDatos:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BaseDatos, cls).__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host="localhost",
                user="root",  
                password="1234",  
                database="agenciaautomoviles" 
            )
        return cls._instance

    def get_connection(self):
        return self.connection