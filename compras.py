# This Python file uses the following encoding: utf-8
import sys
from tkinter import messagebox

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtWidgets
from ui_compras import Ui_MainWindow
from Conexion import Conexion
from PySide6.QtSql import QSqlQuery
from PySide6.QtWidgets import QListView, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel


class Compras(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        # Restringir el tamaño de la ventana al tamaño actual
        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.llenarproductos()
        self.llenarproveedores()
        self.cargarCatergias()
        self.cargarImpuestos()
        self.cargarDescuentos()
        self.ui.txtproveedor.setReadOnly(True)
        self.ui.txtrtn.setReadOnly(True)
        self.ui.btnagregar.clicked.connect(self.guardarProductoEnTabla)
        self.ui.btnComprar.clicked.connect(self.registrarCompra)
        self.ui.txtbuscarpro.textChanged.connect(self.buscarproducto)
        self.ui.listaproveedores.clicked.connect(self.seleccionarfilaprovee)
        self.ui.listaproductosinv.clicked.connect(self.seleccionarfilaprod)
        self.ui.listaproveedores.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.listaproductosinv.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.listaproductosfac.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        columnas = ["codigo","descripcion","cantidad","peso", "precio venta", "impuesto", "descuento"]
        self.modeloDetalle = QStandardItemModel()
        self.modeloDetalle.setHorizontalHeaderLabels(columnas)
        self.ui.listaproductosfac.setModel(self.modeloDetalle)

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

    def llenarproductos(self):
        self.modelo = QStandardItemModel()
        self.ui.listaproductosinv.setModel(self.modelo)
        columnas = ["codigo", "codigobarra","descripcion","stock","peso","precio costo", "precio venta", "categoria", "impuesto", "proveedor","ganancia", "descuento"]
        self.modelo.setHorizontalHeaderLabels(columnas)
        # Obtener la conexión a la base de datos
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        # Ejecutar la consulta
        consulta = "SELECT producto_codigo, producto_codigobarra, producto_descripcion, producto_stock, producto_peso, producto_precio_costo, producto_precio_venta, categoria_codigo, impuesto_codigo, proveedor_codigo, producto_ganancia, producto_descuento FROM tbl_producto"
        cursor.execute(consulta)
        # Llenar el modelo con los datos obtenidos
        for fila_datos in cursor:
            # Crear una fila en el modelo
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)
        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()
        
    def llenarproveedores(self):
        self.modelo2 = QStandardItemModel()
        self.ui.listaproveedores.setModel(self.modelo2)
        # Establecer encabezados de columnas
        columnas = ["Codigo","Nombre", "RTN"]
        self.modelo2.setHorizontalHeaderLabels(columnas)
        # Obtener la conexión a la base de datos
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        # Ejecutar la consulta
        consulta = "SELECT proveedor_codigo,proveedor_nombre,proveedor_rtn from tbl_proveedor"
        cursor.execute(consulta)
        # Llenar el modelo con los datos obtenidos
        for fila_datos in cursor:
            # Crear una fila en el modelo
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo2.appendRow(fila)
        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()

    def cargarCatergias(self):
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT categoria_codigo, categoria_nombre from tbl_categoria"
        cursor.execute(consulta)
        for fila_datos in cursor:
            self.ui.cmbCategoria.addItem(str(fila_datos["categoria_nombre"]), fila_datos)
        cursor.close()
        conexion.close()

    def cargarImpuestos(self):
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()
        consulta = "SELECT impueto_codigo, impuesto_descripcion, impuesto_valor from tbl_impuesto"
        cursor.execute(consulta)
        for fila_datos in cursor:
            self.ui.cmbImpuesto.addItem(str(fila_datos["impuesto_descripcion"]), fila_datos)
        cursor.close()
        conexion.close()

    def cargarDescuentos(self):
        self.ui.cmbDescuento.addItem("0%", 0)
        self.ui.cmbDescuento.addItem("3%", 0.03)
        self.ui.cmbDescuento.addItem("5%", 0.05)
        self.ui.cmbDescuento.addItem("10%", 0.1)
                                                  
    def seleccionarfilaprovee(self, index):
        fila = index.row()        
        nombre=self.modelo2.index(fila,1).data()
        rtn=self.modelo2.index(fila,2).data()       
        self.ui.txtproveedor.setText(nombre)
        self.ui.txtrtn.setText(rtn)   

    def seleccionarfilaprod(self,index):
        fila =index.row()
        nombrepro=self.modelo.index(fila,2).data()
        codigopro=self.modelo.index(fila,1).data()
        peso=self.modelo.index(fila,4).data()
        precio=self.modelo.index(fila,6).data()
        self.ui.txtcodigo.setText(codigopro)
        self.ui.txtnombrepro.setText(nombrepro)
        self.ui.txtpeso.setText(peso)
        self.ui.txtprecio.setText(precio)

    def guardarProductoEnTabla(self):
        codigo = self.ui.txtcodigo.text()
        descripcion = self.ui.txtnombrepro.text()
        cantidad_texto = self.ui.txtcantidad.text()
        peso = self.ui.txtpeso.text()
        precio =self.ui.txtprecio.text()
        impuesto = str(self.ui.cmbImpuesto.itemData(self.ui.cmbImpuesto.currentIndex())["impuesto_valor"])
        descuento = str(self.ui.cmbDescuento.itemData(self.ui.cmbDescuento.currentIndex()))
        #categoria = self.ui.cmbCategoria.itemData(self.ui.cmbCategoria.currentIndex())
        if cantidad_texto.isnumeric():
            cantidad = int(cantidad_texto)
            print(str(cantidad))
            if cantidad > 0:
                rowf = self.modeloDetalle.rowCount()
                self.modeloDetalle.insertRow(rowf)
                self.modeloDetalle.setData(self.modeloDetalle.index(rowf, 0), codigo)
                self.modeloDetalle.setData(self.modeloDetalle.index(rowf, 1), descripcion)
                self.modeloDetalle.setData(self.modeloDetalle.index(rowf, 2), cantidad)
                self.modeloDetalle.setData(self.modeloDetalle.index(rowf, 3), peso)
                self.modeloDetalle.setData(self.modeloDetalle.index(rowf, 4), precio)
                self.modeloDetalle.setData(self.modeloDetalle.index(rowf, 5), impuesto)
                self.modeloDetalle.setData(self.modeloDetalle.index(rowf, 6), descuento)
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
                self.ui.cmbImpuesto.setCurrentIndex(0)
                self.ui.cmbCategoria.setCurrentIndex(0)
                self.ui.cmbDescuento.setCurrentIndex(0)
                for index in range(self.modeloDetalle.rowCount()):
                    item = self.modeloDetalle.item(index)
                    print(item.data())

                self.calcularTotales()
            else:
                QMessageBox.warning(self, "Error", "La cantidad debe ser mayor a cero")
        else:
            QMessageBox.warning(self, "Error", "La cantidad debe ser un número entero positivo") 

    def calcularTotales(self):
        totalGeneral = 0
        subtotalGeneral = 0
        descuentoGeneral = 0
        impuestoGeneral = 0
        model = self.modeloDetalle
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

    def registrarCompra(self) :
        if self.ui.listaproductosfac.model().rowCount() > 0 :
            if len(self.ui.listaproveedores.selectedIndexes()) > 0 and (self.ui.radiocontaefec.isChecked() or self.ui.radiocontatar.isChecked() or self.ui.radiocredito.isChecked()) : 
                conexion = Conexion().getConexion()
                cursor = conexion.cursor()
                # Ejecutar la consulta
                consulta = "SELECT config_correlativo_compra FROM tbl_config limit 1"
                cursor.execute(consulta)

                codigo = str("000")
                correlativo = str(cursor.fetchall()[0]["config_correlativo_compra"])

                codigo = "COM-" + codigo[0 : len(codigo) - len(correlativo)] + correlativo
                cursor.execute("UPDATE tbl_config SET config_correlativo_compra = config_correlativo_compra + 1 WHERE config_codigo = '1'")
                
                referencia = 'Contado'
                formaPago = 'Efectivo'
                if self.ui.radiocredito.isChecked() :
                    referencia = 'Credito'
                elif self.ui.radiocontatar.isChecked() :
                    formaPago = 'Tarjeta'

                cursor.execute("INSERT INTO tbl_transacciones (transacciones_codigo, transacciones_fecha, transacciones_cliente, transacciones_total, transacciones_referencia, transacciones_tipo_pago, transacciones_estado) VALUES ('" + codigo + "', current_timestamp(), '" + self.ui.txtrtn.text() + "', '" + self.ui.txttotal.text() + "', '" + referencia + "', '" + formaPago + "', 'Cancelado')")
                
                cursor.execute("SELECT proveedor_codigo FROM tbl_proveedor WHERE proveedor_rtn = '" + self.ui.txtrtn.text() + "'")
                cursor.execute("INSERT INTO tbl_transaccion_proveedor (transacciones_codigo, proveedor_codigo) VALUES ('" + codigo + "', '" + str(cursor.fetchall()[0]["proveedor_codigo"]) + "')")

                model = self.modeloDetalle
                for x in range(model.rowCount()) :
                    consulta = "SELECT producto_codigo FROM tbl_producto WHERE producto_codigobarra = '" + str(model.data(model.index(x, 0))) + "'"
                    cursor.execute(consulta)
                    
                    codigoProducto = str(cursor.fetchall()[0]["producto_codigo"])
                    cantidad = float(str(model.data(model.index(x, 2))))
                    precio = float(str(model.data(model.index(x, 4))))
                    subtotal = cantidad * precio
                    impuesto = subtotal * float(str(model.data(model.index(x, 5))))
                    descuento = subtotal - subtotal*float(str(model.data(model.index(x, 6))))
                    total = subtotal - descuento
                    
                    cursor.execute("INSERT INTO tbl_transaccion_detalle (transacciones_codigo, transaccion_detalle_posicion, producto_codigo, transaccion_detalle_resta_unidad, transaccion_detalle_cantidad, transaccion_detalle_total_unidad, transaccion_detalle_total, transaccion_detalle_isv, transaccion_detalle_desc) VALUES ('" + codigo + "', '" + str(x) + "', '" + codigoProducto + "', '" + str(cantidad * -1) + "', '" + str(cantidad) + "', '" + str(precio) + "', '" + str(total) + "', '" + str(impuesto) + "', '" + str(descuento) + "')")
                    cursor.execute("UPDATE tbl_producto SET producto_stock = producto_stock + " + str(cantidad) + " WHERE producto_codigo = '" + str(codigoProducto) + "'")
                conexion.commit()


                self.ui.txtrtn.setText('')
                self.ui.txtproveedor.setText('')

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
                QMessageBox.about(self, "Exito", "Compra registrada satisfactoriamente.")
            else :
                QMessageBox.warning(self, "Error", "Asegurese de seleccionar un tipo de pago y un proveedor.")
        else :
            QMessageBox.warning(self, "Error", "No hay detalles seleccionados.")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Compras()
    widget.show()
    sys.exit(app.exec())
