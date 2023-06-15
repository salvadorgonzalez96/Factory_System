# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import imagenes.imagenes_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(299, 297)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 100, 231, 70))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txtusuario = QLineEdit(self.verticalLayoutWidget)
        self.txtusuario.setObjectName(u"txtusuario")
        font = QFont()
        font.setFamilies([u"Droid Sans"])
        font.setPointSize(12)
        self.txtusuario.setFont(font)
        self.txtusuario.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txtusuario.setMaxLength(60)

        self.verticalLayout_3.addWidget(self.txtusuario)

        self.txtcontra = QLineEdit(self.verticalLayoutWidget)
        self.txtcontra.setObjectName(u"txtcontra")
        self.txtcontra.setFont(font)
        self.txtcontra.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txtcontra.setMaxLength(60)
        self.txtcontra.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.txtcontra)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(100, 190, 91, 89))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btnsalir = QPushButton(self.gridLayoutWidget)
        self.btnsalir.setObjectName(u"btnsalir")
        self.btnsalir.setFont(font)
        self.btnsalir.setStyleSheet(u"image: url(:/imagenes/salirlogin.jpg);")

        self.gridLayout.addWidget(self.btnsalir, 2, 0, 1, 1)

        self.btningresar = QPushButton(self.gridLayoutWidget)
        self.btningresar.setObjectName(u"btningresar")
        self.btningresar.setFont(font)
#if QT_CONFIG(statustip)
        self.btningresar.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        self.btningresar.setLayoutDirection(Qt.LeftToRight)
        self.btningresar.setAutoFillBackground(False)
        self.btningresar.setStyleSheet(u"image: url(:/imagenes/Next_arrow_10211.ico);")

        self.gridLayout.addWidget(self.btningresar, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 301, 331))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondologin.jpg);\n"
"background-repeat: no-repeat;\n"
"")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.verticalLayoutWidget.raise_()
        self.gridLayoutWidget.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Login", None))
        self.txtusuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.txtcontra.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.btnsalir.setText("")
#if QT_CONFIG(accessibility)
        self.btningresar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.btningresar.setText("")
        self.label.setText("")
    # retranslateUi

