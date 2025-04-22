from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QMessageBox
from RefaccionControler import RefaccionController

class RefaccionSelectorDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Seleccionar Refacción")
        self.setGeometry(100, 100, 600, 400)

        self.controller = RefaccionController()

        # Layout principal
        self.layout = QVBoxLayout()

        # Tabla para mostrar refacciones
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Precio"])
        self.layout.addWidget(self.table)

        # Campo para ingresar la cantidad
        self.input_cantidad = QLineEdit(self)
        self.input_cantidad.setPlaceholderText("Cantidad")
        self.layout.addWidget(self.input_cantidad)

        # Botón para confirmar la selección
        self.btn_select = QPushButton("Seleccionar", self)
        self.btn_select.clicked.connect(self.select_refaccion)
        self.layout.addWidget(self.btn_select)

        # Cargar las refacciones disponibles
        self.load_refacciones()

        # Configurar el layout
        self.setLayout(self.layout)

        # Variables para almacenar la selección
        self.selected_refaccion = None
        self.selected_cantidad = None

    def load_refacciones(self):
        """Carga las refacciones desde el controlador y las muestra en la tabla."""
        refacciones = self.controller.get_all_refacciones()
        self.table.setRowCount(len(refacciones))
        for row_idx, refaccion in enumerate(refacciones):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(refaccion.id)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(refaccion.nombre))
            self.table.setItem(row_idx, 2, QTableWidgetItem(f"{refaccion.precio:.2f}"))

    def select_refaccion(self):
        """Selecciona una refacción y la cantidad."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona una refacción.")
            return

        cantidad = self.input_cantidad.text()
        if not cantidad.isdigit() or int(cantidad) <= 0:
            QMessageBox.warning(self, "Error", "Ingresa una cantidad válida.")
            return

        self.selected_refaccion = self.table.item(selected_row, 0).text()
        self.selected_cantidad = int(cantidad)
        self.accept()
        
        