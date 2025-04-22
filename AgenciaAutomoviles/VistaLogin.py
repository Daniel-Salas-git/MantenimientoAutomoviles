from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QVBoxLayout
from UsuarioControlador import UserController
from VistaDashBoard import DashboardView

class LoginView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login - Agencia de Automóviles")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()

        self.controller = UserController()  # Instancia del controlador de usuarios

        # Etiquetas y campos de texto
        self.label_user = QLabel("Usuario:", self)
        self.label_user.move(50, 50)
        self.input_user = QLineEdit(self)
        self.input_user.move(150, 50)

        self.label_password = QLabel("Contraseña:", self)
        self.label_password.move(50, 100)
        self.input_password = QLineEdit(self)
        self.input_password.setEchoMode(QLineEdit.Password)
        self.input_password.move(150, 100)

        # Botón de login
        self.btn_login = QPushButton("Iniciar Sesión", self)
        self.btn_login.move(150, 150)
        self.btn_login.clicked.connect(self.login)

    def login(self):
        usuario = self.input_user.text()
        contraseña = self.input_password.text()

    # Validar usuario en la base de datos
        users = self.controller.get_all_users()
        for user in users:
            if user.usuario == usuario and user.contraseña == contraseña:
                QMessageBox.information(self, "Éxito", f"Bienvenido, {user.nombre}")
                self.open_dashboard(user.rol)  # Pasar el rol al Dashboard
                return

        QMessageBox.warning(self, "Error", "Usuario o contraseña incorrectos")

    def open_dashboard(self, rol):
        """Abre el Dashboard y pasa el rol del usuario."""
        self.dashboard = DashboardView(rol, self)
        self.dashboard.show()
        self.close()
    
    def clear_fields(self):
        """Limpia los campos de usuario y contraseña."""
        self.input_user.clear()
        self.input_password.clear()