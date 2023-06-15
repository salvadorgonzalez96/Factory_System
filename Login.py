import sys
from PySide6 import QtWidgets
from ui_login import Ui_MainWindow
from Conexion import Conexion
from utilidades import *
from Principal import Principal

class Login(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)

        self.ui.btningresar.clicked.connect(self.iniciarSesion)

    def iniciarSesion(self):
        usuario = self.ui.txtusuario.text()
        clave = self.ui.txtcontra.text()

        conexion = Conexion().getConexion()

        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM tbl_usuario WHERE usuario_nick = \'' + usuario + '\' AND usuario_clave = \'' + clave + '\' AND usuario_estado = \'habilitado\'' )
        resultado = cursor.fetchall()

        for row in resultado:
            print(row["usuario_codigo"])

        conexion.close()

        if (len(resultado) == 1):
            self.close()
            widget = Principal() 
            widget.show()
            widget.exec()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("El usuario y la clave no coinciden")
            msgBox.exec()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Login()
    widget.show()
    sys.exit(app.exec())
