import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtGui import QTextDocument, QTextTableFormat, QTextCursor, QPageSize, QPdfWriter
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from ui_acercade import Ui_MainWindow
from PySide6.QtCore import Qt, QAbstractItemModel
from Conexion import Conexion  # Importar la conexión y el cursor

class AcercaDe(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        size = self.size()
        self.setMinimumSize(size)
        self.setMaximumSize(size)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = AcercaDe()
    widget.show()
    sys.exit(app.exec())
