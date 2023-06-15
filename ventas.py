# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from ui_ventas import Ui_MainWindow
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
        self.ui.listaclientes.clicked.connect(self.seleccionarfila)
        self.ui.listaproductosinv.clicked.connect(self.seleccionarProducto)
        self.ui.btnagregar.clicked.connect(self.guardarProductoEnTabla)
        self.ui.btnvender.clicked.connect(self.registrarVenta)

        self.modelo3 = QStandardItemModel()
        self.modelo4 = QStandardItemModel()
        self.ui.listaproductosfac.setModel(self.modelo3)
        self.ui.listaproductosfac.clicked.connect(self.seleccionarfila2)
        columnas = ["codigo", "descripcion", "cantidad", "peso", "precio", "impuesto", "descuento"]
        self.ui.listaproductosinv.setModel(self.modelo4)
        self.modelo3.setHorizontalHeaderLabels(columnas)
        #self.total = 0

        # Restringir el tamaño de la ventana al tamaño actual
        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.ui.listaclientes.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.listaproductosinv.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        
        self.modelo2 = QStandardItemModel()
        self.ui.listaproductosinv.setModel(self.modelo2)
        
        columnas = ["codigo","descripcion","cantidad","peso", "precio venta", "impuesto", "descuento"]
        self.modelo2.setHorizontalHeaderLabels(columnas)
        self.modelo4.setHorizontalHeaderLabels(columnas)
        # Obtener la conexión a la base de datos
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        # Ejecutar la consulta
        consultap = """SELECT p.producto_codigo, p.producto_descripcion, p.producto_stock, p.producto_peso, 
        p.producto_precio_venta, i.impuesto_valor,p.producto_descuento FROM tbl_producto p 
        JOIN tbl_impuesto i ON p.impuesto_codigo = i.impueto_codigo;"""
        cursor.execute(consultap)
        # Llenar el modelo con los datos obtenidos
        for fila_datos in cursor:
            # Crear una fila en el modelo
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo2.appendRow(fila)
        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()

        self.modelo = QStandardItemModel()
        self.ui.listaclientes.setModel(self.modelo)
        # Establecer encabezados de columnas
        columnas = ["nombre", "RTN", "direccion", "tel", "email"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        # Obtener la conexión a la base de datos
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        # Ejecutar la consulta
        consulta = "SELECT c.cliente_nombre, c.cliente_rtn, c.cliente_direccion, cc.cliente_contacto_telefono, cc.cliente_contacto_email FROM tbl_cliente c JOIN tbl_cliente_contacto cc ON c.cliente_codigo = cc.cliente_codigo;"
        cursor.execute(consulta)
        # Llenar el modelo con los datos obtenidos
        for fila_datos in cursor:
            # Crear una fila en el modelo
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()

    #Funcion de Seleccion de Clientes
    def seleccionarfila2(self, index):
        # Obtener la fila seleccionada
        fila = index.row()
        codigo = self.modelo4.index(fila, 0).data()
        descripcion = self.modelo4.index(fila, 1).data()
        cantidad = self.modelo4.index(fila, 2).data()
        peso = self.modelo4.index(fila, 3).data()
        precio = self.modelo4.index(fila, 4).data()
        impuesto = self.modelo4.index(fila, 5).data()
        descuento = self.modelo4.index(fila, 6).data()

        # Establecer los valores en los campos correspondientes
        # self.ui.txtnombrecli.setText(nombre)
        # self.ui.txtrtnclien.setText(rtn)
        # self.ui.txtdireccioncli.setText(direccion)
        # self.ui.txttelefonocli.setText(telefono)
        # self.ui.txtemailcli.setText(email)

    def seleccionarfila(self, index):
        # Obtener la fila seleccionada
        fila = index.row()
        nombre = self.modelo.index(fila, 0).data()
        rtn = self.modelo.index(fila, 1).data()
        direccion = self.modelo.index(fila, 2).data()
        telefono = self.modelo.index(fila, 3).data()
        email = self.modelo.index(fila, 4).data()

        # Establecer los valores en los campos correspondientes
        self.ui.txtnombrecli.setText(nombre)
        self.ui.txtrtnclien.setText(rtn)
        self.ui.txtdireccioncli.setText(direccion)
        self.ui.txttelefonocli.setText(telefono)
        self.ui.txtemailcli.setText(email)
        
    def buscarproducto(self):
        
        texto_busqueda = self.ui.txtbuscarpro.text()

        self.modelo.removeRows(0, self.modelo.rowCount())


        conexion = Conexion().getConexion()
        cursor = conexion.cursor()


        consulta = f"SELECT * FROM vista_det_productos WHERE producto_descripcion LIKE '%{texto_busqueda}%'"
        cursor.execute(consulta)
        for fila_datos in cursor:
            
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)

        
        cursor.close()
        conexion.close()
        #Funcion de Seleccinar Productos
    def seleccionarProducto(self, index):
        # Obtener la fila seleccionada
        filap = index.row()
        nombrep = self.modelo2.index(filap, 1).data()
        codigo = self.modelo2.index(filap, 0).data()
        peso = self.modelo2.index(filap, 3).data()
        precio = self.modelo2.index(filap, 4).data()
        impuesto = self.modelo2.index(filap, 5).data()
        descuento = self.modelo2.index(filap, 6).data()
        cantidad = self.modelo2.index(filap, 7).data()

        #Establecer los valores en los campos correspondientes
        self.ui.txtnombrepro.setText(nombrep)
        self.ui.txtcodigo.setText(codigo)
        #self.ui.txtcantidad.setText(cantidad)
        self.ui.txtpeso.setText(peso)
        self.ui.txtprecio.setText(precio)
        self.ui.txtisv.setText(impuesto)
        self.ui.txtdescuento.setText(descuento)
        self.ui.txtcantidad.setText(cantidad)
            
     #######################################################
    
    def calcularTotales(self):
        totalGeneral = 0
        subtotalGeneral = 0
        descuentoGeneral = 0
        impuestoGeneral = 0
        model = self.ui.listaproductosfac.model()
        # ["codigo", "descripcion", "cantidad", "peso", "precio", "impuesto", "descuento"]
        
        for x in range(model.rowCount()) :
            try:
                cantidad = float(str(model.data(model.index(x, 2))))
                precio = float(str(model.data(model.index(x, 4))))
                impuesto = float(str(model.data(model.index(x, 5))))
                subtotal = (cantidad * precio)
                descuento =  subtotal * float(str(model.data(model.index(x, 6))))

                descuentoGeneral += descuento
                subtotalGeneral += subtotal
                impuestoGeneral += subtotal * impuesto
                totalGeneral += subtotal - descuento
            except:
                print("Indice fuera de rango")

        self.ui.txttotal.setText(str(totalGeneral))
        self.ui.txtsubtotal.setText(str(subtotalGeneral))
        self.ui.txtdescuento.setText(str(descuentoGeneral))
        self.ui.txtisv.setText(str(impuestoGeneral))


    def guardarProductoEnTabla(self):


        # for index in self.ui.listaproductosfac:
            # descripcion = self.modelo4.index(index, 2).data()
            # print(index)
            
        # print("Funcion")
        codigo = self.ui.txtcodigo.text()
        descripcion = self.ui.txtnombrepro.text()
        cantidad_texto = self.ui.txtcantidad.text()
        peso = self.ui.txtpeso.text()
        precio =self.ui.txtprecio.text()
        impuesto = self.ui.txtisv.text()
        descuento =self.ui.txtdescuento.text()
        
        if cantidad_texto.isnumeric():
            cantidad = int(cantidad_texto)
            print(str(cantidad))
            if cantidad > 0:
              conexion = Conexion().getConexion()
              cursor = conexion.cursor()

              producto_stock = str(codigo)
              
              cursor.execute("SELECT producto_stock FROM tbl_producto WHERE producto_codigo = %s", [int(producto_stock)])
            #   print(cursor.fetchall())
              producto_stock = cursor.fetchone()
              x = producto_stock["producto_stock"]
            #   print(x)
              if cantidad <= x:
                # cursor.execute("UPDATE tbl_producto SET producto_stock = ? WHERE id = ?", (producto_stock,cantidad))
                # conexion.commit()
                # conexion.close()
                # QMessageBox.information(self, "Éxito", "Producto actualizado en la base de datos")
                rowf = self.modelo3.rowCount()
                self.modelo3.insertRow(rowf)
                self.modelo3.setData(self.modelo3.index(rowf, 0), codigo)
                self.modelo3.setData(self.modelo3.index(rowf, 1), descripcion)
                self.modelo3.setData(self.modelo3.index(rowf, 2), cantidad)
                self.modelo3.setData(self.modelo3.index(rowf, 3), peso)
                self.modelo3.setData(self.modelo3.index(rowf, 4), precio)
                self.modelo3.setData(self.modelo3.index(rowf, 5), impuesto)
                self.modelo3.setData(self.modelo3.index(rowf, 6), descuento)
                # Agregar la fila a la tabla
                filaf = [QStandardItem(str(codigo)), QStandardItem(descripcion), QStandardItem(str(cantidad)),
                    QStandardItem(str(peso)), QStandardItem(str(precio)), QStandardItem(str(impuesto)),
                    QStandardItem(str(descuento))]

                self.ui.txtnombrepro.clear()
                self.ui.txtcodigo.clear()
                self.ui.txtcantidad.clear()
                self.ui.txtpeso.clear()
                self.ui.txtprecio.clear()
                self.ui.txtdescuento.clear()
                model = self.ui.listaproductosfac.model()
                for index in range(model.rowCount()):
                    item = model.item(index)
                    print(item.data())
                
                self.calcularTotales()

              else:
                   QMessageBox.warning(self, "Error", "La cantidad ingresada es mayor al stock actual del producto")
            else:
                QMessageBox.warning(self, "Error", "La cantidad debe ser mayor a cero")
        else:
            QMessageBox.warning(self, "Error", "La cantidad debe ser un número entero positivo") 
            
         


        #if cantidad <= 0:
        # raise ValueError("La cantidad ingresada debe ser mayor que cero")

        #if cantidad > cantidad_texto:
        # raise ValueError("La cantidad ingresada es mayor que la cantidad actual en la base de datos")
        
        #total = (cantidad * precio) - descuento
        #total_con_impuesto = total * (1 + impuesto / 100)

    def registrarVenta(self) :
        if self.ui.listaproductosfac.model().rowCount() > 0 :
            if self.ui.radiocontaefec.isChecked() or self.ui.radiocontatar.isChecked() or self.ui.radiocredito.isChecked() : 
                conexion = Conexion().getConexion()
                cursor = conexion.cursor()
                # Ejecutar la consulta
                consulta = "SELECT config_correlativo_factura FROM tbl_config limit 1"
                cursor.execute(consulta)

                codigo = str("000")
                correlativo = str(cursor.fetchall()[0]["config_correlativo_factura"])

                codigo = "FAC-" + codigo[0 : len(codigo) - len(correlativo)] + correlativo
                cursor.execute("UPDATE tbl_config SET config_correlativo_factura = config_correlativo_factura + 1 WHERE config_codigo = '1'")
                
                referencia = 'Contado'
                formaPago = 'Efectivo'
                if self.ui.radiocredito.isChecked() :
                    referencia = 'Credito'
                elif self.ui.radiocontatar.isChecked() :
                    formaPago = 'Tarjeta'

                cursor.execute("INSERT INTO tbl_transacciones (transacciones_codigo, transacciones_fecha, transacciones_cliente, transacciones_total, transacciones_referencia, transacciones_tipo_pago, transacciones_estado) VALUES ('" + codigo + "', current_timestamp(), '" + self.ui.txtrtnclien.text() + "', '" + self.ui.txttotal.text() + "', '" + referencia + "', '" + formaPago + "', 'Cancelado')")

                model = self.ui.listaproductosfac.model()
                for x in range(model.rowCount()) :
                    codigoProducto = str(model.data(model.index(x, 0)))
                    cantidad = float(str(model.data(model.index(x, 2))))
                    precio = float(str(model.data(model.index(x, 4))))
                    subtotal = cantidad * precio
                    impuesto = subtotal * float(str(model.data(model.index(x, 5))))
                    descuento = subtotal - subtotal*float(str(model.data(model.index(x, 6))))
                    total = subtotal - descuento
                    
                    cursor.execute("INSERT INTO tbl_transaccion_detalle (transacciones_codigo, transaccion_detalle_posicion, producto_codigo, transaccion_detalle_resta_unidad, transaccion_detalle_cantidad, transaccion_detalle_total_unidad, transaccion_detalle_total, transaccion_detalle_isv, transaccion_detalle_desc) VALUES ('" + codigo + "', '" + str(x) + "', '" + codigoProducto + "', '" + str(cantidad * -1) + "', '" + str(cantidad) + "', '" + str(precio) + "', '" + str(total) + "', '" + str(impuesto) + "', '" + str(descuento) + "')")
                    cursor.execute("UPDATE tbl_producto SET producto_stock = producto_stock - " + str(cantidad) + " WHERE producto_codigo = '" + codigoProducto + "'")
                conexion.commit()


                self.ui.txtbuscarcli.setText('')
                self.ui.txtnombrecli.setText('')
                self.ui.txtrtnclien.setText('')
                self.ui.txtdireccioncli.setText('')
                self.ui.txttelefonocli.setText('')
                self.ui.txtemailcli.setText('')

                self.ui.txtsubtotal.setText('')
                self.ui.txtisv.setText('')
                self.ui.txtdescuento.setText('')
                self.ui.txttotal.setText('')
                
                for x in range(self.ui.listaproductosfac.model().rowCount()) :
                    self.ui.listaproductosfac.model().removeRow(x)

                for x in range(self.ui.listaproductosinv.model().rowCount()) :
                    self.ui.listaproductosinv.model().removeRow(x)

                #consultap = """SELECT p.producto_codigo, p.producto_descripcion, p.producto_stock, p.producto_peso, 
                #    p.producto_precio_venta, i.impuesto_valor,p.producto_descuento FROM tbl_producto p 
                #    JOIN tbl_impuesto i ON p.impuesto_codigo = i.impueto_codigo;"""

                #cursor.execute(consultap)
                #for fila_datos in cursor:
                #    fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
                #    self.modelo2.appendRow(fila)

                cursor.close()
                conexion.close()
                QMessageBox.about(self, "Exito", "Venta registrada satisfactoriamente.")
            else :
                QMessageBox.warning(self, "Error", "Seleccione un tipo de pago.")
        else :
            QMessageBox.warning(self, "Error", "No hay detalles seleccionados.")
       
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Ventas()
    widget.show()
    sys.exit(app.exec())
