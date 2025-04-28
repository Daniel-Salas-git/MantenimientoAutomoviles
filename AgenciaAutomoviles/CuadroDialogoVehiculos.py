from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QLineEdit, QDialog, QLabel


class VehiculoDialog(QDialog):
    def __init__(self, marca="", modelo="", anio="",placa="", cliente="", telefono=""):
        super().__init__()
        self.setWindowTitle("Vehículo")
        self.setGeometry(100, 100, 400, 200)

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
        
        self.label_cliente = QLabel("Cliente:")
        self.input_cliente = QLineEdit(self)
        self.layout.addWidget(self.label_cliente)
        self.layout.addWidget(self.input_cliente)

        self.label_telefono = QLabel("Teléfono:")
        self.input_telefono = QLineEdit(self)
        self.layout.addWidget(self.label_telefono)
        self.layout.addWidget(self.input_telefono)

        # Botones
        self.btn_save = QPushButton("Guardar", self)
        self.btn_save.clicked.connect(self.accept)
        self.layout.addWidget(self.btn_save)

        self.setLayout(self.layout)

    def get_data(self):
        """Obtiene los datos ingresados por el usuario."""
        return self.input_marca.text(), self.input_modelo.text(), self.input_anio.text(), self.input_placa.text(), self.input_cliente.text(), self.input_telefono.text()