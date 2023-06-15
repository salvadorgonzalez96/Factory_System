# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'usuarios.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)
import imagenes.imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 554)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 801, 561))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondoaplicacion.jpg);")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(390, 20, 356, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnNuevo = QPushButton(self.horizontalLayoutWidget)
        self.btnNuevo.setObjectName(u"btnNuevo")

        self.horizontalLayout.addWidget(self.btnNuevo)

        self.btnModificar = QPushButton(self.horizontalLayoutWidget)
        self.btnModificar.setObjectName(u"btnModificar")

        self.horizontalLayout.addWidget(self.btnModificar)

        self.btnEliminar = QPushButton(self.horizontalLayoutWidget)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.horizontalLayout.addWidget(self.btnEliminar)

        self.btnRestaurar = QPushButton(self.horizontalLayoutWidget)
        self.btnRestaurar.setObjectName(u"btnRestaurar")

        self.horizontalLayout.addWidget(self.btnRestaurar)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 40, 231, 491))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.listaUsuarios = QTableView(self.verticalLayoutWidget)
        self.listaUsuarios.setObjectName(u"listaUsuarios")

        self.verticalLayout.addWidget(self.listaUsuarios)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(270, 150, 351, 98))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.txtClave = QLineEdit(self.gridLayoutWidget)
        self.txtClave.setObjectName(u"txtClave")
        self.txtClave.setEchoMode(QLineEdit.Normal)

        self.gridLayout.addWidget(self.txtClave, 1, 1, 1, 1)

        self.txtUsuario = QLineEdit(self.gridLayoutWidget)
        self.txtUsuario.setObjectName(u"txtUsuario")

        self.gridLayout.addWidget(self.txtUsuario, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.comboempleado = QComboBox(self.gridLayoutWidget)
        self.comboempleado.setObjectName(u"comboempleado")

        self.gridLayout.addWidget(self.comboempleado, 2, 1, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 110, 121, 20))
        self.btnAccesosU = QPushButton(self.centralwidget)
        self.btnAccesosU.setObjectName(u"btnAccesosU")
        self.btnAccesosU.setGeometry(QRect(593, 280, 121, 28))
        self.btnmodificar2 = QPushButton(self.centralwidget)
        self.btnmodificar2.setObjectName(u"btnmodificar2")
        self.btnmodificar2.setGeometry(QRect(270, 280, 142, 28))
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(270, 280, 142, 28))
        self.btnLimpiar = QPushButton(self.centralwidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(430, 280, 141, 28))
        self.btnEliminar2 = QPushButton(self.centralwidget)
        self.btnEliminar2.setObjectName(u"btnEliminar2")
        self.btnEliminar2.setGeometry(QRect(270, 280, 142, 28))
        self.txtcodigo = QLineEdit(self.centralwidget)
        self.txtcodigo.setObjectName(u"txtcodigo")
        self.txtcodigo.setGeometry(QRect(40, 10, 113, 28))
        self.btnRestaurar2 = QPushButton(self.centralwidget)
        self.btnRestaurar2.setObjectName(u"btnRestaurar2")
        self.btnRestaurar2.setGeometry(QRect(270, 280, 142, 28))
        self.comboCodigoEmpleado = QComboBox(self.centralwidget)
        self.comboCodigoEmpleado.setObjectName(u"comboCodigoEmpleado")
        self.comboCodigoEmpleado.setGeometry(QRect(50, 0, 171, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.comboCodigoEmpleado.raise_()
        self.txtcodigo.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.gridLayoutWidget.raise_()
        self.label_5.raise_()
        self.btnAccesosU.raise_()
        self.btnmodificar2.raise_()
        self.btnGuardar.raise_()
        self.btnLimpiar.raise_()
        self.btnEliminar2.raise_()
        self.btnRestaurar2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mantenimiento Usuarios", None))
        self.label.setText("")
        self.btnNuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnModificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnRestaurar.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Clave", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Empleado", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Datos de Usuario", None))
        self.btnAccesosU.setText(QCoreApplication.translate("MainWindow", u"Accesos", None))
        self.btnmodificar2.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.btnEliminar2.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnRestaurar2.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
    # retranslateUi

