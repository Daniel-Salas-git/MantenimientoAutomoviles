from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton, QMessageBox
from Controlador.RefaccionControler import RefaccionController

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
        
           # Campos de entrada
        self.input_nombre = QLineEdit(self)
        self.input_nombre.setPlaceholderText("Nombre de la refacción")
        self.layout.addWidget(self.input_nombre)

        self.input_precio = QLineEdit(self)
        self.input_precio.setPlaceholderText("Precio de la refacción")
        self.layout.addWidget(self.input_precio)

        # Botones
        self.btn_agregar = QPushButton("Agregar Refacción", self)
        self.btn_agregar.clicked.connect(self.add_refaccion)
        self.layout.addWidget(self.btn_agregar)

        self.btn_actualizar = QPushButton("Actualizar Refacción", self)
        self.btn_actualizar.clicked.connect(self.update_refaccion)
        self.layout.addWidget(self.btn_actualizar)

        self.btn_eliminar = QPushButton("Eliminar Refacción", self)
        self.btn_eliminar.clicked.connect(self.delete_refaccion)
        self.layout.addWidget(self.btn_eliminar)

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
            
    def add_refaccion(self):
        """Agrega una nueva refacción."""
        refaccion = self.input_nombre.text()
        precio = self.input_precio.text()

        if not refaccion or not precio:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            precio = float(precio)
        except ValueError:
            QMessageBox.warning(self, "Error", "El precio debe ser un número válido.")
            return

        if self.controller.add_refaccion_pieza(refaccion, precio):
            QMessageBox.information(self, "Éxito", "Refacción agregada correctamente.")
            self.load_refacciones()
            self.input_nombre.clear()
            self.input_precio.clear()
        else:
            QMessageBox.critical(self, "Error", "No se pudo agregar la refacción.")

    def update_refaccion(self):
        """Actualiza la refacción seleccionada."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona una refacción para actualizar.")
            return

        refaccion = self.input_nombre.text()
        precio = self.input_precio.text()

        if not refaccion or not precio:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        try:
            precio = float(precio)
        except ValueError:
            QMessageBox.warning(self, "Error", "El precio debe ser un número válido.")
            return

        # Obtener el ID de la refacción seleccionada
        refaccion_id = int(self.table.item(selected_row, 0).text())
        print(f"ID de la refacción seleccionada (desde la vista): {refaccion_id}")  # Depuración

        if self.controller.update_refaccion_pieza(refaccion_id, refaccion, precio):
            QMessageBox.information(self, "Éxito", "Refacción actualizada correctamente.")
            self.load_refacciones()  # Recargar la tabla después de actualizar
            self.input_nombre.clear()
            self.input_precio.clear()
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar la refacción.")

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
        
        
    def delete_refaccion(self):
        """Elimina la refacción seleccionada."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona una refacción para eliminar.")
            return

        refaccion_id = self.table.item(selected_row, 0).text()
        confirm = QMessageBox.question(self,"Confirmar Eliminación", f"¿Estás seguro de que deseas eliminar la refacción con ID {refaccion_id}?",
        QMessageBox.Yes | QMessageBox.No)

        if confirm == QMessageBox.Yes:
            if self.controller.delete_refaccion(refaccion_id):
                QMessageBox.information(self, "Éxito", "Refacción eliminada correctamente.")
                self.load_refacciones()  # Recargar la tabla después de eliminar
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar la refacción.")