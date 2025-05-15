from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit, QMessageBox, QWidget
from Controlador.ClienteController import ClienteController

class ClienteView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Clientes")
        self.setGeometry(100, 100, 800, 600)

        self.controller = ClienteController()

        # Layout principal
        self.layout = QVBoxLayout()

        # Tabla para mostrar clientes
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Teléfono", "Email", "Dirección"])
        self.layout.addWidget(self.table)

        # Campos de entrada
        self.input_nombre = QLineEdit(self)
        self.input_nombre.setPlaceholderText("Nombre")
        self.layout.addWidget(self.input_nombre)

        self.input_telefono = QLineEdit(self)
        self.input_telefono.setPlaceholderText("Teléfono")
        self.layout.addWidget(self.input_telefono)

        self.input_email = QLineEdit(self)
        self.input_email.setPlaceholderText("Email")
        self.layout.addWidget(self.input_email)

        self.input_direccion = QLineEdit(self)
        self.input_direccion.setPlaceholderText("Dirección")
        self.layout.addWidget(self.input_direccion)

        # Botones
        self.btn_agregar = QPushButton("Agregar Cliente", self)
        self.btn_agregar.clicked.connect(self.add_cliente)
        self.layout.addWidget(self.btn_agregar)
        
        self.btn_actualizar = QPushButton("Actualizar Cliente", self)  # Botón para actualizar
        self.btn_actualizar.clicked.connect(self.update_cliente)
        self.layout.addWidget(self.btn_actualizar)

        self.btn_eliminar = QPushButton("Eliminar Cliente", self)
        self.btn_eliminar.clicked.connect(self.delete_cliente)
        self.layout.addWidget(self.btn_eliminar)

        # Contenedor principal
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Cargar los clientes al iniciar
        self.load_clientes()

    def load_clientes(self):
        """Carga los clientes desde el controlador y los muestra en la tabla."""
        clientes = self.controller.get_all_clientes()
        self.table.setRowCount(len(clientes))
        for row_idx, cliente in enumerate(clientes):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(cliente.id)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(cliente.nombre))
            self.table.setItem(row_idx, 2, QTableWidgetItem(cliente.telefono))
            self.table.setItem(row_idx, 3, QTableWidgetItem(cliente.email))
            self.table.setItem(row_idx, 4, QTableWidgetItem(cliente.direccion))

    def add_cliente(self):
        """Agrega un nuevo cliente."""
        nombre = self.input_nombre.text()
        telefono = self.input_telefono.text()
        email = self.input_email.text()
        direccion = self.input_direccion.text()

        if not nombre or not telefono:
            QMessageBox.warning(self, "Error", "Los campos Nombre y Teléfono son obligatorios.")
            return

        if self.controller.add_cliente(nombre, telefono, email, direccion):
            QMessageBox.information(self, "Éxito", "Cliente agregado correctamente.")
            self.load_clientes()
            self.input_nombre.clear()
            self.input_telefono.clear()
            self.input_email.clear()
            self.input_direccion.clear()
        else:
            QMessageBox.critical(self, "Error", "No se pudo agregar el cliente.")

    def delete_cliente(self):
        """Elimina el cliente seleccionado."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un cliente para eliminar.")
            return

        cliente_id = self.table.item(selected_row, 0).text()
        confirm = QMessageBox.question(
            self,
            "Confirmar Eliminación",
            f"¿Estás seguro de que deseas eliminar el cliente con ID {cliente_id}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            if self.controller.delete_cliente(cliente_id):
                QMessageBox.information(self, "Éxito", "Cliente eliminado correctamente.")
                self.load_clientes()
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar el cliente.")
                
    def update_cliente(self):
        """Actualiza el cliente seleccionado."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un cliente para actualizar.")
            return

        cliente_id = self.table.item(selected_row, 0).text()
        nombre = self.input_nombre.text()
        telefono = self.input_telefono.text()
        email = self.input_email.text()
        direccion = self.input_direccion.text()

        if not nombre or not telefono:
            QMessageBox.warning(self, "Error", "Los campos Nombre y Teléfono son obligatorios.")
            return

        if self.controller.update_cliente(cliente_id, nombre, telefono, email, direccion):
            QMessageBox.information(self, "Éxito", "Cliente actualizado correctamente.")
            self.load_clientes()
            self.input_nombre.clear()
            self.input_telefono.clear()
            self.input_email.clear()
            self.input_direccion.clear()
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar el cliente.")
