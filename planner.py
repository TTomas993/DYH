import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QGridLayout, \
    QHBoxLayout, QMenuBar, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap, QFont


class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)

        # Menüsor inicializálása
        self.menuSor_keszitese()

        # Ablak beállításai
        self.setWindowTitle('DYH!')
        self.setWindowIcon(QIcon("Icon.png"))
        self.setGeometry(100, 100, 800, 600)

        # Fő tartalom elhelyezése
        tartalom_widget = QWidget()
        tartalom_elrendezes = QGridLayout(tartalom_widget)

        # Cím beállítása
        foCim = QLabel('Do Your Home!')
        foCim_meret=QFont()
        foCim_meret.setPointSize(60)
        foCim.setFont(foCim_meret)
        foCim.setAlignment(Qt.AlignHCenter)
        tartalom_elrendezes.addWidget(foCim,0,0,0,3)

    def menuSor_keszitese(self):
        # Menübár alapja
        menuSor = QMenuBar(self)
        self.setMenuBar(menuSor)
        file_menu = menuSor.addMenu("Fájl")
        edit_menu = menuSor.addMenu("Szerkesztés")
        view_menu = menuSor.addMenu("Nézet")
        help_menu = menuSor.addMenu("Help")