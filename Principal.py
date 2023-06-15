import sys

#from DialogRegistrarCliente import DialogRegistrarCliente
#from DialogClientes import DialogClientes
#from DialogRegistrarProveedor import DialogRegistrarProveedor
#from DialogProveedores import DialogProveedores
#from DialogRegistrarProducto import DialogRegistrarProducto
#from DialogProductos import DialogProductos
#from Login import Login

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_principal import Ui_MainWindow
from ventas import Ventas
#from inventario import Inventario
from usuarios import Usuarios
from Empleados import Empleados
from AcercaDe import AcercaDe
from clientes import Clientes 
from compras import Compras
from proveedores import Proveedores
from utilidades import *
#from Login import Login


class Principal(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)

        #self.ui.btninventario.clicked.connect(lambda funcion: self.abrirDialog(Inventario()))
        self.ui.actionUsuarios.triggered.connect(lambda funcion: self.abrirDialog(Usuarios()))
        self.ui.actionEmpleados.triggered.connect(lambda funcion: self.abrirDialog(Empleados()))
        self.ui.btnventa.clicked.connect(lambda funcion: self.abrirDialog(Ventas()))
        self.ui.actionAcerca_de.triggered.connect(lambda funcion: self.abrirDialog(AcercaDe()))
        self.ui.actionClientes.triggered.connect(lambda funcion: self.abrirDialog(Clientes()))
        self.ui.btncompra.clicked.connect(lambda funcion: self.abrirDialog(Compras()))
        self.ui.actionProveedores.triggered.connect(lambda funcion: self.abrirDialog(Proveedores()))
      #  self.ui.actionCerrar_Session.triggered.connect(lambda funcion: self.abrirDialog(Login()))
        
    def abrirDialog(self, dialog):
        dialog.show()
        dialog.exec()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Principal()
    widget.show()
    sys.exit(app.exec())
