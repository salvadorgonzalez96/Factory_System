# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'categoria.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QWidget)
import imagenes.imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(734, 475)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 771, 491))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondoaplicacion.jpg);")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(320, 100, 361, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.txtnombrecat = QLineEdit(self.gridLayoutWidget)
        self.txtnombrecat.setObjectName(u"txtnombrecat")

        self.gridLayout.addWidget(self.txtnombrecat, 0, 1, 1, 1)

        self.txtdescripcioncat = QLineEdit(self.gridLayoutWidget)
        self.txtdescripcioncat.setObjectName(u"txtdescripcioncat")

        self.gridLayout.addWidget(self.txtdescripcioncat, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.tablacategoria = QTableView(self.centralwidget)
        self.tablacategoria.setObjectName(u"tablacategoria")
        self.tablacategoria.setGeometry(QRect(10, 60, 291, 371))
        self.gridLayoutWidget_2 = QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(360, 10, 344, 51))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnNuevo = QPushButton(self.gridLayoutWidget_2)
        self.btnNuevo.setObjectName(u"btnNuevo")

        self.gridLayout_2.addWidget(self.btnNuevo, 0, 0, 1, 1)

        self.btnModificar = QPushButton(self.gridLayoutWidget_2)
        self.btnModificar.setObjectName(u"btnModificar")

        self.gridLayout_2.addWidget(self.btnModificar, 0, 1, 1, 1)

        self.btnEliminar = QPushButton(self.gridLayoutWidget_2)
        self.btnEliminar.setObjectName(u"btnEliminar")

        self.gridLayout_2.addWidget(self.btnEliminar, 0, 2, 1, 1)

        self.btnRestaurar = QPushButton(self.gridLayoutWidget_2)
        self.btnRestaurar.setObjectName(u"btnRestaurar")

        self.gridLayout_2.addWidget(self.btnRestaurar, 0, 3, 1, 1)

        self.txtcodigocat = QLineEdit(self.centralwidget)
        self.txtcodigocat.setObjectName(u"txtcodigocat")
        self.txtcodigocat.setGeometry(QRect(30, 20, 113, 28))
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(340, 380, 111, 41))
        self.btnModificar2 = QPushButton(self.centralwidget)
        self.btnModificar2.setObjectName(u"btnModificar2")
        self.btnModificar2.setGeometry(QRect(340, 380, 111, 41))
        self.btnEliminar2 = QPushButton(self.centralwidget)
        self.btnEliminar2.setObjectName(u"btnEliminar2")
        self.btnEliminar2.setGeometry(QRect(340, 380, 111, 41))
        self.btnRestaurar2 = QPushButton(self.centralwidget)
        self.btnRestaurar2.setObjectName(u"btnRestaurar2")
        self.btnRestaurar2.setGeometry(QRect(340, 380, 111, 41))
        MainWindow.setCentralWidget(self.centralwidget)
        self.txtcodigocat.raise_()
        self.label.raise_()
        self.gridLayoutWidget.raise_()
        self.tablacategoria.raise_()
        self.gridLayoutWidget_2.raise_()
        self.btnGuardar.raise_()
        self.btnModificar2.raise_()
        self.btnEliminar2.raise_()
        self.btnRestaurar2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Menu Categorias", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None))
        self.btnNuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnModificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnEliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnRestaurar.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
        self.btnGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnModificar2.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnEliminar2.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnRestaurar2.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
    # retranslateUi

