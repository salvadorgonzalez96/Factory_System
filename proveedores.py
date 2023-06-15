import sys
from datetime import date, datetime, time
import re
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from ui_proveedores import Ui_MainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QAbstractItemModel
from Conexion import Conexion
from PySide6.QtWidgets import *
from PySide6.QtCore import *
#from Conexion import Conexion
#from Principal import Principal

class Proveedores(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.ui.tablaproveedores.clicked.connect(self.seleccionarfila)
        self.ui.tablaproveedores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.btnGuardar.hide()
        self.ui.btnModificar2.hide()
        self.ui.btnEliminar2.hide()
        self.ui.btnRestaurar2.hide()
        self.ui.btnRestaurar2.hide()

        self.llenarlista()
        self.ui.btnNuevo.clicked.connect(self.habilitarnuevo)
        self.ui.btnModificar.clicked.connect(self.habilitarmodificar)
        self.ui.btnEliminar.clicked.connect(self.habilitareliminar)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnModificar2.clicked.connect(self.modificar)
        self.ui.btnEliminar2.clicked.connect(self.eliminar)

    ##########################################################
    def guardar(self):
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()

    # Obtener los valores de los QLineEdit
        nombre = self.ui.txtNombrecli.text()
        rtn = self.ui.txtRtn.text()
        direccion = self.ui.txtDireccion.text()
        telefono = self.ui.txtTelefono.text()
        email = self.ui.txtEmail.text()

        query1 = "INSERT INTO tbl_proveedor (proveedor_nombre, proveedor_rtn, proveedor_direccion) VALUES (%s, %s, %s);"
        query2 = "INSERT INTO tbl_proveedor_contacto (proveedor_codigo, proveedor_contacto_telefono, proveedor_contacto_email) VALUES (%s, %s, %s);"


        # Insertar en la tabla tbl_proveedor
        valores_proveedor = (nombre, rtn, direccion)
        cursor.execute(query1, valores_proveedor)
        proveedor_codigo = cursor.lastrowid 

        # Insertar en la tabla tbl_proveedor_contacto
        valores_proveedor_contacto = (proveedor_codigo, telefono, email)
        cursor.execute(query2, valores_proveedor_contacto)
      
        conexion.commit()
        if cursor.rowcount > 0:
           QtWidgets.QMessageBox.information(None, "Mensaje","Se han agregado el proveedor")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se pudo agregar el proveedor")

        cursor.close()
        conexion.close()
        self.ui.txtNombrecli.clear()
        self.ui.txtRtn.clear()
        direccion = self.ui.txtDireccion.clear()
        self.ui.txtTelefono.clear()
        self.ui.txtEmail.clear()

    #############################################################
    
    def modificar(self):
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()

    # Obtener los valores de los QLineEdit
        codigo = self.ui.txtCodigo.text()
        nombre = self.ui.txtNombrecli.text()
        rtn = self.ui.txtRtn.text()
        direccion = self.ui.txtDireccion.text()
        telefono = self.ui.txtTelefono.text()
        email = self.ui.txtEmail.text()

        query1 = "UPDATE tbl_proveedor SET proveedor_nombre = %s, proveedor_rtn = %s, proveedor_direccion = %s WHERE proveedor_codigo = %s;"
        query2 = "UPDATE tbl_proveedor_contacto SET proveedor_contacto_telefono = %s, proveedor_contacto_email = %s WHERE proveedor_codigo = %s;"

        # Actualizar en la tabla tbl_proveedor
        valores_proveedor = (nombre, rtn, direccion, codigo)
        cursor.execute(query1, valores_proveedor)

         # Actualizar en la tabla tbl_proveedor_contacto
        valores_proveedor_contacto = (telefono, email, codigo)
        cursor.execute(query2, valores_proveedor_contacto)

        conexion.commit()
        if conexion.commit() is None:
           QtWidgets.QMessageBox.information(None, "Mensaje","Se han actualizado los datos del proveedor")
        else:
           QtWidgets.QMessageBox.critical(None, "Error", "No se ha podido actualizar los datos del proveedor")
        cursor.close()
        conexion.close()

     
    #################################################################
    def eliminar(self):
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()

        # Obtener el valor del ID del proveedor a eliminar
        proveedor_codigo = self.ui.txtCodigo.text()

        # Consulta SQL para eliminar los registros de la tabla tbl_proveedor_contacto que hacen referencia al proveedor
        query1 = "DELETE FROM tbl_proveedor_contacto WHERE proveedor_codigo = %s"

        # Consulta SQL para eliminar el proveedor de la tabla tbl_proveedor
        query2 = "DELETE FROM tbl_proveedor WHERE proveedor_codigo = %s"

        # Eliminar los registros de la tabla tbl_proveedor_contacto que hacen referencia al proveedor
        cursor.execute(query1, (proveedor_codigo,))

        # Eliminar el proveedor de la tabla tbl_proveedor
        cursor.execute(query2, (proveedor_codigo,))

        conexion.commit()

        if cursor.rowcount > 0:
           QtWidgets.QMessageBox.information(None, "Mensaje", "Se ha eliminado el proveedor")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se ha podido eliminar el proveedor")

        cursor.close()
        conexion.close()




    def llenarlista(self):
        self.modelo = QStandardItemModel()
        self.ui.tablaproveedores.setModel(self.modelo)
        columnas = ["codigo", "nombre", "RTN", "Direccion","Telefono","Email"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = """SELECT p.proveedor_codigo, p.proveedor_nombre, p.proveedor_rtn, p.proveedor_direccion, pc.proveedor_contacto_telefono, pc.proveedor_contacto_email 
                    FROM tbl_proveedor p 
                    LEFT JOIN tbl_proveedor_contacto pc ON p.proveedor_codigo = pc.proveedor_codigo;"""
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()

    def desahabilitarcampos(self):
        self.ui.txtCodigo.setReadOnly(True)
        self.ui.txtNombrecli.setReadOnly(True)
        self.ui.txtRtn.setReadOnly(True)
        self.ui.txtDireccion.setReadOnly(True)
        self.ui.txtEmail.setReadOnly(True)
        self.ui.txtTelefono.setReadOnly(True)
      

    def habilitarcampos(self):
        self.ui.txtCodigo.setReadOnly(False)
        self.ui.txtNombrecli.setReadOnly(False)
        self.ui.txtRtn.setReadOnly(False)
        self.ui.txtDireccion.setReadOnly(False)
        self.ui.txtEmail.setReadOnly(False)
        self.ui.txtTelefono.setReadOnly(False)
         
    def habilitarnuevo(self):    
        self.ui.btnNuevo.setEnabled(False)
        self.ui.btnEliminar.setEnabled(True)
        self.ui.btnModificar.setEnabled(True)
        self.ui.btnModificar2.hide()
        self.ui.btnEliminar2.hide()
        self.ui.btnGuardar.setVisible(True)
        
    def habilitarmodificar(self):
        
        self.ui.btnNuevo.setEnabled(True)
        self.ui.btnGuardar.hide()
        self.ui.btnEliminar2.hide()
        self.ui.btnEliminar.setEnabled(True)
        self.ui.btnModificar2.setVisible(True)
        self.ui.btnModificar.setEnabled(False)

    def habilitareliminar(self):
        self.ui.btnNuevo.setEnabled(True)
        self.ui.btnGuardar.hide()
        self.ui.btnModificar.setEnabled(True)
        self.ui.btnModificar2.hide()
        self.ui.btnEliminar2.setVisible(True)
        self.ui.btnEliminar.setEnabled(False)
        self.ui.txtCodigo.setReadOnly(True)
        self.ui.txtNombrecli.setReadOnly(True)
        self.ui.txtRtn.setReadOnly(True)
        self.ui.txtDireccion.setReadOnly(True)
        self.ui.txtEmail.setReadOnly(True)
        self.ui.txtTelefono.setReadOnly(True)
       
        
    def seleccionarfila(self, index):

        fila = index.row()
        codigo=self.modelo.index(fila,0).data()
        nombre=self.modelo.index(fila,1).data()
        rtn=self.modelo.index(fila,2).data()
        direccion=self.modelo.index(fila,3).data()
        telefono=self.modelo.index(fila,4).data()
        email=self.modelo.index(fila,5).data()

        self.ui.txtCodigo.setText(codigo)
        self.ui.txtNombrecli.setText(nombre)
        self.ui.txtTelefono.setText(telefono)
        self.ui.txtRtn.setText(rtn)
        self.ui.txtDireccion.setText(direccion)
        self.ui.txtEmail.setText(email)


        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Proveedores()
    widget.show()
    sys.exit(app.exec())