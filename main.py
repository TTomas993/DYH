import sys

import PyQt5.QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QGridLayout, \
    QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap, QFont


class OtthontervezoAblak(QMainWindow):
    def __init__(self):
        super().__init__()

        # Ablak beállításai
        self.setWindowTitle('DYH!')
        self.setGeometry(100, 100, 800, 600)

        # Menüsor felépítésa
        menu=self.menuBar()
        file_menu=menu.addMenu("File")
        open=file_menu.addAction("Megnyitás")
        open.triggered.connect(self.open)
        last_opened=file_menu.addMenu("Utoljára megnyitott")
        last_opened.triggered.connect(self.lastOpen)

        menu.addMenu("Edit")
        menu.addMenu("View")
        menu.addMenu("Help")



        # Fő tartalom elhelyezése
        tartalom_widget = QWidget()
        tartalom_elrendezes = QGridLayout(tartalom_widget)

        # Cím beállítása
        foCim = QLabel('Do Your Home!')
        foCim_meret=QFont()
        foCim_meret.setPointSize(60)
        foCim.setFont(foCim_meret)
        foCim.setAlignment(Qt.AlignCenter)
        tartalom_elrendezes.addWidget(foCim,0,0,0,3)

        # Funkció ikonok megjelenítése
        uj_terv_label=QLabel(self)
        uj_terv_kep=QPixmap("newPlan.png")
        uj_terv_label.setPixmap(uj_terv_kep)
        uj_terv_label.setAlignment(Qt.AlignCenter)
        tartalom_elrendezes.addWidget(uj_terv_label, 2,0)
        uj_terv_label.mousePressEvent = self.ujTerv

        megnyitas_label = QLabel(self)
        megnyitas_kep = QPixmap("open.png")
        megnyitas_label.setPixmap(megnyitas_kep)
        megnyitas_label.setAlignment(Qt.AlignCenter)
        tartalom_elrendezes.addWidget(megnyitas_label, 2,1)
        megnyitas_label.mousePressEvent = self.open

        export_label = QLabel(self)
        export_kep = QPixmap("export.png")
        export_label.setPixmap(export_kep)
        export_label.setAlignment(Qt.AlignCenter)
        tartalom_elrendezes.addWidget(export_label, 2, 2)
        export_label.mousePressEvent = self.export


        #tartalom_elrendezes.addWidget(ikonok_elrendezese)
        """
        layout=QGridLayout(self)
        layout.addWidget(uj_terv_label, 10, 5)
        layout.addWidget(megnyitas_label, 0, 1)

        layout.setAlignment(Qt.AlignCenter)
        """
        """
        gomb = QPushButton('Nyitás')
        gomb.clicked.connect(self.nyit_alkalmazas)
        tartalom_elrendezes.addWidget(gomb)
        """
        self.setCentralWidget(tartalom_widget)

    def open(self, event):
        if event.button() == Qt.LeftButton:
            print('Az alkalmazás nyitása...')

    def lastOpen(self):
        print("Last open")

    def ujTerv(self, event):
        if event.button() == Qt.LeftButton:
            print("Új terv katt")

    def export(self, event):
        if event.button() == Qt.LeftButton:
            print("Export katt")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ablak = OtthontervezoAblak()
    ablak.show()
    sys.exit(app.exec_())
