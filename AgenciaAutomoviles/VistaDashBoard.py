from PyQt5.QtWidgets import QMainWindow, QPushButton,QVBoxLayout, QWidget
from UsuarioVista import UserView
from ServicioVista import ServiceView
from VehiculoVista import VehicleView
from GraficaDashboard import DashboardGraphView

class DashboardView(QMainWindow):
    def __init__(self, rol, login_view):
        super().__init__()
        self.setWindowTitle("Dashboard - Agencia de Automóviles")
        self.setGeometry(100, 100, 600, 400)
        
        # Guardar una referencia a la ventana de login
        self.rol = rol
        self.login_view = login_view
        
        # Layout principal
        layout = QVBoxLayout()

        # Botón de cerrar sesión
        self.btn_logout = QPushButton("Cerrar Sesión", self)
        self.btn_logout.clicked.connect(self.logout)
        layout.addWidget(self.btn_logout)


        # Botón para gestionar usuarios (solo visible para Administrador)
        if rol == "Administrador":
            self.btn_users = QPushButton("Gestión de Usuarios", self)
            self.btn_users.clicked.connect(self.open_user_view)
            layout.addWidget(self.btn_users)

        # Botón para gestionar servicios (visible para Gerente y Técnico)
        if rol in ["Administrador", "Gerente", "Técnico"]:
            self.btn_services = QPushButton("Gestión de Servicios", self)
            self.btn_services.clicked.connect(self.open_service_view)
            layout.addWidget(self.btn_services)

        # Botón para gestionar vehículos (visible para Recepcionista y Administrador)
        if rol in ["Administrador", "Recepcionista"]:
            self.btn_vehicles = QPushButton("Gestión de Vehículos", self)
            self.btn_vehicles.clicked.connect(self.open_vehicle_view)
            layout.addWidget(self.btn_vehicles)
    
        self.btn_dashboard = QPushButton("Tablero de Gráficas", self)
        self.btn_dashboard.clicked.connect(self.open_dashboard_graph)
        layout.addWidget(self.btn_dashboard)

        # Contenedor principal
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_user_view(self):
        """Abre la vista de gestión de usuarios."""
        self.user_view = UserView()
        self.user_view.show()

    def open_service_view(self):
        """Abre la vista de gestión de servicios."""
        self.service_view = ServiceView()
        self.service_view.show()

    def open_vehicle_view(self):
        """Abre la vista de gestión de vehículos."""
        self.vehicle_view = VehicleView()
        self.vehicle_view.show()
        
    def open_dashboard_graph(self):
        self.dashboard_graph = DashboardGraphView()
        self.dashboard_graph.show()
    
    def logout(self):
        """Cerrar sesión y volver a la ventana de login."""
        self.close() ## Cerrar el dashboard
        self.login_view.clear_fields()  # Limpiar los campos de usuario y contraseña
        self.login_view.show()  # Mostrar la ventana de login