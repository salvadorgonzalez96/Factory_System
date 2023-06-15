# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QWidget)
import imagenes.imagenes_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(839, 566)
        MainWindow.setStyleSheet(u"")
        self.actionAcerca_de = QAction(MainWindow)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.actionEmpleados = QAction(MainWindow)
        self.actionEmpleados.setObjectName(u"actionEmpleados")
        self.actionUsuarios = QAction(MainWindow)
        self.actionUsuarios.setObjectName(u"actionUsuarios")
        self.actionAjustes = QAction(MainWindow)
        self.actionAjustes.setObjectName(u"actionAjustes")
        self.actionCerrar_Session = QAction(MainWindow)
        self.actionCerrar_Session.setObjectName(u"actionCerrar_Session")
        self.actionClientes = QAction(MainWindow)
        self.actionClientes.setObjectName(u"actionClientes")
        self.actionProveedores = QAction(MainWindow)
        self.actionProveedores.setObjectName(u"actionProveedores")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnventa = QPushButton(self.centralwidget)
        self.btnventa.setObjectName(u"btnventa")
        self.btnventa.setGeometry(QRect(40, 70, 84, 28))
        font = QFont()
        font.setFamilies([u"Droid Sans"])
        font.setPointSize(13)
        self.btnventa.setFont(font)
        self.btnreportes = QPushButton(self.centralwidget)
        self.btnreportes.setObjectName(u"btnreportes")
        self.btnreportes.setGeometry(QRect(40, 130, 84, 28))
        self.btnreportes.setFont(font)
        self.btncompra = QPushButton(self.centralwidget)
        self.btncompra.setObjectName(u"btncompra")
        self.btncompra.setGeometry(QRect(40, 190, 84, 28))
        self.btncompra.setFont(font)
        self.btninventario = QPushButton(self.centralwidget)
        self.btninventario.setObjectName(u"btninventario")
        self.btninventario.setGeometry(QRect(40, 250, 101, 28))
        self.btninventario.setFont(font)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-18, -1, 871, 551))
        self.label.setStyleSheet(u"background-image: url(:/imagenes/fondoaplicacion.jpg);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(350, 60, 221, 20))
        font1 = QFont()
        font1.setFamilies([u"Droid Sans"])
        font1.setPointSize(16)
        self.label_2.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.btnventa.raise_()
        self.btnreportes.raise_()
        self.btncompra.raise_()
        self.btninventario.raise_()
        self.label_2.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 839, 25))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuUsuarios = QMenu(self.menubar)
        self.menuUsuarios.setObjectName(u"menuUsuarios")
        self.menuPlantilla = QMenu(self.menubar)
        self.menuPlantilla.setObjectName(u"menuPlantilla")
        self.menuReportes = QMenu(self.menubar)
        self.menuReportes.setObjectName(u"menuReportes")
        self.menuAyuda = QMenu(self.menubar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuUsuarios.menuAction())
        self.menubar.addAction(self.menuPlantilla.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionAjustes)
        self.menuArchivo.addAction(self.actionCerrar_Session)
        self.menuUsuarios.addAction(self.actionEmpleados)
        self.menuUsuarios.addAction(self.actionUsuarios)
        self.menuPlantilla.addAction(self.actionClientes)
        self.menuPlantilla.addAction(self.actionProveedores)
        self.menuAyuda.addAction(self.actionAcerca_de)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Principal", None))
        self.actionAcerca_de.setText(QCoreApplication.translate("MainWindow", u"Acerca de", None))
        self.actionEmpleados.setText(QCoreApplication.translate("MainWindow", u"Empleados", None))
        self.actionUsuarios.setText(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.actionAjustes.setText(QCoreApplication.translate("MainWindow", u"Ajustes", None))
        self.actionCerrar_Session.setText(QCoreApplication.translate("MainWindow", u"Cerrar Sesion", None))
        self.actionClientes.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.actionProveedores.setText(QCoreApplication.translate("MainWindow", u"Proveedores", None))
        self.btnventa.setText(QCoreApplication.translate("MainWindow", u"Venta", None))
        self.btnreportes.setText(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.btncompra.setText(QCoreApplication.translate("MainWindow", u"Compra", None))
        self.btninventario.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Bienvenido", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuUsuarios.setTitle(QCoreApplication.translate("MainWindow", u"Usuarios", None))
        self.menuPlantilla.setTitle(QCoreApplication.translate("MainWindow", u"Plantilla", None))
        self.menuReportes.setTitle(QCoreApplication.translate("MainWindow", u"Reportes", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

