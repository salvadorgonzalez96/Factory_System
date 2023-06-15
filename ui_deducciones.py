# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Deducciones.ui'
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
    QPushButton, QSizePolicy, QTableView, QWidget)
import imagenes.imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 552)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 801, 551))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondoaplicacion.jpg);")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(330, 30, 356, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnNuevo = QPushButton(self.horizontalLayoutWidget)
        self.btnNuevo.setObjectName(u"btnNuevo")

        self.horizontalLayout.addWidget(self.btnNuevo)

        self.btnModificar3 = QPushButton(self.horizontalLayoutWidget)
        self.btnModificar3.setObjectName(u"btnModificar3")

        self.horizontalLayout.addWidget(self.btnModificar3)

        self.btnEliminar = QPushButton(self.horizontalLayoutWidget)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.horizontalLayout.addWidget(self.btnEliminar)

        self.btnRestaurar = QPushButton(self.horizontalLayoutWidget)
        self.btnRestaurar.setObjectName(u"btnRestaurar")

        self.horizontalLayout.addWidget(self.btnRestaurar)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(280, 140, 141, 20))
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(310, 180, 321, 98))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.txtNombre = QLineEdit(self.gridLayoutWidget)
        self.txtNombre.setObjectName(u"txtNombre")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtNombre.sizePolicy().hasHeightForWidth())
        self.txtNombre.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.txtNombre, 0, 1, 1, 1)

        self.txtDescripcion = QLineEdit(self.gridLayoutWidget)
        self.txtDescripcion.setObjectName(u"txtDescripcion")

        self.gridLayout.addWidget(self.txtDescripcion, 2, 1, 1, 1)

        self.comboPuesto = QComboBox(self.gridLayoutWidget)
        self.comboPuesto.setObjectName(u"comboPuesto")
        sizePolicy.setHeightForWidth(self.comboPuesto.sizePolicy().hasHeightForWidth())
        self.comboPuesto.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.comboPuesto, 1, 1, 1, 1)

        self.listadeducciones = QTableView(self.centralwidget)
        self.listadeducciones.setObjectName(u"listadeducciones")
        self.listadeducciones.setGeometry(QRect(10, 140, 256, 251))
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(310, 320, 121, 61))
        self.btnModificar2 = QPushButton(self.centralwidget)
        self.btnModificar2.setObjectName(u"btnModificar2")
        self.btnModificar2.setGeometry(QRect(310, 320, 121, 61))
        self.btnEliminar2 = QPushButton(self.centralwidget)
        self.btnEliminar2.setObjectName(u"btnEliminar2")
        self.btnEliminar2.setGeometry(QRect(310, 320, 121, 61))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mantenimiento de Deducciones", None))
        self.label.setText("")
        self.btnNuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnModificar3.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnRestaurar.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Datos de Deduccion", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Puesto", None))
        self.btnGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnModificar2.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnEliminar2.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
    # retranslateUi

