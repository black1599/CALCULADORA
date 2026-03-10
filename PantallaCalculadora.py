from PySide6 import QtWidgets

from pantalla import Ui_MainWindow

class PantallaCalculadora(QtWidgets.QMainWindow, Ui_MainWindow):
    "Clase básica que carga la interfaz generada por QtDesigner"

    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def opera(self):
        #Método que se llamará al hacer clic en el botón de operar
        pass
    def verificar(self):
        #Método que se llamará al hacer clic en el botón de operar
        pass

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PantallaCalculadora()
    window.show()
    sys.exit(app.exec_())