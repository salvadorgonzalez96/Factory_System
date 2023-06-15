# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Inventario.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import imagenes.imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1178, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, 0, 1191, 601))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondoaplicacion.jpg);")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(980, 140, 151, 98))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnExporpdf = QPushButton(self.verticalLayoutWidget)
        self.btnExporpdf.setObjectName(u"btnExporpdf")

        self.verticalLayout.addWidget(self.btnExporpdf)

        self.btnExporexcel = QPushButton(self.verticalLayoutWidget)
        self.btnExporexcel.setObjectName(u"btnExporexcel")

        self.verticalLayout.addWidget(self.btnExporexcel)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(939, 30, 231, 90))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.txtBuscarpro = QLineEdit(self.verticalLayoutWidget_2)
        self.txtBuscarpro.setObjectName(u"txtBuscarpro")

        self.verticalLayout_2.addWidget(self.txtBuscarpro)

        self.btnBuscar = QPushButton(self.verticalLayoutWidget_2)
        self.btnBuscar.setObjectName(u"btnBuscar")

        self.verticalLayout_2.addWidget(self.btnBuscar)

        self.tablaproductos = QTableView(self.centralwidget)
        self.tablaproductos.setObjectName(u"tablaproductos")
        self.tablaproductos.setGeometry(QRect(20, 20, 911, 561))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lista Productos", None))
        self.label.setText("")
        self.btnExporpdf.setText(QCoreApplication.translate("MainWindow", u"Exportar PDF", None))
        self.btnExporexcel.setText(QCoreApplication.translate("MainWindow", u"Exportar Excel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre producto", None))
        self.btnBuscar.setText(QCoreApplication.translate("MainWindow", u"Buscar", None))
    # retranslateUi

