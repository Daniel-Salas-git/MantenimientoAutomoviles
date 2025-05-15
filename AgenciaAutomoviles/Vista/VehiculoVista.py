from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QDialog, QMessageBox
from Controlador.VehiculoControlador import VehicleController
from Vista.CuadroDialogoVehiculos import VehiculoDialog

class VehicleView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Vehículos")
        self.setGeometry(100, 100, 800, 600)

        self.controller = VehicleController()  # Instancia del controlador

        # Layout principal
        self.layout = QVBoxLayout()

        # Tabla para mostrar vehículos
        self.table = QTableWidget(self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Marca", "Modelo", "Año", "Placa", "Cliente", "Teléfono"])
        self.layout.addWidget(self.table)

        self.btn_add = QPushButton("Agregar Vehículo", self)
        self.btn_add.clicked.connect(self.add_vehiculo)
        self.layout.addWidget(self.btn_add)

        self.btn_update = QPushButton("Actualizar Vehículo", self)
        self.btn_update.clicked.connect(self.update_vehiculo)
        self.layout.addWidget(self.btn_update)
        
        self.btn_ver_servicios = QPushButton("Ver Servicios", self)
        self.btn_ver_servicios.clicked.connect(self.view_services)
        self.layout.addWidget(self.btn_ver_servicios)

        self.btn_delete = QPushButton("Eliminar Vehículo", self)
        self.btn_delete.clicked.connect(self.delete_vehiculo)
        self.layout.addWidget(self.btn_delete)

        # Contenedor principal
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Cargar datos iniciales
        self.load_vehicles()

    def load_vehicles(self):
        """Carga los vehículos desde el controlador y los muestra en la tabla."""
        vehicles = self.controller.get_all_vehicles()
        self.table.setRowCount(len(vehicles))
        for row_idx, vehicle in enumerate(vehicles):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(vehicle.id)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(vehicle.marca))
            self.table.setItem(row_idx, 2, QTableWidgetItem(vehicle.modelo))
            self.table.setItem(row_idx, 3, QTableWidgetItem(str(vehicle.año)))
            self.table.setItem(row_idx, 4, QTableWidgetItem(vehicle.placa))
            self.table.setItem(row_idx, 5, QTableWidgetItem(vehicle.cliente))
            self.table.setItem(row_idx, 6, QTableWidgetItem(vehicle.telefono))
            
    def add_vehiculo(self):
        """Abre un cuadro de diálogo para agregar un nuevo vehículo."""
        dialog = VehiculoDialog()
        if dialog.exec_() == QDialog.Accepted:
            marca, modelo, anio, placa, cliente, telefono = dialog.get_data()
            if self.controller.add_vehicle(marca, modelo, anio, placa, cliente, telefono):
                QMessageBox.information(self, "Éxito", "Vehículo agregado correctamente.")
                self.load_vehicles()
            else:
                QMessageBox.critical(self, "Error", "No se pudo agregar el vehículo.")

    def update_vehiculo(self):
        """Abre un cuadro de diálogo para actualizar un vehículo seleccionado."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un vehículo para actualizar.")
            return
        vehiculo_id = self.table.item(selected_row, 0).text()
        marca = self.table.item(selected_row, 1).text()
        modelo = self.table.item(selected_row, 2).text()
        anio = self.table.item(selected_row, 3).text()
        placa = self.table.item(selected_row, 4).text()
        cliente = self.table.item(selected_row, 5).text()
        telefono = self.table.item(selected_row, 6).text()

        dialog = VehiculoDialog(marca, modelo, anio, placa, cliente, telefono)
        if dialog.exec_() == QDialog.Accepted:
            nueva_marca, nuevo_modelo, nuevo_anio, nuevo_placa, nuevo_cliente, nuevo_telefono = dialog.get_data()
            if self.controller.update_vehicle(vehiculo_id, nueva_marca, nuevo_modelo, nuevo_anio, nuevo_placa, nuevo_cliente, nuevo_telefono):
                QMessageBox.information(self, "Éxito", "Vehículo actualizado correctamente.")
                self.load_vehicles()
            else:
                QMessageBox.critical(self, "Error", "No se pudo actualizar el vehículo.")
                
    def delete_vehiculo(self):
        """Elimina el vehículo seleccionado."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un vehículo para eliminar.")
            return

        vehiculo_id = self.table.item(selected_row, 0).text()
        if self.controller.delete_vehiculo(vehiculo_id):
            QMessageBox.information(self, "Éxito", "Vehículo eliminado correctamente.")
            self.load_vehicles()
        else:
            QMessageBox.critical(self, "Error", "No se pudo eliminar el vehículo.")
            
    def view_services(self):
        """Muestra los servicios asociados al vehículo seleccionado."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un vehículo para ver sus servicios.")
            return

        id_vehiculo = self.table.item(selected_row, 0).text()  # Obtener el ID del vehículo seleccionado

        # Obtener los servicios asociados al vehículo desde el controlador
        servicios = self.controller.get_services_by_vehicle(id_vehiculo)
        if not servicios:
            QMessageBox.information(self, "Sin Servicios", "No hay servicios registrados para este vehículo.")
            return

        # Crear una nueva ventana para mostrar la tabla
        self.servicios_window = QMainWindow()  # Guardar referencia en self
        self.servicios_window.setWindowTitle(f"Servicios Asociados al Vehículo {id_vehiculo}")
        self.servicios_window.setGeometry(100, 100, 800, 600)
    
        layout = QVBoxLayout()

        self.table_servicios = QTableWidget(self.servicios_window)
        self.table_servicios.setColumnCount(7)
        self.table_servicios.setHorizontalHeaderLabels(["Folio", "Estatus", "Fecha Servicio", "Próximo Servicio", "Diagnostico", "Responsable", "Entregado Por"])
        self.table_servicios.setRowCount(len(servicios))

        for row_idx, servicio in enumerate(servicios):
            self.table_servicios.setItem(row_idx, 0, QTableWidgetItem(str(servicio[0])))  # Folio
            self.table_servicios.setItem(row_idx, 1, QTableWidgetItem(servicio[1]))       # Estatus

            # Convertir las fechas a cadenas antes de insertarlas
            fecha_servicio = servicio[2].strftime("%Y-%m-%d") if servicio[2] else ""
            proximo_servicio = servicio[3].strftime("%Y-%m-%d") if servicio[3] else ""

            self.table_servicios.setItem(row_idx, 2, QTableWidgetItem(fecha_servicio))    # Fecha Servicio
            self.table_servicios.setItem(row_idx, 3, QTableWidgetItem(proximo_servicio)) # Próximo Servicio
            self.table_servicios.setItem(row_idx, 4, QTableWidgetItem(servicio[4]))      # Diagnostico
            self.table_servicios.setItem(row_idx, 4, QTableWidgetItem(servicio[5]))      # Responsable
            self.table_servicios.setItem(row_idx, 5, QTableWidgetItem(servicio[6]))      # Entregado Por

        layout.addWidget(self.table_servicios)

        # Contenedor principal
        container = QWidget()
        container.setLayout(layout)
        self.servicios_window.setCentralWidget(container)
        self.servicios_window.show()
            
