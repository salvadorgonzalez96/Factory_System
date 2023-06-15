# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'acercade.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QWidget)
import imagenes.imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(695, 242)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, 0, 1001, 431))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondoaplicacion.jpg);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(260, 30, 231, 20))
        font = QFont()
        font.setFamilies([u"Droid Sans"])
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 70, 171, 20))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 90, 161, 20))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 110, 111, 20))
        self.label_5.setFont(font)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(270, 130, 101, 20))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(280, 10, 201, 20))
        font1 = QFont()
        font1.setFamilies([u"Droid Sans"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(582, 210, 101, 20))
        self.label_8.setFont(font)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(150, 70, 121, 20))
        self.label_9.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Acerca De", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Desarrollado por TuxSoft", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Salvador Gonzalez ", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Liliana Hernandez", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Delbert Lira", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Axel Reyes", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Sistema de ventas", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Version 1.1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Integrantes:", None))
    # retranslateUi

