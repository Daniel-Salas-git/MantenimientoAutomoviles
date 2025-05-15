from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QWidget, QLineEdit, QLabel, QMessageBox, QComboBox
from Controlador.UsuarioControlador import UserController

class UserView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Usuarios")
        self.setGeometry(100, 100, 800, 600)

        self.controller = UserController()  # Instancia del controlador

        # Layout principal
        self.layout = QVBoxLayout()

        # Tabla para mostrar usuarios
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Nombre", "Usuario", "Contraseña", "Rol"])
        self.layout.addWidget(self.table)

        # Campos de entrada
        self.label_nombre = QLabel("Nombre:", self)
        self.input_nombre = QLineEdit(self)
        self.layout.addWidget(self.label_nombre)
        self.layout.addWidget(self.input_nombre)

        self.label_usuario = QLabel("Usuario:", self)
        self.input_usuario = QLineEdit(self)
        self.layout.addWidget(self.label_usuario)
        self.layout.addWidget(self.input_usuario)

        self.label_contraseña = QLabel("Contraseña:", self)
        self.input_contraseña = QLineEdit(self)
        self.layout.addWidget(self.label_contraseña)
        self.layout.addWidget(self.input_contraseña)

        self.label_rol = QLabel("Rol:", self)
        self.input_rol = QComboBox(self)
        self.input_rol.addItem("Selecciona una opción") 
        self.input_rol.addItems(self.ROLES)  # Agregar los roles predefinidos al combobox
        self.layout.addWidget(self.label_rol)
        self.layout.addWidget(self.input_rol)

        # Botones
        self.btn_add = QPushButton("Agregar Usuario", self)
        self.btn_add.clicked.connect(self.add_user)
        self.layout.addWidget(self.btn_add)

        self.btn_update = QPushButton("Actualizar Usuario", self)
        self.btn_update.clicked.connect(self.update_user)
        self.layout.addWidget(self.btn_update)

        self.btn_delete = QPushButton("Eliminar Usuario", self)
        self.btn_delete.clicked.connect(self.delete_user)
        self.layout.addWidget(self.btn_delete)

        self.btn_refresh = QPushButton("Actualizar Tabla", self)
        self.btn_refresh.clicked.connect(self.load_users)
        self.layout.addWidget(self.btn_refresh)

        # Contenedor principal
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Cargar datos iniciales
        self.load_users()

    def load_users(self):
        """Carga los usuarios desde el controlador y los muestra en la tabla."""
        users = self.controller.get_all_users()
        self.table.setRowCount(len(users))
        for row_idx, user in enumerate(users):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(user.id)))
            self.table.setItem(row_idx, 1, QTableWidgetItem(user.nombre))
            self.table.setItem(row_idx, 2, QTableWidgetItem(user.usuario))
            self.table.setItem(row_idx, 3, QTableWidgetItem(user.contraseña))
            self.table.setItem(row_idx, 4, QTableWidgetItem(user.rol))

    def add_user(self):
        """Agrega un nuevo usuario utilizando el controlador."""
        nombre = self.input_nombre.text()
        usuario = self.input_usuario.text()
        contraseña = self.input_contraseña.text()
        rol = self.input_rol.currentText()

        if not (nombre and usuario and contraseña and rol):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        if self.controller.add_user(nombre, usuario, contraseña, rol):
            QMessageBox.information(self, "Éxito", "Usuario agregado correctamente.")
            self.load_users()
            self.clear_fields() 
        else:
            QMessageBox.critical(self, "Error", "No se pudo agregar el usuario.")

    def update_user(self):
        """Actualiza un usuario seleccionado utilizando el controlador."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un usuario para actualizar.")
            return

        user_id = self.table.item(selected_row, 0).text()
        nombre = self.input_nombre.text()
        usuario = self.input_usuario.text()
        contraseña = self.input_contraseña.text()
        rol = self.input_rol.currentText()

        if not (nombre and usuario and contraseña and rol):
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios.")
            return

        if self.controller.update_user(user_id, nombre, usuario, contraseña, rol):
            QMessageBox.information(self, "Éxito", "Usuario actualizado correctamente.")
            self.load_users()
            self.clear_fields()
        else:
            QMessageBox.critical(self, "Error", "No se pudo actualizar el usuario.")

    def delete_user(self):
        """Elimina un usuario seleccionado utilizando el controlador."""
        selected_row = self.table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Selecciona un usuario para eliminar.")
            return

        user_id = self.table.item(selected_row, 0).text()

        if self.controller.delete_user(user_id):
            QMessageBox.information(self, "Éxito", "Usuario eliminado correctamente.")
            self.load_users()
        else:
            QMessageBox.critical(self, "Error", "No se pudo eliminar el usuario.")
        
    ROLES = ["Administrador", "Gerente", "Técnico", "Recepcionista"]
    
    def clear_fields(self):
        """Limpia todos los campos de entrada."""
        self.input_nombre.clear()
        self.input_usuario.clear()
        self.input_contraseña.clear()
        self.input_rol.setCurrentIndex(0)