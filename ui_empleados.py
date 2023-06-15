# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'empleados.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QTableView,
    QVBoxLayout, QWidget)
import imagenes.imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(956, 579)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -20, 971, 601))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondoaplicacion.jpg);")
        self.btnnuevo = QPushButton(self.centralwidget)
        self.btnnuevo.setObjectName(u"btnnuevo")
        self.btnnuevo.setGeometry(QRect(380, 20, 84, 28))
        self.btnmodificar = QPushButton(self.centralwidget)
        self.btnmodificar.setObjectName(u"btnmodificar")
        self.btnmodificar.setGeometry(QRect(470, 20, 84, 28))
        self.btneliminar = QPushButton(self.centralwidget)
        self.btneliminar.setObjectName(u"btneliminar")
        self.btneliminar.setGeometry(QRect(560, 20, 84, 28))
        self.btnrestaurar = QPushButton(self.centralwidget)
        self.btnrestaurar.setObjectName(u"btnrestaurar")
        self.btnrestaurar.setGeometry(QRect(650, 20, 84, 28))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(380, 60, 351, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.txtid = QLineEdit(self.verticalLayoutWidget)
        self.txtid.setObjectName(u"txtid")
        self.txtid.setMaxLength(13)

        self.horizontalLayout_9.addWidget(self.txtid)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.txtpnombre = QLineEdit(self.verticalLayoutWidget)
        self.txtpnombre.setObjectName(u"txtpnombre")
        self.txtpnombre.setMaxLength(45)

        self.horizontalLayout_6.addWidget(self.txtpnombre)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.txtsnombre = QLineEdit(self.verticalLayoutWidget)
        self.txtsnombre.setObjectName(u"txtsnombre")
        self.txtsnombre.setMaxLength(45)

        self.horizontalLayout_8.addWidget(self.txtsnombre)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.txtpapellido = QLineEdit(self.verticalLayoutWidget)
        self.txtpapellido.setObjectName(u"txtpapellido")
        self.txtpapellido.setMaxLength(45)

        self.horizontalLayout_7.addWidget(self.txtpapellido)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_10.addWidget(self.label_7)

        self.txtsapellido = QLineEdit(self.verticalLayoutWidget)
        self.txtsapellido.setObjectName(u"txtsapellido")
        self.txtsapellido.setMaxLength(45)

        self.horizontalLayout_10.addWidget(self.txtsapellido)


        self.verticalLayout.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.fechanac = QDateEdit(self.verticalLayoutWidget)
        self.fechanac.setObjectName(u"fechanac")

        self.horizontalLayout_5.addWidget(self.fechanac)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_3.addWidget(self.label_9)

        self.bgmasculino = QRadioButton(self.verticalLayoutWidget)
        self.bgmasculino.setObjectName(u"bgmasculino")

        self.horizontalLayout_3.addWidget(self.bgmasculino)

        self.bgfemenino = QRadioButton(self.verticalLayoutWidget)
        self.bgfemenino.setObjectName(u"bgfemenino")

        self.horizontalLayout_3.addWidget(self.bgfemenino)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_10 = QLabel(self.verticalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout.addWidget(self.label_10)

        self.comboestadocivil = QComboBox(self.verticalLayoutWidget)
        self.comboestadocivil.setObjectName(u"comboestadocivil")

        self.horizontalLayout.addWidget(self.comboestadocivil)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_2.addWidget(self.label_11)

        self.combocargo = QComboBox(self.verticalLayoutWidget)
        self.combocargo.setObjectName(u"combocargo")

        self.horizontalLayout_2.addWidget(self.combocargo)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_11.addWidget(self.label_13)

        self.combotipocon = QComboBox(self.verticalLayoutWidget)
        self.combotipocon.setObjectName(u"combotipocon")

        self.horizontalLayout_11.addWidget(self.combotipocon)


        self.verticalLayout.addLayout(self.horizontalLayout_11)

        self.btnguardar = QPushButton(self.centralwidget)
        self.btnguardar.setObjectName(u"btnguardar")
        self.btnguardar.setGeometry(QRect(300, 510, 141, 51))
        self.listempleados = QTableView(self.centralwidget)
        self.listempleados.setObjectName(u"listempleados")
        self.listempleados.setGeometry(QRect(10, 20, 361, 481))
        self.btnModificar2 = QPushButton(self.centralwidget)
        self.btnModificar2.setObjectName(u"btnModificar2")
        self.btnModificar2.setGeometry(QRect(300, 510, 141, 51))
        self.btnEliminar2 = QPushButton(self.centralwidget)
        self.btnEliminar2.setObjectName(u"btnEliminar2")
        self.btnEliminar2.setGeometry(QRect(300, 510, 141, 51))
        self.txtcodigo = QLineEdit(self.centralwidget)
        self.txtcodigo.setObjectName(u"txtcodigo")
        self.txtcodigo.setGeometry(QRect(60, 0, 113, 28))
        self.btnrestaurar2 = QPushButton(self.centralwidget)
        self.btnrestaurar2.setObjectName(u"btnrestaurar2")
        self.btnrestaurar2.setGeometry(QRect(300, 510, 141, 51))
        MainWindow.setCentralWidget(self.centralwidget)
        self.txtcodigo.raise_()
        self.label.raise_()
        self.btnnuevo.raise_()
        self.btnmodificar.raise_()
        self.btneliminar.raise_()
        self.btnrestaurar.raise_()
        self.verticalLayoutWidget.raise_()
        self.btnguardar.raise_()
        self.listempleados.raise_()
        self.btnModificar2.raise_()
        self.btnEliminar2.raise_()
        self.btnrestaurar2.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Menu Empleados", None))
        self.label.setText("")
        self.btnnuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.btnmodificar.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btneliminar.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnrestaurar.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Primer nombre", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Segundo Nombre", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Primer apellido", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Segundo apellido", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Fecha Nacimiento", None))
        self.fechanac.setDisplayFormat(QCoreApplication.translate("MainWindow", u"M/d/yyyy ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Genero", None))
        self.bgmasculino.setText(QCoreApplication.translate("MainWindow", u"Masculino", None))
        self.bgfemenino.setText(QCoreApplication.translate("MainWindow", u"Femenino", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Estado Civil", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Cargo Laboral", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Tipo Contratacion", None))
        self.btnguardar.setText(QCoreApplication.translate("MainWindow", u"Guardar", None))
        self.btnModificar2.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.btnEliminar2.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.btnrestaurar2.setText(QCoreApplication.translate("MainWindow", u"Restaurar", None))
    # retranslateUi

