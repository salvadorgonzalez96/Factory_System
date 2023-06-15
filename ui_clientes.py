# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clientes.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import imagenes.imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 510)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-8, -1, 821, 611))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondoaplicacion.jpg);")
        self.tablaclientes = QTableView(self.centralwidget)
        self.tablaclientes.setObjectName(u"tablaclientes")
        self.tablaclientes.setGeometry(QRect(20, 50, 256, 421))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(330, 10, 451, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnNuevo = QPushButton(self.horizontalLayoutWidget)
        self.btnNuevo.setObjectName(u"btnNuevo")

        self.horizontalLayout.addWidget(self.btnNuevo)

        self.btnModificar = QPushButton(self.horizontalLayoutWidget)
        self.btnModificar.setObjectName(u"btnModificar")

        self.horizontalLayout.addWidget(self.btnModificar)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(380, 60, 351, 261))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_9.addWidget(self.label_3)

        self.txtNombrecli = QLineEdit(self.verticalLayoutWidget)
        self.txtNombrecli.setObjectName(u"txtNombrecli")
        self.txtNombrecli.setMaxLength(13)

        self.horizontalLayout_9.addWidget(self.txtNombrecli)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.txtRtn = QLineEdit(self.verticalLayoutWidget)
        self.txtRtn.setObjectName(u"txtRtn")
        self.txtRtn.setMaxLength(45)

        self.horizontalLayout_6.addWidget(self.txtRtn)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.txtDireccion = QLineEdit(self.verticalLayoutWidget)
        self.txtDireccion.setObjectName(u"txtDireccion")
        self.txtDireccion.setMaxLength(45)

        self.horizontalLayout_8.addWidget(self.txtDireccion)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.txtTelefono = QLineEdit(self.verticalLayoutWidget)
        self.txtTelefono.setObjectName(u"txtTelefono")
        self.txtTelefono.setMaxLength(45)

        self.horizontalLayout_7.addWidget(self.txtTelefono)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.txtEmail = QLineEdit(self.verticalLayoutWidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setMaxLength(45)

        self.horizontalLayout_10.addWidget(self.txtEmail)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(300, 400, 141, 41))
        self.btnModificar2 = QPushButton(self.centralwidget)
        self.btnModificar2.setObjectName(u"btnModificar2")
        self.btnModificar2.setGeometry(QRect(300, 400, 141, 41))
        self.btnEliminar2 = QPushButton(self.centralwidget)
        self.btnEliminar2.setObjectName(u"btnEliminar2")
        self.btnEliminar2.setGeometry(QRect(300, 400, 141, 41))
        self.txtCodigo = QLineEdit(self.centralwidget)
        self.txtCodigo.setObjectName(u"txtCodigo")
        self.txtCodigo.setGeometry(QRect(30, 10, 113, 28))
        self.btnrestaurar2 = QPushButton(self.centralwidget)
        self.btnrestaurar2.setObjectName(u"btnrestaurar2")
        self.btnrestaurar2.setGeometry(QRect(300, 400, 141, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.txtCodigo.raise_()
        self.label.raise_()
        self.tablaclientes.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.btnGuardar.raise_()
        self.btnModificar2.raise_()
        self.btnEliminar2.raise_()
        self.btnrestaurar2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Menu Clientes", None))
        self.label.setText("")
        self.btnNuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnModificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"RTN", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Direccion", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Telefono", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.btnGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnModificar2.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnEliminar2.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnrestaurar2.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
    # retranslateUi

