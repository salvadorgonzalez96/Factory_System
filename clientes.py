import sys
from datetime import date, datetime, time
import re
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
from ui_clientes import Ui_MainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QAbstractItemModel
from Conexion import Conexion
from PySide6.QtWidgets import *
from PySide6.QtCore import *
#from Conexion import Conexion
#from Principal import Principal

class Clientes(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.ui.tablaclientes.clicked.connect(self.seleccionarfila)
        self.ui.tablaclientes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.btnGuardar.hide()
        self.ui.btnModificar2.hide()
        self.ui.btnrestaurar2.hide()
        self.ui.btnEliminar2.hide()
        self.llenarlista()
        self.ui.btnNuevo.clicked.connect(self.habilitarnuevo)
        self.ui.btnModificar.clicked.connect(self.habilitarmodificar)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnModificar2.clicked.connect(self.modificar)
        
    def llenarlista(self):
        self.modelo = QStandardItemModel()
        self.ui.tablaclientes.setModel(self.modelo)
        columnas = ["codigo", "nombre", "RTN", "Direccion","Telefono","Email"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT c.cliente_codigo, c.cliente_nombre, c.cliente_rtn, c.cliente_direccion, cc.cliente_contacto_telefono, cc.cliente_contacto_email FROM tbl_cliente c LEFT JOIN tbl_cliente_contacto cc ON c.cliente_codigo = cc.cliente_codigo"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.tablaclientes.hideColumn(0)

    def habilitarnuevo(self):    
        self.ui.btnNuevo.setEnabled(False)
        self.ui.btnModificar.setEnabled(True)
        self.ui.btnGuardar.setVisible(True)
        self.ui.btnModificar2.hide()
        
    def habilitarmodificar(self):
        
        self.ui.btnNuevo.setEnabled(True)
        self.ui.btnModificar.setEnabled(False)
        self.ui.btnGuardar.hide()
        self.ui.btnModificar2.setVisible(True)
        
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

    def guardar(self):
        nombre=self.ui.txtNombrecli.text()
        rtn=int(self.ui.txtRtn.text())
        direccion=self.ui.txtDireccion.text()
        telefono=int(self.ui.txtTelefono.text())    
        apoyo=int(0)   
        email=self.ui.txtEmail.text()

        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "insert into tbl_cliente (cliente_codigo, cliente_nombre, cliente_rtn, cliente_direccion) VALUES (%s, %s, %s, %s)"
        values = (apoyo, nombre, rtn, direccion)
        cursor.execute(query, values)
        conexion.commit()
        print("Se han insertado los datos en la tabla tbl_cliente.")
        cursor.close()
        conexion.close()

        # Obtener el último ID insertado
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "select cliente_codigo from tbl_cliente order by cliente_codigo desc limit 1"
        cursor.execute(query)
        resultado = cursor.fetchall()
        cliente_codigo = ""
        for row in resultado:
            cliente_codigo = str(row["cliente_codigo"])
        cursor.close()
        conexion.close()

        print(cliente_codigo)

        # Insertar los datos en la tabla tbl_cliente_contacto
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "insert into tbl_cliente_contacto (cliente_codigo, cliente_contacto_telefono, cliente_contacto_email) VALUES (%s, %s, %s)"
        values = (cliente_codigo, telefono, email)
        cursor.execute(query, values)
        conexion.commit()
        print("Se han insertado los datos en la tabla tbl_cliente_contacto.")
        cursor.close()
        conexion.close()

        self.modelo = QStandardItemModel()
        self.ui.tablaclientes.setModel(self.modelo)
        columnas = ["codigo", "nombre", "RTN", "Direccion","Telefono","Email"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT c.cliente_codigo, c.cliente_nombre, c.cliente_rtn, c.cliente_direccion, cc.cliente_contacto_telefono, cc.cliente_contacto_email FROM tbl_cliente c LEFT JOIN tbl_cliente_contacto cc ON c.cliente_codigo = cc.cliente_codigo"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.tablaclientes.hideColumn(0)
        
    def modificar(self):
        cliente_codigo = int(self.ui.txtCodigo.text())
        nombre = self.ui.txtNombrecli.text()
        rtn = int(self.ui.txtRtn.text())
        direccion = self.ui.txtDireccion.text()
        telefono = int(self.ui.txtTelefono.text())
        email = self.ui.txtEmail.text()

        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "UPDATE tbl_cliente SET cliente_nombre = %s, cliente_rtn = %s, cliente_direccion = %s WHERE cliente_codigo = %s"
        values = (nombre, rtn, direccion, cliente_codigo)
        cursor.execute(query, values)
        conexion.commit()
        #print("Se han actualizado los datos en la tabla tbl_cliente.")
        cursor.close()
        conexion.close()

        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "UPDATE tbl_cliente_contacto SET cliente_contacto_telefono = %s, cliente_contacto_email = %s WHERE cliente_codigo = %s"
        values = (telefono, email, cliente_codigo)
        cursor.execute(query, values)
        conexion.commit()
        #print("Se han actualizado los datos en la tabla tbl_cliente_contacto.")
        cursor.close()
        conexion.close()

        self.modelo = QStandardItemModel()
        self.ui.tablaclientes.setModel(self.modelo)
        columnas = ["codigo", "nombre", "RTN", "Direccion","Telefono","Email"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT c.cliente_codigo, c.cliente_nombre, c.cliente_rtn, c.cliente_direccion, cc.cliente_contacto_telefono, cc.cliente_contacto_email FROM tbl_cliente c LEFT JOIN tbl_cliente_contacto cc ON c.cliente_codigo = cc.cliente_codigo"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.tablaclientes.hideColumn(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Clientes()
    widget.show()
    sys.exit(app.exec())
