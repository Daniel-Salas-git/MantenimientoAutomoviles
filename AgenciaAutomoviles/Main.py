import sys
from PyQt5.QtWidgets import QApplication
from VistaLogin import LoginView

if __name__ == "__main__":
    # Crear la aplicación
    app = QApplication(sys.argv)

    # Crear e iniciar la ventana de Login
    login = LoginView()
    login.show()

    # Ejecutar el bucle principal de la aplicación
    sys.exit(app.exec_())