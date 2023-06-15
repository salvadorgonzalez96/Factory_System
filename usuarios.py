import sys
from PySide6 import QtWidgets
from ui_usuarios import Ui_MainWindow
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt, QAbstractItemModel
from PySide6.QtCore import Qt
from Conexion import Conexion
from accesousuarios import Accesousuarios
from utilidades import *

class Usuarios(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.ui.listaUsuarios.clicked.connect(self.seleccionarfila)
        self.ui.listaUsuarios.setEditTriggers(QAbstractItemView.NoEditTriggers) 
        self.ui.txtUsuario.setReadOnly(True)
        self.ui.txtClave.setReadOnly(True)
        self.ui.btnGuardar.hide()
        self.ui.btnEliminar2.hide()
        self.ui.btnmodificar2.hide()
        self.ui.btnRestaurar2.hide()
        self.ui.btnNuevo.clicked.connect(self.habilitarnuevo)
        self.ui.btnModificar.clicked.connect(self.habilitarmodificar)
        self.ui.btnEliminar.clicked.connect(self.habilitareliminar)
        self.ui.btnRestaurar.clicked.connect(self.habilitarestaurar)
        self.ui.btnLimpiar.clicked.connect(self.limpiarcampos)
        self.ui.btnAccesosU.clicked.connect(self.ingresoacceso)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        
        self.modelo = QStandardItemModel()
        self.ui.listaUsuarios.setModel(self.modelo)
        columnas = ["Codigo","Usuario","Clave","Estado"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT usuario_codigo,usuario_nick,usuario_clave,usuario_estado FROM tbl_usuario where usuario_estado ='habilitado'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listaUsuarios.hideColumn(0)
        self.ui.listaUsuarios.hideColumn(2)

        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT concat(empleado_nombre,' ',empleado_snombre,' ',empleado_apellido,' ',empleado_sapellido) as nombrec, empleado_codigo FROM tbl_empleado"
        cursor.execute(consulta)
        resultado = cursor.fetchall()
        self.ui.comboempleado.clear()
        self.ui.comboempleado.addItem("Seleccione un Empleado")
        self.ui.comboCodigoEmpleado.clear()
        self.ui.comboCodigoEmpleado.addItem("Seleccione un Empleado")
        for row in resultado:
            codigo = str(row["empleado_codigo"])
            self.ui.comboempleado.addItem(row["nombrec"], userData = row)
            self.ui.comboCodigoEmpleado.addItem(codigo, userData = row)
        cursor.close()
        conexion.close()

    def guardar(self):
        #code = self.ui.txtcodigo.text()
        code = int(0)
        user = self.ui.txtUsuario.text()
        password = self.ui.txtClave.text()
        index = self.ui.comboempleado.currentIndex()
        name=self.ui.comboempleado.currentText()
        self.ui.comboCodigoEmpleado.setCurrentIndex(index)
        valor=self.ui.comboCodigoEmpleado.currentText()
        #print("Dato:"+valor)
        
        estado = "habilitado"
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "INSERT INTO tbl_usuario(usuario_codigo, usuario_nick, usuario_clave, usuario_estado) VALUES (%s,%s, %s, %s)"
        cursor.execute(query, (code,user,password,estado))
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se han agregado el empleado")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el guardado del empleado")
        cursor.close()
        conexion.close()

        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "select usuario_codigo from tbl_usuario where usuario_estado='habilitado' order by usuario_codigo desc limit 1"
        cursor.execute(query)
        resultado = cursor.fetchall()
        codigo = ""
        for row in resultado:
            codigo = str(row["usuario_codigo"])
        cursor.close()
        conexion.close()

        state_vendor = "activo"
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "INSERT INTO tbl_vendedor(vendedor_codigo, vendedor_nombre, usuario_codigo, empleado_codigo, vendedor_estado) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(query, (code,name,codigo,valor,state_vendor))
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se han agregado el vendedor")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el guardado del vendedor")
        cursor.close()
        conexion.close()

        self.modelo = QStandardItemModel()
        self.ui.listaUsuarios.setModel(self.modelo)
        columnas = ["Codigo","Usuario","Clave","Estado"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT usuario_codigo,usuario_nick,usuario_clave,usuario_estado FROM tbl_usuario where usuario_estado ='habilitado'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listaUsuarios.hideColumn(0)
        self.ui.listaUsuarios.hideColumn(2)

        
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "select usuario_codigo from tbl_usuario where usuario_estado='habilitado' order by usuario_codigo desc limit 1"
        cursor.execute(query)
        resultado = cursor.fetchall()
        codigo = ""
        for row in resultado:
            codigo = str(row["usuario_codigo"])
        cursor.close()
        conexion.close()

        state_vendor = "activo"
        conexion = Conexion().getConexion()
        conexion2 = Conexion().getConexion()
        cursor = conexion.cursor()
        cursor2 = conexion2.cursor()
        query = "select modulo_codigo from tbl_modulo"
        cursor.execute(query)
        resultado = cursor.fetchall()
        #resultado2 = cursor2.fetchall()
        modulo = ""
        for row in resultado:
            modulo = str(row["modulo_codigo"])

            query2 = "INSERT INTO tbl_acceso(usuario_codigo, modulo_codigo, acceso_estado) VALUES (%s,%s,%s)"
            cursor2.execute(query2, (codigo,modulo,state_vendor))
            conexion2.commit()
            print(codigo+" "+modulo+" "+state_vendor)

        cursor.close()
        cursor2.close()
        
        conexion.close()
        conexion2.close()

    def eliminar(self):
        codigo = self.ui.txtcodigo.text()
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "UPDATE tbl_usuario SET usuario_estado='deshabilitado' WHERE usuario_codigo = %s"
        cursor.execute(query, (codigo))
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se ha Eliminado el usuario")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el eliminado del usuario")
        cursor.close()
        conexion.close()

        self.modelo = QStandardItemModel()
        self.ui.listaUsuarios.setModel(self.modelo)
        columnas = ["Codigo","Usuario","Clave","Estado"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT usuario_codigo,usuario_nick,usuario_clave,usuario_estado FROM tbl_usuario where usuario_estado ='habilitado'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listaUsuarios.hideColumn(0)
        self.ui.listaUsuarios.hideColumn(2)

    def restaurar(self):
        codigo = self.ui.txtcodigo.text()
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        query = "UPDATE tbl_usuario SET usuario_estado='activo' WHERE usuario_codigo = %s"
        cursor.execute(query, (codigo))
        conexion.commit()
        if conexion.commit() is None:
            QtWidgets.QMessageBox.information(None, "Mensaje","Se ha Restaurar el usuario")
        else:
            QtWidgets.QMessageBox.critical(None, "Error", "No se esta cumpliendo el restauramiento del usuario")
        cursor.close()
        conexion.close()

        self.modelo = QStandardItemModel()
        self.ui.listaUsuarios.setModel(self.modelo)
        columnas = ["usuario", "estado"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT usuario_nick,usuario_estado FROM tbl_usuario where usuario_estado ='deshabilitado'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
    
    def habilitarnuevo(self):
        self.ui.btnNuevo.setEnabled(False)
        self.ui.btnModificar.setEnabled(True)
        self.ui.btnEliminar.setEnabled(True)
        self.ui.btnRestaurar.setEnabled(True)

        self.ui.btnEliminar2.hide()
        self.ui.btnmodificar2.hide()
        self.ui.btnRestaurar2.hide()
        self.ui.btnGuardar.setVisible(True)
        self.ui.txtUsuario.setReadOnly(False)
        self.ui.txtClave.setReadOnly(False)
        
        self.modelo = QStandardItemModel()
        self.ui.listaUsuarios.setModel(self.modelo)
        columnas = ["Codigo","Usuario","Clave","Estado"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT usuario_codigo,usuario_nick,usuario_clave,usuario_estado FROM tbl_usuario where usuario_estado ='habilitado'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listaUsuarios.hideColumn(0)
        self.ui.listaUsuarios.hideColumn(2)

    def habilitarmodificar(self):
        self.ui.btnNuevo.setEnabled(True)
        self.ui.btnModificar.setEnabled(False)
        self.ui.btnEliminar.setEnabled(True)
        self.ui.btnRestaurar.setEnabled(True)

        self.ui.btnEliminar2.hide()
        self.ui.btnmodificar2.setVisible(True)
        self.ui.btnRestaurar2.hide()
        self.ui.btnGuardar.hide()
        self.ui.txtUsuario.setReadOnly(False)
        self.ui.txtClave.setReadOnly(False)

        self.modelo = QStandardItemModel()
        self.ui.listaUsuarios.setModel(self.modelo)
        columnas = ["Codigo","Usuario","Clave","Estado"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT usuario_codigo,usuario_nick,usuario_clave,usuario_estado FROM tbl_usuario where usuario_estado ='habilitado'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listaUsuarios.hideColumn(0)
        self.ui.listaUsuarios.hideColumn(2)
    
    def habilitareliminar(self):
        self.ui.btnNuevo.setEnabled(True)
        self.ui.btnModificar.setEnabled(True)
        self.ui.btnEliminar.setEnabled(False)
        self.ui.btnRestaurar.setEnabled(True)

        self.ui.btnEliminar2.setVisible(True)
        self.ui.btnmodificar2.hide()
        self.ui.btnGuardar.hide()
        self.ui.btnRestaurar2.hide()
        self.ui.txtUsuario.setReadOnly(True)
        self.ui.txtClave.setReadOnly(True)

        self.modelo = QStandardItemModel()
        self.ui.listaUsuarios.setModel(self.modelo)
        columnas = ["Codigo","Usuario","Clave","Estado"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT usuario_codigo,usuario_nick,usuario_clave,usuario_estado FROM tbl_usuario where usuario_estado ='habilitado'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()
        self.ui.listaUsuarios.hideColumn(0)
        self.ui.listaUsuarios.hideColumn(2)

    def habilitarestaurar(self):
        self.modelo = QStandardItemModel()
        self.ui.listaUsuarios.setModel(self.modelo)
        columnas = ["usuario", "estado"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT usuario_nick,usuario_estado FROM tbl_usuario where usuario_estado ='deshabilitado'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        cursor.close()
        conexion.close()

        self.ui.btnNuevo.setEnabled(True)
        self.ui.btnModificar.setEnabled(True)
        self.ui.btnEliminar.setEnabled(True)
        self.ui.btnRestaurar.setEnabled(False)

        self.ui.btnmodificar2.hide()
        self.ui.btnGuardar.hide()
        self.ui.btnEliminar2.hide()
        self.ui.btnRestaurar2.setVisible(True)
        self.ui.txtUsuario.setReadOnly(True)
        self.ui.txtClave.setReadOnly(True)

    def seleccionarfila(self, index):
        fila = index.row()
        codigo=self.modelo.index(fila,0).data()
        usuario=self.modelo.index(fila,1).data()
        contra=self.modelo.index(fila,2).data()
        estado=self.modelo.index(fila,3).data()
        
        self.ui.txtcodigo.setText(codigo)
        self.ui.txtUsuario.setText(usuario)
        self.ui.txtClave.setText(contra)
        #self.ui.comboempleado.activated(contra)
        #self.ui.comboempleado.activated[index].connect(self.mostrarMensaje)
                                                       
    def mostrarMensaje(self, int):
        QMessageBox.information(self, "Selección", f"Seleccionaste: {int}")

    def limpiarcampos(self):
        self.ui.txtUsuario.clear()
        self.ui.txtClave.clear()

    def ingresoacceso(self):
        self.close()
        widget= Accesousuarios()
        widget.show()
        widget.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Usuarios()
    widget.show()
    sys.exit(app.exec())