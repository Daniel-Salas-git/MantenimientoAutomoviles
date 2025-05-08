from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QMessageBox, QDialog, QComboBox,QDateEdit
from PyQt5.QtCore import QDate
from ServicioControlador import ServiceController
from CuadroDialogoRefacciones import RefaccionSelectorDialog

class ServiceView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Servicios")
        self.setGeometry(100, 100, 800, 600)

        self.controller = ServiceController()  # Instancia del controlador

        # Layout principal
        self.layout = QVBoxLayout()
        
        # Tabla para mostrar servicios
        self.table = QTableWidget(self)
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Folio", "ID Vehículo", "Estatus", "Fecha Servicio", "Próximo Servicio", "Diagnostico","Responsable", "Entregado Por"])
        self.layout.addWidget(self.table)

        # Campos de entrada
        #self.label_id_vehiculo = QLabel("ID Vehículo:", self)
        #self.input_id_vehiculo = QLineEdit(self)
        #self.layout.addWidget(self.label_id_vehiculo)
        #self.layout.addWidget(self.input_id_vehiculo)

        self.label_id_vehiculo = QLabel("ID Vehículo:")
        self.input_id_vehiculo = QComboBox(self)  # Cambiar QLineEdit por QComboBox
        self.populate_entregado_por_combobox()  # Llenar el combobox con los ids
        self.layout.addWidget(self.label_id_vehiculo)
        self.layout.addWidget(self.input_id_vehiculo)

        # Campo para seleccionar el estado del servicio
        self.label_estatus = QLabel("Estatus del Servicio:")
        self.input_estatus = QComboBox(self)  # Cambiar QLineEdit por QComboBox
        self.input_estatus.addItem("Selecciona una opción")  # Opción inicial vacía
        self.input_estatus.addItems(["En proceso", "En espera", "Finalizado"])  # Opciones del combobox
        self.layout.addWidget(self.label_estatus)
        self.layout.addWidget(self.input_estatus)

        # Campo para la fecha de servicio
        self.label_fecha_servicio = QLabel("Fecha de Servicio:")
        self.input_fecha_servicio = QDateEdit(self)
        self.input_fecha_servicio.setCalendarPopup(True)  # Habilitar el calendario desplegable
        self.input_fecha_servicio.setDisplayFormat("yyyy-MM-dd")  # Formato de fecha
        self.input_fecha_servicio.setDate(QDate.currentDate())  # Fecha actual por defecto
        self.layout.addWidget(self.label_fecha_servicio)
        self.layout.addWidget(self.input_fecha_servicio)

        # Campo para la próxima fecha de servicio
        self.label_proximo_servicio = QLabel("Próximo Servicio:")
        self.input_proximo_servicio = QDateEdit(self)
        self.input_proximo_servicio.setCalendarPopup(True)  # Habilitar el calendario desplegable
        self.input_proximo_servicio.setDisplayFormat("yyyy-MM-dd")  # Formato de fecha
        self.input_proximo_servicio.setDate(QDate.currentDate())  # Fecha actual por defecto
        self.layout.addWidget(self.label_proximo_servicio)
        self.layout.addWidget(self.input_proximo_servicio)
        
        self.label_diagnostico = QLabel("Diagnóstico:")
        self.input_diagnostico = QLineEdit(self)
        self.layout.addWidget(self.label_diagnostico)
        self.layout.addWidget(self.input_diagnostico)

        # Campo para seleccionar el responsable
        self.label_responsable = QLabel("Responsable:")
        self.input_responsable = QComboBox(self) 
        self.populate_responsable_combobox()  # Llenar el combobox con los usuarios
        self.layout.addWidget(self.label_responsable)
        self.layout.addWidget(self.input_responsable)
        
        self.label_entregado_por = QLabel("Entregado Por:", self)
        self.input_entregado_por = QLineEdit(self)
        self.layout.addWidget(self.label_entregado_por)
        self.layout.addWidget(self.input_entregado_por)

        # Botones
        self.btn_add = QPushButton("Agregar Servicio", self)
        self.btn_add.clicked.connect(self.add_service)
        self.layout.addWidget(self.btn_add)

        self.btn_update = QPushButton("Actualizar Servicio", self)
        self.btn_update.clicked.connect(self.update_service)
        self.layout.addWidget(self.btn_update)

        self.btn_delete = QPushButton("Eliminar Servicio", self)
        self.btn_delete.clicked.connect(self.delete_service)
        self.layout.addWidget(self.btn_delete)

        self.btn_refresh = QPushButton("Actualizar Tabla", self)
        self.btn_refresh.clicked.connect(self.load_services)
        self.layout.addWidget(self.btn_refresh)
        
        self.btn_add_refaccion = QPushButton("Asociar Refacción", self)
        self.btn_add_refaccion.clicked.connect(self.add_refaccion_to_service)
        self.layout.addWidget(self.btn_add_refaccion)
        
        self.btn_view_refacciones = QPushButton("Ver Refacciones", self)
        self.btn_view_refacciones.clicked.connect(self.view_refacciones)
        self.layout.addWidget(self.btn_view_refacciones)

        # Contenedor principal
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Cargar datos iniciales
        self.load_services()

    def load_services(self):
        """Carga los servicios desde el controlador y los muestra en la tabla."""
        services = self.controller.get_all_services()
        self.table.setRowCount(len(services))
        for row_idx, service in enumerate(services):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(service.folio)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(str(service.id_vehiculo)))
            self.table.setItem(row_idx, 2, QTableWidgetItem(service.estatus))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(service.fecha_servicio)))
            self.table.setItem(row_idx, 4, QTableWidgetItem(str(service.proximo_servicio)))
            self.table.setItem(row_idx, 5, QTableWidgetItem(service.diagnostico))
            self.table.setItem(row_idx, 6, QTableWidgetItem(service.responsable))
            self.table.setItem(row_idx, 7, QTableWidgetItem(service.entregado_por))

    def add_service(self):
        """Agrega un nuevo servicio utilizando el controlador."""
        id_vehiculo = self.input_id_vehiculo.currentData()  # Obtener el ID del vehículo seleccionado
        if not id_vehiculo:
            QMessageBox.warning(self, "Error", "Debes seleccionar un vehículo válido.")
            return

        estatus = self.input_estatus.currentText()
        fecha_servicio = self.input_fecha_servicio.date().toString("yyyy-MM-dd")  # Obtener la fecha seleccionada
        proximo_servicio = self.input_proximo_servicio.date().toString("yyyy-MM-dd")  # Obtener la fecha seleccionada
        responsable = self.input_responsable.currentText()
        entregado_por = self.input_entregado_por.text()
        diagonostico = self.input_diagnostico.text()

        if not (estatus and fecha_servicio and proximo_servicio and responsable and entregado_por and diagonostico):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        
        if estatus == "Selecciona una opción":
            QMessageBox.warning(self, "Error", "Debes seleccionar un estatus válido.")
            return

        if self.controller.add_service(id_vehiculo, estatus, fecha_servicio, proximo_servicio, responsable, entregado_por, diagonostico):
            QMessageBox.information(self, "Éxito", "Servicio agregado correctamente.")
            self.load_services()
            self.populate_entregado_por_combobox()  # Volver a llenar el combobox
            self.clear_fields()
        else:
            QMessageBox.critical(self, "Error", "No se pudo agregar el servicio.")

    def update_service(self):
        """Actualiza un servicio seleccionado utilizando el controlador."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un servicio para actualizar.")
            return
        id_vehiculo = self.input_id_vehiculo.currentData()  # Obtener el ID del vehículo seleccionado
        if not id_vehiculo:
            QMessageBox.warning(self, "Error", "Debes seleccionar un vehículo válido.")
            return

        folio = self.table.item(selected_row, 0).text()
        estatus = self.input_estatus.currentText()
        fecha_servicio = self.input_fecha_servicio.date().toString("yyyy-MM-dd")  # Obtener la fecha seleccionada
        proximo_servicio = self.input_proximo_servicio.date().toString("yyyy-MM-dd")  # Obtener la fecha seleccionada
        responsable = self.input_responsable.currentText()
        entregado_por = self.input_entregado_por.text()
        diagnostico = self.input_diagnostico.text()

        if not (estatus and fecha_servicio and proximo_servicio and responsable and entregado_por and diagnostico):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return
        
        if estatus == "Selecciona una opción":
            QMessageBox.warning(self, "Error", "Debes seleccionar un estatus válido.")
            return

        if self.controller.update_service(folio, id_vehiculo, estatus, fecha_servicio, proximo_servicio, responsable, entregado_por, diagnostico):
            QMessageBox.information(self, "Éxito", "Servicio actualizado correctamente.")
            self.load_services()
            self.populate_entregado_por_combobox()  # Volver a llenar el combobox
            self.clear_fields()
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar el servicio.")

    def delete_service(self):
        """Elimina un servicio seleccionado utilizando el controlador."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un servicio para eliminar.")
            return

        folio = self.table.item(selected_row, 0).text()

        if self.controller.delete_service(folio):
            QMessageBox.information(self, "Éxito", "Servicio eliminado correctamente.")
            self.load_services()
        else:
            QMessageBox.critical(self, "Error", "No se pudo eliminar el servicio.")
            
    def add_refaccion_to_service(self):
        """Asocia una refacción a un servicio seleccionado."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un servicio para asociar una refacción.")
            return

        id_servicio = self.table.item(selected_row, 0).text()

        # Abrir el cuadro de diálogo para seleccionar una refacción
        dialog = RefaccionSelectorDialog()
        if dialog.exec_() == QDialog.Accepted:
            id_refaccion = dialog.selected_refaccion
            cantidad = dialog.selected_cantidad
            
            if not id_refaccion or not cantidad:
                QMessageBox.warning(self, "Error", "No se seleccionó una refacción o cantidad válida.")
                return

            if self.controller.add_refaccion_to_service(id_servicio, id_refaccion, cantidad):
                QMessageBox.information(self, "Éxito", "Refacción asociada correctamente.")
            else:
                QMessageBox.critical(self, "Error", "No se pudo asociar la refacción.")
        else:
            # Si el cuadro de diálogo fue cerrado sin aceptar, no hacer nada
            QMessageBox.information(self, "Cancelado", "No se seleccionó ninguna refacción.")
    
    def view_refacciones(self):
        """Muestra las refacciones asociadas al servicio seleccionado."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un servicio para ver sus refacciones.")
            return

        id_servicio = self.table.item(selected_row, 0).text()  # Obtener el ID del servicio seleccionado

        # Obtener las refacciones asociadas al servicio desde el controlador
        refacciones = self.controller.get_refacciones_by_service(id_servicio)
        if not refacciones:
            QMessageBox.information(self, "Sin Refacciones", "No hay refacciones asociadas a este servicio.")
            return

        # Crear una nueva ventana para mostrar la tabla
        self.refaccion_window = QMainWindow()  # Guardar referencia en self
        self.refaccion_window.setWindowTitle(f"Refacciones Asociadas al Servicio {id_servicio}")
        self.refaccion_window.setGeometry(100, 100, 800, 600)
        
        layout = QVBoxLayout()

        self.table_refacciones = QTableWidget(self.refaccion_window)
        self.table_refacciones.setColumnCount(4)
        self.table_refacciones.setHorizontalHeaderLabels(["Folio Servicio", "Refacción", "Cantidad", "Precio"])
        self.table_refacciones.setRowCount(len(refacciones))
        
        total = 0  # Calcular el precio total
        
        for row_idx, ref in enumerate(refacciones):
            id_servicio = ref[0]
            refacciones = ref[1]
            cantidad = ref[2]
            precio_unitario = ref[3]
            precio_total = cantidad * precio_unitario  # Calcular el precio total por refacción
            
            self.table_refacciones.setItem(row_idx, 0, QTableWidgetItem(str(ref[0])))  # Folio del servicio
            self.table_refacciones.setItem(row_idx, 1, QTableWidgetItem(ref[1]))       # Nombre de la refacción
            self.table_refacciones.setItem(row_idx, 2, QTableWidgetItem(str(ref[2])))  # Cantidad
            self.table_refacciones.setItem(row_idx, 3, QTableWidgetItem(f"${precio_total:.2f}"))  # Precio
            total += precio_total  # Sumar al total general

        layout.addWidget(self.table_refacciones)
        
        # Mostrar el total
        self.label_total = QLabel(f"Total: ${total:.2f}", self.refaccion_window)
        layout.addWidget(self.label_total)

    # Botón para eliminar refacción
        self.btn_delete_refaccion = QPushButton("Eliminar Refacción", self.refaccion_window)
        self.btn_delete_refaccion.clicked.connect(self.delete_refaccion)
        layout.addWidget(self.btn_delete_refaccion)

    # Contenedor principal
        container = QWidget()
        container.setLayout(layout)
        self.refaccion_window.setCentralWidget(container)
        self.refaccion_window.show()
        
    def delete_refaccion(self):
        """Elimina la refacción seleccionada de la tabla."""
        selected_row = self.table_refacciones.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona una refacción para eliminar.")
            return

    # Obtener los datos de la refacción seleccionada
        id_servicio = self.table_refacciones.item(selected_row, 0).text()
        nombre_refaccion = self.table_refacciones.item(selected_row, 1).text()

    # Confirmar la eliminación
        confirm = QMessageBox.question(
            self, "Confirmar Eliminación",
            f"¿Estás seguro de que deseas eliminar la refacción '{nombre_refaccion}' del servicio {id_servicio}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            # Llamar al controlador para eliminar la refacción
            if self.controller.delete_refaccion_from_service(id_servicio, nombre_refaccion):
                QMessageBox.information(self, "Éxito", "Refacción eliminada correctamente.")
                self.view_refacciones()  # Recargar la tabla
            else:
                QMessageBox.critical(self, "Error", "No se pudo eliminar la refacción.")
    
    def populate_responsable_combobox(self):
        """Llena el combobox de responsables con los usuarios registrados."""
        usuarios = self.controller.get_all_users()  # Obtener usuarios desde el controlador
        if usuarios:
            self.input_responsable.addItem("Selecciona un responsable")  # Opción inicial
            nombres_usuarios = [user.nombre for user in usuarios]  # Extraer los nombres de los objetos User
            self.input_responsable.addItems(nombres_usuarios)
        else:
            QMessageBox.warning(self, "Error", "No se pudieron cargar los usuarios.")
            
    def clear_fields(self):
        """Limpia todos los campos de entrada."""
        self.input_id_vehiculo.setCurrentIndex(0)
        self.input_estatus.setCurrentIndex(0)  # Restablecer el QComboBox al valor inicial
        self.input_fecha_servicio.setDate(QDate.currentDate())  # Restablecer la fecha al día actual
        self.input_proximo_servicio.setDate(QDate.currentDate())  # Restablecer la fecha al día actual
        self.input_responsable.setCurrentIndex(0)  # Restablecer el QComboBox al valor inicial
        self.input_entregado_por.clear()
        self.input_diagnostico.clear()
        
    def populate_entregado_por_combobox(self):
        """Llena el combobox de ID Vehículo con información adicional (cliente y teléfono)."""
        self.input_id_vehiculo.clear() 
        vehiculos = self.controller.get_all_id_vehicles()  # Obtener vehículos desde el controlador
        if vehiculos:
            self.input_id_vehiculo.addItem("Selecciona un vehículo")  # Opción inicial
            for vehiculo in vehiculos:
                # Crear una descripción completa para mostrar en el combobox
                descripcion = f"{vehiculo.id} - {vehiculo.cliente} - {vehiculo.telefono}"
                self.input_id_vehiculo.addItem(descripcion, vehiculo.id)  # Asociar el ID como dato adicional
        else:
            QMessageBox.warning(self, "Error", "No se pudieron cargar los vehículos.")