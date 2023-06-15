# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'compras.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import imagenes.imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1715, 766)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, 0, 1731, 771))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondoaplicacion.jpg);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(50, 20, 211, 20))
        font = QFont()
        font.setFamilies([u"Droid Sans"])
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(30, 80, 531, 51))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName(u"label_12")
        font1 = QFont()
        font1.setFamilies([u"Droid Sans"])
        font1.setPointSize(12)
        self.label_12.setFont(font1)

        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout.addWidget(self.label_11, 0, 0, 1, 1)

        self.txtcodigo = QLineEdit(self.gridLayoutWidget)
        self.txtcodigo.setObjectName(u"txtcodigo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtcodigo.sizePolicy().hasHeightForWidth())
        self.txtcodigo.setSizePolicy(sizePolicy)
        self.txtcodigo.setReadOnly(True)

        self.gridLayout.addWidget(self.txtcodigo, 0, 3, 1, 1)

        self.txtnombrepro = QLineEdit(self.gridLayoutWidget)
        self.txtnombrepro.setObjectName(u"txtnombrepro")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txtnombrepro.sizePolicy().hasHeightForWidth())
        self.txtnombrepro.setSizePolicy(sizePolicy1)
        self.txtnombrepro.setReadOnly(True)

        self.gridLayout.addWidget(self.txtnombrepro, 0, 1, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(30, 130, 749, 31))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.gridLayoutWidget_2)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 0, 5, 1, 1)

        self.txtprecio = QLineEdit(self.gridLayoutWidget_2)
        self.txtprecio.setObjectName(u"txtprecio")
        self.txtprecio.setReadOnly(True)

        self.gridLayout_2.addWidget(self.txtprecio, 0, 7, 1, 1)

        self.txtpeso = QLineEdit(self.gridLayoutWidget_2)
        self.txtpeso.setObjectName(u"txtpeso")
        sizePolicy.setHeightForWidth(self.txtpeso.sizePolicy().hasHeightForWidth())
        self.txtpeso.setSizePolicy(sizePolicy)
        self.txtpeso.setReadOnly(True)

        self.gridLayout_2.addWidget(self.txtpeso, 0, 3, 1, 1)

        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_2.addWidget(self.label_13, 0, 2, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.gridLayout_2.addWidget(self.label_14, 0, 0, 1, 1)

        self.txtcantidad = QLineEdit(self.gridLayoutWidget_2)
        self.txtcantidad.setObjectName(u"txtcantidad")
        sizePolicy.setHeightForWidth(self.txtcantidad.sizePolicy().hasHeightForWidth())
        self.txtcantidad.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.txtcantidad, 0, 1, 1, 1)

        self.label_16 = QLabel(self.gridLayoutWidget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.gridLayout_2.addWidget(self.label_16, 0, 6, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout_2.addWidget(self.label_15, 0, 4, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 240, 361, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.horizontalLayoutWidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font1)

        self.horizontalLayout.addWidget(self.label_18)

        self.txtbuscarpro = QLineEdit(self.horizontalLayoutWidget)
        self.txtbuscarpro.setObjectName(u"txtbuscarpro")

        self.horizontalLayout.addWidget(self.txtbuscarpro)

        self.listaproveedores = QTableView(self.centralwidget)
        self.listaproveedores.setObjectName(u"listaproveedores")
        self.listaproveedores.setGeometry(QRect(1320, 50, 381, 192))
        self.listaproveedores.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(1460, 30, 141, 20))
        self.label_19.setFont(font1)
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(230, 290, 231, 20))
        self.label_20.setFont(font)
        self.listaproductosinv = QTableView(self.centralwidget)
        self.listaproductosinv.setObjectName(u"listaproductosinv")
        self.listaproductosinv.setGeometry(QRect(30, 320, 1111, 192))
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(230, 520, 231, 20))
        self.label_21.setFont(font)
        self.listaproductosfac = QTableView(self.centralwidget)
        self.listaproductosfac.setObjectName(u"listaproductosfac")
        self.listaproductosfac.setGeometry(QRect(20, 550, 1111, 192))
        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(1370, 350, 296, 92))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.radiocontaefec = QRadioButton(self.gridLayoutWidget_3)
        self.radiocontaefec.setObjectName(u"radiocontaefec")
        self.radiocontaefec.setFont(font1)

        self.gridLayout_3.addWidget(self.radiocontaefec, 0, 1, 1, 1)

        self.radiocontatar = QRadioButton(self.gridLayoutWidget_3)
        self.radiocontatar.setObjectName(u"radiocontatar")
        self.radiocontatar.setFont(font1)

        self.gridLayout_3.addWidget(self.radiocontatar, 1, 1, 1, 1)

        self.radiocredito = QRadioButton(self.gridLayoutWidget_3)
        self.radiocredito.setObjectName(u"radiocredito")
        self.radiocredito.setFont(font1)

        self.gridLayout_3.addWidget(self.radiocredito, 2, 1, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget_3)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font1)

        self.gridLayout_3.addWidget(self.label_22, 1, 0, 1, 1)

        self.gridLayoutWidget_4 = QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(1370, 460, 301, 141))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.gridLayoutWidget_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font1)

        self.gridLayout_5.addWidget(self.label_23, 0, 0, 1, 1)

        self.label_26 = QLabel(self.gridLayoutWidget_4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font1)

        self.gridLayout_5.addWidget(self.label_26, 3, 0, 1, 1)

        self.label_25 = QLabel(self.gridLayoutWidget_4)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.gridLayout_5.addWidget(self.label_25, 2, 0, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget_4)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font1)

        self.gridLayout_5.addWidget(self.label_24, 1, 0, 1, 1)

        self.txtsubtotal = QLineEdit(self.gridLayoutWidget_4)
        self.txtsubtotal.setObjectName(u"txtsubtotal")
        self.txtsubtotal.setReadOnly(True)

        self.gridLayout_5.addWidget(self.txtsubtotal, 0, 1, 1, 1)

        self.txtdescuento = QLineEdit(self.gridLayoutWidget_4)
        self.txtdescuento.setObjectName(u"txtdescuento")
        self.txtdescuento.setReadOnly(True)

        self.gridLayout_5.addWidget(self.txtdescuento, 1, 1, 1, 1)

        self.txtisv = QLineEdit(self.gridLayoutWidget_4)
        self.txtisv.setObjectName(u"txtisv")
        self.txtisv.setReadOnly(True)

        self.gridLayout_5.addWidget(self.txtisv, 2, 1, 1, 1)

        self.txttotal = QLineEdit(self.gridLayoutWidget_4)
        self.txttotal.setObjectName(u"txttotal")
        self.txttotal.setReadOnly(True)

        self.gridLayout_5.addWidget(self.txttotal, 3, 1, 1, 1)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1440, 630, 160, 31))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnComprar = QPushButton(self.verticalLayoutWidget_2)
        self.btnComprar.setObjectName(u"btnComprar")
        self.btnComprar.setFont(font1)

        self.verticalLayout_2.addWidget(self.btnComprar)

        self.gridLayoutWidget_5 = QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(740, 210, 361, 80))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)

        self.txtproveedor = QLineEdit(self.gridLayoutWidget_5)
        self.txtproveedor.setObjectName(u"txtproveedor")

        self.gridLayout_4.addWidget(self.txtproveedor, 0, 1, 1, 1)

        self.txtrtn = QLineEdit(self.gridLayoutWidget_5)
        self.txtrtn.setObjectName(u"txtrtn")

        self.gridLayout_4.addWidget(self.txtrtn, 1, 1, 1, 1)

        self.txtTempISV = QLineEdit(self.centralwidget)
        self.txtTempISV.setObjectName(u"txtTempISV")
        self.txtTempISV.setGeometry(QRect(360, 20, 113, 28))
        self.txtTempDescuento = QLineEdit(self.centralwidget)
        self.txtTempDescuento.setObjectName(u"txtTempDescuento")
        self.txtTempDescuento.setGeometry(QRect(490, 20, 113, 28))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(790, 140, 81, 20))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(870, 130, 113, 28))
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 160, 261, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.label_7)

        self.cmbImpuesto = QComboBox(self.horizontalLayoutWidget_2)
        self.cmbImpuesto.setObjectName(u"cmbImpuesto")

        self.horizontalLayout_2.addWidget(self.cmbImpuesto)

        self.btnagregar = QPushButton(self.centralwidget)
        self.btnagregar.setObjectName(u"btnagregar")
        self.btnagregar.setGeometry(QRect(400, 240, 158, 26))
        self.btnagregar.setFont(font1)
        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(320, 160, 261, 41))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.cmbCategoria = QComboBox(self.horizontalLayoutWidget_4)
        self.cmbCategoria.setObjectName(u"cmbCategoria")

        self.horizontalLayout_4.addWidget(self.cmbCategoria)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(610, 160, 261, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.horizontalLayoutWidget_5)
        self.label_27.setObjectName(u"label_27")
        sizePolicy2.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.label_27)

        self.cmbDescuento = QComboBox(self.horizontalLayoutWidget_5)
        self.cmbDescuento.setObjectName(u"cmbDescuento")

        self.horizontalLayout_5.addWidget(self.cmbDescuento)

        MainWindow.setCentralWidget(self.centralwidget)
        self.txtTempDescuento.raise_()
        self.txtTempISV.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.gridLayoutWidget.raise_()
        self.gridLayoutWidget_2.raise_()
        self.horizontalLayoutWidget.raise_()
        self.listaproveedores.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.listaproductosinv.raise_()
        self.label_21.raise_()
        self.listaproductosfac.raise_()
        self.gridLayoutWidget_3.raise_()
        self.gridLayoutWidget_4.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.gridLayoutWidget_5.raise_()
        self.label_6.raise_()
        self.lineEdit.raise_()
        self.horizontalLayoutWidget_2.raise_()
        self.btnagregar.raise_()
        self.horizontalLayoutWidget_4.raise_()
        self.horizontalLayoutWidget_5.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Compras", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ingreso de Productos", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Codigo", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Nombre del producto", None))
        self.label_17.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Cantidad", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Precio Costo", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"lbs", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Buscar Producto", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Lista Proveedores", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Productos en Inventario", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Productos a Facturar", None))
        self.radiocontaefec.setText(QCoreApplication.translate("MainWindow", u"Contado Efectivo", None))
        self.radiocontatar.setText(QCoreApplication.translate("MainWindow", u"Contado Tarjeta", None))
        self.radiocredito.setText(QCoreApplication.translate("MainWindow", u"Credito", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Formas de pago", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"SubTotal", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"ISV", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Descuento", None))
        self.btnComprar.setText(QCoreApplication.translate("MainWindow", u"Comprar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"RTN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"% Ganancia", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Impuesto ISV", None))
        self.btnagregar.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Categoria", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Descuento", None))
    # retranslateUi

