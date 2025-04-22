from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from ServicioControlador import ServiceController

class DashboardGraphView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tablero - Gráficas de Estatus")
        self.setGeometry(100, 100, 800, 600)

        self.controller = ServiceController()

        # Layout principal
        self.layout = QVBoxLayout()

        # Campo para filtrar por fecha
        self.label_fecha = QLabel("Filtrar por fecha (YYYY-MM-DD):", self)
        self.layout.addWidget(self.label_fecha)

        self.input_fecha = QLineEdit(self)
        self.layout.addWidget(self.input_fecha)

        self.btn_filtrar = QPushButton("Filtrar", self)
        self.btn_filtrar.clicked.connect(self.update_graph)
        self.layout.addWidget(self.btn_filtrar)

        # Botón para mostrar todos los registros
        self.btn_todos = QPushButton("Mostrar Todos", self)
        self.btn_todos.clicked.connect(self.show_all)
        self.layout.addWidget(self.btn_todos)

        # Gráfica
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        # Contenedor principal
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        # Mostrar la gráfica inicial
        self.show_all()

    def update_graph(self):
        """Actualiza la gráfica con los datos filtrados por fecha."""
        fecha = self.input_fecha.text()
        if not fecha:
            return

        status_counts = self.controller.get_status_counts(fecha)
        self.plot_graph(status_counts, f"Servicios para {fecha}")

    def show_all(self):
        """Muestra la gráfica con todos los registros."""
        status_counts = self.controller.get_status_counts()
        self.plot_graph(status_counts, "Todos los Servicios")

    def plot_graph(self, status_counts, title):
        """Genera la gráfica de barras."""
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar(status_counts.keys(), status_counts.values(), color=["blue", "orange", "green"])
        ax.set_title(title)
        ax.set_xlabel("Estatus")
        ax.set_ylabel("Cantidad")
        self.canvas.draw()