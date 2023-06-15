# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from ui_categoria import Ui_MainWindow
from Conexion import Conexion
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QListView
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QTableView, QHeaderView, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QStandardItem, QStandardItemModel


class Ventas(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.ui.btnGuardar.hide()
        self.ui.btnEliminar2.hide()
        self.ui.btnModificar2.hide()
        self.ui.btnRestaurar2.hide()
        self.ui.txtnombrecat.setReadOnly(True)
        self.ui.txtdescripcioncat.setReadOnly(True)
        
        self.llenar()
        self.ui.tablacategoria.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.btnNuevo.clicked.connect(self.habilitarnuevo)
        self.ui.btnEliminar.clicked.connect(self.habilitareliminar)
        self.ui.btnModificar.clicked.connect(self.habilitarmodificar)
        self.ui.btnRestaurar.clicked.connect(self.habilitarrestaurar)
        self.ui.tablacategoria.clicked.connect(self.seleccionarfila)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnModificar2.clicked.connect(self.modificar)

    def guardar(self):
        nombre=self.ui.txtnombrecat.text()
        descripcion=self.ui.txtdescripcioncat.text()
        apoyo=int(0)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "insert into tbl_categoria (categoria_codigo, categoria_nombre, categoria_descripcion) VALUES (%s, %s, %s)"
        values = (apoyo,nombre,descripcion)
        cursor.execute(query, values)
        conexion.commit()
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se ha agregado la nueva categoria")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el guardado de la nueva categoria")
        cursor.close()
        conexion.close()
        self.llenar()

    def modificar(self):
        nombre = self.ui.txtnombrecat.text()
        descripcion = self.ui.txtdescripcioncat.text()
        codigos = self.ui.txtcodigocat.text()

        if codigos.isdigit():
            codigo = int(codigos)
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "El código debe ser un número entero")
            return

        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "UPDATE tbl_categoria SET categoria_nombre=%s, categoria_descripcion=%s WHERE categoria_codigo=%s"
        values = (nombre, descripcion, codigo)

        cursor.execute(query, values)
        conexion.commit()

        if cursor.rowcount > 0:
            QtWidgets.QMessageBox.information(None, "Mensaje", "Se ha modificado la categoría")
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "No se ha encontrado la categoría con el código especificado")

        cursor.close()
        conexion.close()

        self.llenar()

    #def eliminar(self):

    def habilitarnuevo(self):
        self.ui.btnNuevo.setEnabled(False)
        self.ui.btnModificar.setEnabled(True)
        self.ui.btnEliminar.setEnabled(True)
        self.ui.btnRestaurar.setEnabled(True)
        self.ui.btnGuardar.setVisible(True)
        self.ui.btnEliminar2.hide()
        self.ui.btnModificar2.hide()
        self.ui.txtnombrecat.setReadOnly(False)
        self.ui.txtdescripcioncat.setReadOnly(False)

    def habilitarmodificar(self):
        self.ui.btnNuevo.setEnabled(True)
        self.ui.btnModificar.setEnabled(False)
        self.ui.btnEliminar.setEnabled(True)
        self.ui.btnRestaurar.setEnabled(True)
        self.ui.btnModificar2.setVisible(True)
        self.ui.btnEliminar2.hide()
        self.ui.btnRestaurar2.hide()
        self.ui.btnGuardar.hide()
        self.ui.txtnombrecat.setReadOnly(False)
        self.ui.txtdescripcioncat.setReadOnly(False)

    def habilitareliminar(self):
        self.ui.btnNuevo.setEnabled(True)
        self.ui.btnModificar.setEnabled(True)
        self.ui.btnEliminar.setEnabled(False)
        self.ui.btnRestaurar.setEnabled(True)
        self.ui.btnEliminar2.setVisible(True)
        self.ui.btnModificar2.hide()
        self.ui.btnRestaurar2.hide()
        self.ui.btnGuardar.hide()
        self.ui.txtnombrecat.setReadOnly(True)
        self.ui.txtdescripcioncat.setReadOnly(True) 

    def habilitarrestaurar(self):
        self.ui.btnNuevo.setEnabled(True)
        self.ui.btnModificar.setEnabled(True)
        self.ui.btnEliminar.setEnabled(True)
        self.ui.btnRestaurar.setEnabled(False)
        self.ui.btnEliminar2.hide()
        self.ui.btnModificar2.hide()
        self.ui.btnRestaurar2.setVisible(True)
        self.ui.btnGuardar.hide()
        self.ui.txtnombrecat.setReadOnly(True)
        self.ui.txtdescripcioncat.setReadOnly(True)               
    def llenar(self):
        self.modelo = QStandardItemModel()
        self.ui.tablacategoria.setModel(self.modelo)
        
        columnas = ["codigo","nombre","descripcion"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        # Obtener la conexión a la base de datos
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        # Ejecutar la consulta
        consulta = "select * from tbl_categoria"
        cursor.execute(consulta)
        # Llenar el modelo con los datos obtenidos
        for fila_datos in cursor:
            # Crear una fila en el modelo
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()

   
    def seleccionarfila(self, index):
        # Obtener la fila seleccionada
        fila = index.row()
        codigo=self.modelo.index(fila,0).data()
        nombre = self.modelo.index(fila, 1).data()
        descripcion = self.modelo.index(fila, 2).data()
    

        # Establecer los valores en los campos correspondientes
        self.ui.txtcodigocat.setText((codigo))
        self.ui.txtnombrecat.setText(nombre)
        self.ui.txtdescripcioncat.setText(descripcion)


   

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Ventas()
    widget.show()
    sys.exit(app.exec())
