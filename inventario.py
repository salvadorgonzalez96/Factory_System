import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtGui import QTextDocument, QTextTableFormat, QTextCursor, QPageSize, QPdfWriter
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from ui_inventario import Ui_MainWindow
from PySide6.QtCore import Qt, QAbstractItemModel
from fpdf import FPDF
import xlsxwriter
from Conexion import Conexion  # Importar la conexión y el cursor

class Inventario(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        self.llenartabla()
        self.ui.btnBuscar.clicked.connect(self.buscar_productos)
        self.ui.btnExporpdf.clicked.connect(self.exportar_a_pdf)
        self.ui.btnExporexcel.clicked.connect(self.exportar_a_excel)
# Configurar la tabla ...
    def llenartabla(self):
        # Crear conexión
        self.modelo = QStandardItemModel()
        self.ui.tablaproductos.setModel(self.modelo)

        # Establecer encabezados de columnas
        columnas = ["Código", "Código de Barra", "Descripción", "Stock", "Peso", "Precio de Venta", "Impuesto", "Proveedor", "Descuento"]
        self.modelo.setHorizontalHeaderLabels(columnas)

        # Obtener la conexión a la base de datos
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()

        # Ejecutar la consulta
        consulta = "SELECT * FROM vista_det_productos"



        cursor.execute(consulta)

        # Llenar el modelo con los datos obtenidos
        for fila_datos in cursor:
            # Crear una fila en el modelo
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)

        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()


    def buscar_productos(self):
        # Obtener el texto de búsqueda del cuadro de búsqueda
        texto_busqueda = self.ui.txtBuscarpro.text()

        # Eliminar todas las filas de la tabla existente
        self.modelo.removeRows(0, self.modelo.rowCount())

        # Obtener la conexión a la base de datos
        conexion = Conexion().getConexion()
        cursor = conexion.cursor()

        # Ejecutar la consulta
        consulta = f"SELECT * FROM vista_det_productos WHERE producto_descripcion LIKE '%{texto_busqueda}%'"

        cursor.execute(consulta)

        # Llenar el modelo con los datos obtenidos
        for fila_datos in cursor:
            # Crear una fila en el modelo
            fila = [QStandardItem(str(valor)) for valor in fila_datos.values()]
            self.modelo.appendRow(fila)

        # Cerrar la conexión y el cursor
        cursor.close()
        conexion.close()

    def exportar_a_pdf(self):
        # Obtener la ruta del archivo de destino
        ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo PDF", "", "Archivos PDF (*.pdf)")

        if ruta:
            # Crear el objeto FPDF
            pdf = FPDF()
            pdf.add_page(orientation='L')
            pdf.set_font('Arial', 'B', 12)
            pdf.cell(0, 10, "Lista de productos", 0, 1, "C")

            # Agregar las cabeceras de las columnas
            # Agregar las cabeceras de las columnas
            pdf.cell(20, 10, "Código", 1, 0, "C")
            pdf.cell(40, 10, "Código de barra", 1, 0, "C")
            pdf.cell(40, 10, "Descripción", 1, 0, "C")
            pdf.cell(20, 10, "Stock", 1, 0, "C")
            pdf.cell(30, 10, "Peso", 1, 0, "C")
            pdf.cell(35, 10, "Precio de venta", 1, 0, "C")
            pdf.cell(20, 10, "Impuesto", 1, 0, "C")
            pdf.cell(30, 10, "Proveedor", 1, 0, "C")
            pdf.cell(40, 10, "Descuento", 1, 1, "C")

# Agregar los datos de la tabla
        for fila in range(self.modelo.rowCount()):
            pdf.cell(20, 10, str(self.modelo.index(fila, 0).data()), 1, 0, "C")
            pdf.cell(40, 10, str(self.modelo.index(fila, 1).data()), 1, 0, "C")
            pdf.cell(40, 10, str(self.modelo.index(fila, 2).data()), 1, 0, "C")
            pdf.cell(20, 10, str(self.modelo.index(fila, 3).data()), 1, 0, "C")
            pdf.cell(30, 10, str(self.modelo.index(fila, 4).data()), 1, 0, "C")
            pdf.cell(35, 10, str(self.modelo.index(fila, 5).data()), 1, 0, "C")
            pdf.cell(20, 10, str(self.modelo.index(fila, 6).data()), 1, 0, "C")
            pdf.cell(30, 10, str(self.modelo.index(fila, 7).data()), 1, 0, "C")
            pdf.cell(40, 10, str(self.modelo.index(fila, 8).data()), 1, 1, "C")
        pdf.ln()

            # Guardar el archivo PDF
        pdf.output(ruta + ".pdf", "F")
        
    def exportar_a_excel(self):  
        
    # Obtener la ruta del archivo de destino
        ruta2, _ = QFileDialog.getSaveFileName(self, "Guardar archivo de Excel", "", "Archivos de Excel (*.xlsx)")

        if ruta2:
            
        # Crear el objeto Workbook y la hoja de cálculo
            workbook = xlsxwriter.Workbook(ruta2 + '.xlsx')
            hoja = workbook.add_worksheet()

        # Agregar las cabeceras de las columnas
            for columna in range(self.ui.tablaproductos.model().columnCount()):
                header = self.ui.tablaproductos.horizontalHeader()
                modelo = self.ui.tablaproductos.model()
                texto = modelo.headerData(columna, Qt.Horizontal, Qt.DisplayRole)
                hoja.write(0, columna, texto)

        # Agregar los datos de la tabla
            for fila in range(modelo.rowCount()):
                for columna in range(modelo.columnCount()):
                    celda = modelo.index(fila, columna)
                    texto = str(celda.data())
                    hoja.write(fila+1, columna, texto)

        # Ajustar el ancho de las columnas
            for columna in range(self.ui.tablaproductos.model().columnCount()):
                header = self.ui.tablaproductos.horizontalHeader()
                modelo = self.ui.tablaproductos.model()
                texto = modelo.headerData(columna, Qt.Horizontal, Qt.DisplayRole)
                hoja.set_column(columna, columna, len(texto))

        # Guardar el archivo de Excel
        workbook.close()


    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Inventario()
    widget.show()
    sys.exit(app.exec())
