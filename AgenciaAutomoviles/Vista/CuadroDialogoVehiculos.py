from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QDialog, QLabel, QComboBox, QMessageBox
from Controlador.ClienteController import ClienteController
from Controlador.VehiculoControlador import VehicleController

class VehiculoDialog(QDialog):
    def __init__(self, marca="", modelo="", anio="",placa="", cliente="", telefono=""):
        super().__init__()
        self.setWindowTitle("Vehículo")
        self.setGeometry(100, 100, 400, 200)

        # Instancia del controlador de clientes
        self.cliente_controller = ClienteController()
        # Layout principal
        self.layout = QVBoxLayout()

        # Campos de entrada
        self.label_marca = QLabel("Marca:")
        self.input_marca = QLineEdit(self)
        self.layout.addWidget(self.label_marca)
        self.layout.addWidget(self.input_marca)

        self.label_modelo = QLabel("Modelo:")
        self.input_modelo = QLineEdit(self)
        self.layout.addWidget(self.label_modelo)
        self.layout.addWidget(self.input_modelo)

        self.label_anio = QLabel("Año:")
        self.input_anio = QLineEdit(self)
        self.layout.addWidget(self.label_anio)
        self.layout.addWidget(self.input_anio)
        
        self.label_placa = QLabel("Placa:")
        self.input_placa = QLineEdit(self)
        self.layout.addWidget(self.label_placa)
        self.layout.addWidget(self.input_placa)
        

        # ComboBox para seleccionar cliente
        self.label_cliente = QLabel("Cliente:")
        self.layout.addWidget(self.label_cliente)  # Agregar el QLabel antes del QComboBox
        self.combo_cliente = QComboBox(self)
        self.combo_cliente.setPlaceholderText("Seleccionar Cliente")
        self.layout.addWidget(self.combo_cliente)

        # ComboBox para seleccionar teléfono
        self.label_telefono = QLabel("Telefono:")
        self.layout.addWidget(self.label_telefono)  # Agregar el QLabel antes del QComboBox
        self.combo_telefono = QComboBox(self)
        self.combo_telefono.setPlaceholderText("Seleccionar Teléfono")
        self.layout.addWidget(self.combo_telefono)

        # Botones
        self.btn_save = QPushButton("Guardar", self)
        self.btn_save.clicked.connect(self.accept)
        self.layout.addWidget(self.btn_save)

        self.setLayout(self.layout)
        
        self.cargar_clientes()


    def get_data(self):
        """Obtiene los datos ingresados por el usuario."""
        return self.input_marca.text(), self.input_modelo.text(), self.input_anio.text(), self.input_placa.text(), self.combo_cliente.currentText(), self.combo_telefono.currentText()
    

    def cargar_clientes(self):
        """Carga los clientes y sus teléfonos en los ComboBox."""
        clientes = self.cliente_controller.get_clientes_con_telefonos()
        print(f"Clientes cargados en los ComboBox: {clientes}")  # Depuración
        self.combo_cliente.clear()
        self.combo_telefono.clear()

        if not clientes:
            print("No se encontraron clientes para cargar.")  # Depuración
            return

        for cliente_id, cliente_info in clientes:
            nombre, telefono = cliente_info.split(" - ")  # Separar nombre y teléfono
            self.combo_cliente.addItem(nombre, cliente_id)  # Solo el nombre en el combo_cliente
            self.combo_telefono.addItem(telefono, f"{nombre}")  # Solo el teléfono en el combo_telefono
    
    def guardar_vehiculo(self):
        """Obtiene los datos del formulario y los guarda usando el controlador."""
        marca = self.input_marca.text()
        modelo = self.input_modelo.text()
        anio = self.input_anio.text()
        placa = self.input_placa.text()
        cliente = self.combo_cliente.currentText()
        telefono = self.combo_telefono.currentText()

        if not marca or not modelo or not anio or not placa or not cliente or not telefono:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        if self.vehiculo_controller.guardar_vehiculo(marca, modelo, anio, placa, cliente, telefono):
            QMessageBox.information(self, "Éxito", "Vehículo guardado correctamente.")
            self.accept()
        else:
            QMessageBox.critical(self, "Error", "No se pudo guardar el vehículo.")