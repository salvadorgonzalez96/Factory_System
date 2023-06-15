import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_accesousuarios import Ui_MainWindow
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QListView
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from Conexion import Conexion
from utilidades import *

class Accesousuarios(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.conexion = Conexion().getConexion()
        self.llenarcombobox()
        self.conexion.close()
        self.ui.comboemple.activated.connect(self.llenarfila)
        self.ui.listaccesoreg.clicked.connect(self.seleccionarfilaizq)
        self.ui.listaccesoenlis.clicked.connect(self.seleccionarfilader)
        self.ui.listaccesoenlis.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.listaccesoreg.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def llenarcombobox(self):
        codigos = ""
        cursor = self.conexion.cursor()
        cursor.execute("SELECT usuario_nick,usuario_codigo FROM tbl_usuario where usuario_estado='habilitado'")
        resultados = cursor.fetchall()
        self.ui.comboemple.clear()
        self.ui.comboemple.addItem("Seleccione un Usuario")
        self.ui.cmbCodigoUsuario.clear()
        self.ui.cmbCodigoUsuario.addItem("Seleccione un Usuario")
        for row in resultados:
            codigos = str(row["usuario_codigo"])
            self.ui.comboemple.addItem(row["usuario_nick"], userData = row)
            self.ui.cmbCodigoUsuario.addItem(codigos, userData = row)
        cursor.close()
        
    def llenarfila(self, index):
        self.ui.cmbCodigoUsuario.setCurrentIndex(index)
        valor=self.ui.cmbCodigoUsuario.currentText()
        self.modelo = QStandardItemModel()
        self.ui.listaccesoreg.setModel(self.modelo)
        columnas = ["Codigo","Modulo"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT  m.modulo_codigo, m.modulo_nombre FROM tbl_acceso a INNER JOIN tbl_modulo m ON a.modulo_codigo = m.modulo_codigo WHERE a.usuario_codigo = %s AND a.acceso_estado = 'inactivo'"
        cursor.execute(consulta,valor)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()

        self.modelo2 = QStandardItemModel()
        self.ui.listaccesoenlis.setModel(self.modelo2)
        columnas = ["Codigo","Modulo"]
        self.modelo2.setHorizontalHeaderLabels(columnas)
        
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT m.modulo_codigo, m.modulo_nombre FROM tbl_acceso a INNER JOIN tbl_modulo m ON a.modulo_codigo = m.modulo_codigo WHERE a.usuario_codigo = %s AND a.acceso_estado = 'activo'"
        cursor.execute(consulta,valor)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo2.appendRow(fila)
        cursor.close()
        conexion.close()

        self.ui.listaccesoenlis.hideColumn(0)
        self.ui.listaccesoreg.hideColumn(0)

    def seleccionarfilaizq(self, index):
        fila = index.row()
        importante=self.modelo.index(fila,0).data()
        module=self.modelo.index(fila,1).data()
        #print(importante)
        #print(module)
        valor=self.ui.cmbCodigoUsuario.currentText()
        #print(valor)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "UPDATE tbl_acceso SET acceso_estado='activo' WHERE modulo_codigo = %s and usuario_codigo = %s"
        cursor.execute(query, (importante, valor))
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se ha Eliminado el acceso")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el Eliminado del acceso")
        
        cursor.close()
        conexion.close()

        ################################################################
        self.modelo = QStandardItemModel()
        self.ui.listaccesoreg.setModel(self.modelo)
        columnas = ["Codigo","Modulo"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT  m.modulo_codigo, m.modulo_nombre FROM tbl_acceso a INNER JOIN tbl_modulo m ON a.modulo_codigo = m.modulo_codigo WHERE a.usuario_codigo = %s AND a.acceso_estado = 'inactivo'"
        cursor.execute(consulta,valor)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()

        self.modelo2 = QStandardItemModel()
        self.ui.listaccesoenlis.setModel(self.modelo2)
        columnas = ["Codigo","Modulo"]
        self.modelo2.setHorizontalHeaderLabels(columnas)
        
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT m.modulo_codigo, m.modulo_nombre FROM tbl_acceso a INNER JOIN tbl_modulo m ON a.modulo_codigo = m.modulo_codigo WHERE a.usuario_codigo = %s AND a.acceso_estado = 'activo'"
        cursor.execute(consulta,valor)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo2.appendRow(fila)
        cursor.close()
        conexion.close()

        self.ui.listaccesoenlis.hideColumn(0)
        self.ui.listaccesoreg.hideColumn(0)

    def seleccionarfilader(self, index):
        fila = index.row()
        importante=self.modelo2.index(fila,0).data()
        module=self.modelo2.index(fila,1).data()
        valor=self.ui.cmbCodigoUsuario.currentText()

        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "UPDATE tbl_acceso SET acceso_estado='inactivo' WHERE modulo_codigo = %s and usuario_codigo = %s"
        cursor.execute(query, (importante,valor))
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se ha Agregado el acceso")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el agregado del acceso")
        
        cursor.close()
        conexion.close()
        ################################################################
        self.modelo = QStandardItemModel()
        self.ui.listaccesoreg.setModel(self.modelo)
        columnas = ["Codigo","Modulo"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT  m.modulo_codigo, m.modulo_nombre FROM tbl_acceso a INNER JOIN tbl_modulo m ON a.modulo_codigo = m.modulo_codigo WHERE a.usuario_codigo = %s AND a.acceso_estado = 'inactivo'"
        cursor.execute(consulta,valor)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()

        self.modelo2 = QStandardItemModel()
        self.ui.listaccesoenlis.setModel(self.modelo2)
        columnas = ["Codigo","Modulo"]
        self.modelo2.setHorizontalHeaderLabels(columnas)
        
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT m.modulo_codigo, m.modulo_nombre FROM tbl_acceso a INNER JOIN tbl_modulo m ON a.modulo_codigo = m.modulo_codigo WHERE a.usuario_codigo = %s AND a.acceso_estado = 'activo'"
        cursor.execute(consulta,valor)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo2.appendRow(fila)
        cursor.close()
        conexion.close()

        self.ui.listaccesoenlis.hideColumn(0)
        self.ui.listaccesoreg.hideColumn(0)
        

    def modulos(self):
        cursor=self.conexion.cursor()
        cursor.execute("SELECT u.usuario_codigo, u.usuario_nick, m.modulo_descrip FROM tbl_usuario u JOIN tbl_acceso a ON u.usuario_codigo = a.usuario_codigo JOIN tbl_modulo m ON a.modulo_codigo = m.modulo_codigo;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Accesousuarios()
    widget.show()
    sys.exit(app.exec())
