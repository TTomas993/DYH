import sys


from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QGridLayout, \
    QHBoxLayout, QMenuBar, QMessageBox, QFileDialog, QAction, QDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap, QFont


class Planner(QWidget):
    def __init__(self, parent=None):
        super(Planner, self).__init__(parent)
        label = QLabel("Sub Window", self)
        label.setGeometry(0, 0, 20, 10)
        self.show()


