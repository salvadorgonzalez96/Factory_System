import sys
from datetime import date, datetime, time
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtSql import QSqlDatabase, QSqlQuery
from PySide6.QtCore import Qt
from PySide6 import QtWidgets
#from ui_empleados import Ui_MainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QAbstractItemModel
from Conexion import Conexion
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Empleados(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.ui.listempleados.clicked.connect(self.seleccionarfila)
        self.ui.listempleados.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.btnguardar.hide()
        self.ui.btnModificar2.hide()
        self.ui.btnEliminar2.hide()
        self.ui.btnrestaurar2.hide()
        self.ui.btnnuevo.clicked.connect(self.habilitarnuevo)
        self.ui.btnmodificar.clicked.connect(self.habilitarmodificar)

        self.modelo = QStandardItemModel()
        self.ui.listempleados.setModel(self.modelo)
        columnas = ["Codigo","Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido","Identidad","Fecha nacimiento", "Genero", "Estado Civil", "Cargo", "Tipo Contratacion"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT empleado_codigo,empleado_nombre, empleado_snombre, empleado_apellido, empleado_sapellido, empleado_id, empleado_fecha_nacimiento, empleado_genero, empleado_estado_civil, empleado_cargo, empleado_tipo_contratacion FROM tbl_empleado where empleado_estado like 'activo'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listempleados.setEnabled(False)
        self.ui.listempleados.hideColumn(0)
        

    def guardar(self):
        fecha_qdateedit = self.ui.fechanac.date()
        defectuoso=int(0)
        nacimiento = datetime(fecha_qdateedit.year(), fecha_qdateedit.month(), fecha_qdateedit.day())
        id=int(self.ui.txtid.text())
        pnombre=self.ui.txtpnombre.text()
        snombre=self.ui.txtsnombre.text()
        papellido=self.ui.txtpapellido.text()
        sapellido=self.ui.txtsapellido.text()
        cargo=self.ui.combocargo.currentText()
        estadocivil=self.ui.comboestadocivil.currentText()
        tipocon=self.ui.combotipocon.currentText()
        estado="activo"
        genero=""
        if self.ui.bgmasculino.isChecked():
            genero = "Masculino"
        elif self.ui.bgfemenino.isChecked():
            genero = "Femenino"
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "INSERT INTO tbl_empleado(empleado_codigo, empleado_nombre, empleado_snombre, empleado_apellido, empleado_sapellido, empleado_id, empleado_fecha_nacimiento, empleado_genero, empleado_estado_civil, empleado_cargo, empleado_tipo_contratacion, empleado_estado) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (defectuoso,pnombre,snombre,papellido,sapellido,id,nacimiento,genero,estadocivil,cargo,tipocon,estado))
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se han agregado el empleado")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el guardado del empleado")
        cursor.close()
        conexion.close()

        self.modelo = QStandardItemModel()
        self.ui.listempleados.setModel(self.modelo)
        columnas = ["Codigo","Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido","Identidad","Fecha nacimiento", "Genero", "Estado Civil", "Cargo", "Tipo Contratacion"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT empleado_codigo,empleado_nombre, empleado_snombre, empleado_apellido, empleado_sapellido, empleado_id, empleado_fecha_nacimiento, empleado_genero, empleado_estado_civil, empleado_cargo, empleado_tipo_contratacion FROM tbl_empleado where empleado_estado like 'activo'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listempleados.hideColumn(0)

    def modificar(self):
        fecha_qdateedit = self.ui.fechanac.date()
        codigo = self.ui.txtcodigo.text()
        nacimiento = datetime(fecha_qdateedit.year(), fecha_qdateedit.month(), fecha_qdateedit.day())
        id=int(self.ui.txtid.text())
        pnombre=self.ui.txtpnombre.text()
        snombre=self.ui.txtsnombre.text()
        papellido=self.ui.txtpapellido.text()
        sapellido=self.ui.txtsapellido.text()
        cargo=self.ui.combocargo.currentText()
        estadocivil=self.ui.comboestadocivil.currentText()
        tipocon=self.ui.combotipocon.currentText()
        #estado="activo"
        genero=""
        if self.ui.bgmasculino.isChecked():
            genero = "Masculino"
        elif self.ui.bgfemenino.isChecked():
            genero = "Femenino"
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "UPDATE tbl_empleado SET empleado_nombre=%s, empleado_snombre=%s, empleado_apellido=%s, empleado_sapellido=%s, empleado_id=%s, empleado_fecha_nacimiento=%s, empleado_genero=%s, empleado_estado_civil=%s, empleado_cargo=%s, empleado_tipo_contratacion=%s WHERE empleado_codigo = %s"
        cursor.execute(query, (pnombre,snombre,papellido,sapellido,id,nacimiento,genero,estadocivil,cargo,tipocon,codigo))
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se ha Modificado el empleado")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el modificado del empleado")
        cursor.close()
        conexion.close()

        self.modelo = QStandardItemModel()
        self.ui.listempleados.setModel(self.modelo)
        columnas = ["Codigo","Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido","Identidad","Fecha nacimiento", "Genero", "Estado Civil", "Cargo", "Tipo Contratacion"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT empleado_codigo,empleado_nombre, empleado_snombre, empleado_apellido, empleado_sapellido, empleado_id, empleado_fecha_nacimiento, empleado_genero, empleado_estado_civil, empleado_cargo, empleado_tipo_contratacion FROM tbl_empleado where empleado_estado like 'activo'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listempleados.hideColumn(0)

    def eliminar(self):
        codigo = self.ui.txtcodigo.text()
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "UPDATE tbl_empleado SET empleado_estado='inactivo' WHERE empleado_codigo = %s"
        cursor.execute(query, (codigo))
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se ha Eliminado el empleado")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el eliminado del empleado")
        cursor.close()
        conexion.close()

        self.modelo = QStandardItemModel()
        self.ui.listempleados.setModel(self.modelo)
        columnas = ["Codigo","Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido","Identidad","Fecha nacimiento", "Genero", "Estado Civil", "Cargo", "Tipo Contratacion"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT empleado_codigo,empleado_nombre, empleado_snombre, empleado_apellido, empleado_sapellido, empleado_id, empleado_fecha_nacimiento, empleado_genero, empleado_estado_civil, empleado_cargo, empleado_tipo_contratacion FROM tbl_empleado where empleado_estado like 'activo'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listempleados.hideColumn(0)

    def restaurar(self):
        codigo = self.ui.txtcodigo.text()
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "UPDATE tbl_empleado SET empleado_estado='activo' WHERE empleado_codigo = %s"
        cursor.execute(query, (codigo))
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se ha Restaurar el empleado")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el restauramiento del empleado")
        cursor.close()
        conexion.close()

        self.modelo = QStandardItemModel()
        self.ui.listempleados.setModel(self.modelo)
        columnas = ["Codigo","Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido","Identidad","Fecha nacimiento", "Genero", "Estado Civil", "Cargo", "Tipo Contratacion"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT empleado_codigo,empleado_nombre, empleado_snombre, empleado_apellido, empleado_sapellido, empleado_id, empleado_fecha_nacimiento, empleado_genero, empleado_estado_civil, empleado_cargo, empleado_tipo_contratacion FROM tbl_empleado where empleado_estado like 'inactivo'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listempleados.hideColumn(0)

    def habilitarnuevo(self):
        self.modelo = QStandardItemModel()
        self.ui.listempleados.setModel(self.modelo)
        columnas = ["Codigo","Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido","Identidad","Fecha nacimiento", "Genero", "Estado Civil", "Cargo", "Tipo Contratacion"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT empleado_codigo,empleado_nombre, empleado_snombre, empleado_apellido, empleado_sapellido, empleado_id, empleado_fecha_nacimiento, empleado_genero, empleado_estado_civil, empleado_cargo, empleado_tipo_contratacion FROM tbl_empleado where empleado_estado like 'activo'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listempleados.hideColumn(0)

        self.ui.btnnuevo.setEnabled(False)
        self.ui.btneliminar.setEnabled(True)
        self.ui.btnmodificar.setEnabled(True)
        self.ui.btnrestaurar.setEnabled(True)
        self.ui.btnModificar2.hide()
        self.ui.btnEliminar2.hide()
        self.ui.btnrestaurar2.hide()
        self.ui.btnguardar.setVisible(True)

        self.ui.txtid.setReadOnly(False)
        self.ui.txtpnombre.setReadOnly(False)
        self.ui.txtsnombre.setReadOnly(False)
        self.ui.txtpapellido.setReadOnly(False)
        self.ui.txtsapellido.setReadOnly(False)
        self.ui.fechanac.setEnabled(True)
        self.ui.bgmasculino.setEnabled(True)
        self.ui.bgfemenino.setEnabled(True)
        self.ui.combocargo.setEnabled(True)
        self.ui.comboestadocivil.setEnabled(True)
        self.ui.combotipocon.setEnabled(True)
        self.ui.listempleados.setEnabled(False)
        
    def habilitarmodificar(self):
        self.modelo = QStandardItemModel()
        self.ui.listempleados.setModel(self.modelo)
        columnas = ["Codigo","Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido","Identidad","Fecha nacimiento", "Genero", "Estado Civil", "Cargo", "Tipo Contratacion"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT empleado_codigo,empleado_nombre, empleado_snombre, empleado_apellido, empleado_sapellido, empleado_id, empleado_fecha_nacimiento, empleado_genero, empleado_estado_civil, empleado_cargo, empleado_tipo_contratacion FROM tbl_empleado where empleado_estado like 'activo'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listempleados.hideColumn(0)

        self.ui.btnnuevo.setEnabled(True)
        self.ui.btnguardar.hide()
        self.ui.btnEliminar2.hide()
        self.ui.btneliminar.setEnabled(True)
        self.ui.btnModificar2.setVisible(True)
        self.ui.btnmodificar.setEnabled(False)
        self.ui.btnrestaurar.setEnabled(True)
        self.ui.btnrestaurar2.hide()
        self.ui.txtid.setReadOnly(False)
        self.ui.txtpnombre.setReadOnly(False)
        self.ui.txtsnombre.setReadOnly(False)
        self.ui.txtpapellido.setReadOnly(False)
        self.ui.txtsapellido.setReadOnly(False)
        self.ui.fechanac.setEnabled(True)
        self.ui.bgmasculino.setEnabled(True)
        self.ui.bgfemenino.setEnabled(True)
        self.ui.combocargo.setEnabled(True)
        self.ui.comboestadocivil.setEnabled(True)
        self.ui.combotipocon.setEnabled(True)
        self.ui.listempleados.setEnabled(True)

    def habilitareliminar(self):
        self.modelo = QStandardItemModel()
        self.ui.listempleados.setModel(self.modelo)
        columnas = ["Codigo","Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido","Identidad","Fecha nacimiento", "Genero", "Estado Civil", "Cargo", "Tipo Contratacion"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT empleado_codigo,empleado_nombre, empleado_snombre, empleado_apellido, empleado_sapellido, empleado_id, empleado_fecha_nacimiento, empleado_genero, empleado_estado_civil, empleado_cargo, empleado_tipo_contratacion FROM tbl_empleado where empleado_estado like 'activo'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listempleados.hideColumn(0)
        self.ui.btnnuevo.setEnabled(True)
        self.ui.btnguardar.hide()
        self.ui.btnmodificar.setEnabled(True)
        self.ui.btnModificar2.hide()
        self.ui.btnEliminar2.setVisible(True)
        self.ui.btneliminar.setEnabled(False)
        self.ui.btnrestaurar.setEnabled(True)
        self.ui.btnrestaurar2.hide()
        self.ui.txtid.setReadOnly(True)
        self.ui.txtpnombre.setReadOnly(True)
        self.ui.txtsnombre.setReadOnly(True)
        self.ui.txtpapellido.setReadOnly(True)
        self.ui.txtsapellido.setReadOnly(True)
        self.ui.fechanac.setEnabled(False)
        self.ui.bgmasculino.setEnabled(False)
        self.ui.bgfemenino.setEnabled(False)
        self.ui.combocargo.setEnabled(False)
        self.ui.comboestadocivil.setEnabled(False)
        self.ui.combotipocon.setEnabled(False)
        self.ui.listempleados.setEnabled(True)
        
    def habilitarRestaurar(self):
        self.modelo = QStandardItemModel()
        self.ui.listempleados.setModel(self.modelo)
        columnas = ["Codigo","Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido","Identidad","Fecha nacimiento", "Genero", "Estado Civil", "Cargo", "Tipo Contratacion"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT empleado_codigo,empleado_nombre, empleado_snombre, empleado_apellido, empleado_sapellido, empleado_id, empleado_fecha_nacimiento, empleado_genero, empleado_estado_civil, empleado_cargo, empleado_tipo_contratacion FROM tbl_empleado where empleado_estado like 'inactivo'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listempleados.hideColumn(0)
        self.ui.btnnuevo.setEnabled(True)
        self.ui.btnguardar.hide()
        self.ui.btnmodificar.setEnabled(True)
        self.ui.btnModificar2.hide()
        self.ui.btnEliminar2.hide()
        self.ui.btneliminar.setEnabled(True)
        self.ui.btnrestaurar.setEnabled(False)
        self.ui.btnrestaurar2.setVisible(True)
        self.ui.txtid.setReadOnly(True)
        self.ui.txtpnombre.setReadOnly(True)
        self.ui.txtsnombre.setReadOnly(True)
        self.ui.txtpapellido.setReadOnly(True)
        self.ui.txtsapellido.setReadOnly(True)
        self.ui.fechanac.setEnabled(False)
        self.ui.bgmasculino.setEnabled(False)
        self.ui.bgfemenino.setEnabled(False)
        self.ui.combocargo.setEnabled(False)
        self.ui.comboestadocivil.setEnabled(False)
        self.ui.combotipocon.setEnabled(False)
        self.ui.listempleados.setEnabled(True)
        
    def seleccionarfila(self, index):

        fila = index.row()
        code=self.modelo.index(fila,0).data()
        id=self.modelo.index(fila,5).data()
        pnombre=self.modelo.index(fila,1).data()
        snombre=self.modelo.index(fila,2).data()
        papellido=self.modelo.index(fila,3).data()
        sapellido=self.modelo.index(fila,4).data()
        fechanaci=self.modelo.index(fila,6).data()
        genero=self.modelo.index(fila,7).data()
        if genero == "Masculino":
            self.ui.bgmasculino.setChecked(True)
            self.ui.bgfemenino.setChecked(False)
        elif genero == "Femenino":
            self.ui.bgmasculino.setChecked(False)
            self.ui.bgfemenino.setChecked(True)
        estadocivil = self.modelo.index(fila, 8).data()
        cargo = self.modelo.index(fila, 9).data()
        contra = self.modelo.index(fila, 10).data()

        self.ui.txtcodigo.setText(code)
        self.ui.txtid.setText(id)
        self.ui.txtpnombre.setText(pnombre)
        self.ui.txtsnombre.setText(snombre)
        self.ui.txtpapellido.setText(papellido)
        self.ui.txtsapellido.setText(sapellido)
        fecha_nacimiento = QDate.fromString(fechanaci, "yyyy-MM-dd")
        self.ui.fechanac.setDate(fecha_nacimiento)
        self.ui.comboestadocivil.setCurrentText(estadocivil)
        self.ui.combocargo.setCurrentText(cargo)
        self.ui.combotipocon.setCurrentText(contra)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Empleados()
    widget.show()
    sys.exit(app.exec())
