# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'accesousuarios.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QSizePolicy, QTableView,
    QWidget)
import imagenes.imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(717, 590)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 801, 601))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondoaplicacion.jpg);")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(170, 10, 451, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Droid Sans"])
        font.setPointSize(14)
        self.label_2.setFont(font)

        self.horizontalLayout.addWidget(self.label_2)

        self.comboemple = QComboBox(self.horizontalLayoutWidget)
        self.comboemple.setObjectName(u"comboemple")

        self.horizontalLayout.addWidget(self.comboemple)

        self.listaccesoenlis = QTableView(self.centralwidget)
        self.listaccesoenlis.setObjectName(u"listaccesoenlis")
        self.listaccesoenlis.setGeometry(QRect(10, 140, 256, 441))
        self.listaccesoreg = QTableView(self.centralwidget)
        self.listaccesoreg.setObjectName(u"listaccesoreg")
        self.listaccesoreg.setGeometry(QRect(450, 140, 256, 441))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 120, 171, 20))
        font1 = QFont()
        font1.setFamilies([u"Droid Sans"])
        font1.setPointSize(13)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(500, 120, 181, 20))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(290, 220, 151, 20))
        self.label_5.setFont(font1)
        self.cmbCodigoUsuario = QComboBox(self.centralwidget)
        self.cmbCodigoUsuario.setObjectName(u"cmbCodigoUsuario")
        self.cmbCodigoUsuario.setGeometry(QRect(30, 30, 111, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.cmbCodigoUsuario.raise_()
        self.label.raise_()
        self.horizontalLayoutWidget.raise_()
        self.listaccesoenlis.raise_()
        self.listaccesoreg.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Acceso de Usuarios", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Seleccione Empleado", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Accesos Enlistados", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Accesos Registrados", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Accesos Usuarios", None))
    # retranslateUi

