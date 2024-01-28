import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QGridLayout, \
    QHBoxLayout, QMenuBar, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap, QFont
import planner



class OtthontervezoAblak(QMainWindow):
    def __init__(self, parent=None):
        super(OtthontervezoAblak, self).__init__(parent)

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

        # Funkció ikonok megjelenítése
        uj_terv_label=QLabel(self)
        uj_terv_kep=QPixmap("newPlan.png")
        uj_terv_label.setPixmap(uj_terv_kep)
        uj_terv_label.setAlignment(Qt.AlignHCenter)
        tartalom_elrendezes.addWidget(uj_terv_label, 1,0)
        uj_terv_label.mousePressEvent = self.ujTerv
        self.dialog = planner.Second(self)

        megnyitas_label = QLabel(self)
        megnyitas_kep = QPixmap("open.png")
        megnyitas_label.setPixmap(megnyitas_kep)
        megnyitas_label.setAlignment(Qt.AlignHCenter)
        tartalom_elrendezes.addWidget(megnyitas_label, 1,1)
        megnyitas_label.mousePressEvent = self.open

        export_label = QLabel(self)
        export_kep = QPixmap("export.png")
        export_label.setPixmap(export_kep)
        export_label.setAlignment(Qt.AlignHCenter)
        tartalom_elrendezes.addWidget(export_label, 1, 2)
        export_label.mousePressEvent = self.export

        self.setCentralWidget(tartalom_widget)

    def menuSor_keszitese(self):
        # Menübár alapja
        menuSor=QMenuBar(self)
        self.setMenuBar(menuSor)
        file_menu = menuSor.addMenu("Fájl")
        edit_menu=menuSor.addMenu("Szerkesztés")
        view_menu=menuSor.addMenu("Nézet")
        help_menu=menuSor.addMenu("Help")

        # File menu pontjai
        open = file_menu.addAction("Megnyitás")
        open.triggered.connect(self.menuOpen)
        last_opened = file_menu.addAction("Utoljára megnyitott")
        last_opened.triggered.connect(self.lastOpen)
        file_menu.addSeparator()
        save=file_menu.addAction("Mentés")
        save.triggered.connect(self.save)
        saveAs=file_menu.addAction("Mentés másként")
        saveAs.triggered.connect(self.saveAs)
        plan_export=file_menu.addAction("Terv exportálása")
        plan_export.triggered.connect(self.plan_export)
        file_menu.addSeparator()
        settings=file_menu.addAction("Beállítások")
        settings.triggered.connect(self.settings)
        file_menu.addSeparator()
        exit=file_menu.addAction("Kilépés")
        exit.triggered.connect(self.close)

    # Fájl menü funkciói
    def menuOpen(self):
        print("Menu nyomva")

    def lastOpen(self):
        print("Last open")

    def save(self):
        print("Mentés katt")

    def saveAs(self):
        print("Mentés másként katt")

    def export(self):
        print("Export katt")

    def plan_export(self):
        print("Terv Export katt")

    def settings(self):
        print("Settings")

    def closeEvent(self, event):
        quit_msg = "Biztosan ki szeretne lépni?"
        reply = QMessageBox.question(self, 'Figyelmeztetés', quit_msg, QMessageBox.Yes, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # Fő gombok
    def open(self, event):
        if event.button() == Qt.LeftButton:
            # Tallózási ablak megnyitása
            file_dialog = QFileDialog(self)
            file_dialog.setNameFilter("Text files (*.txt);;All files (*.*)")

            if file_dialog.exec_():
                selected_file = file_dialog.selectedFiles()[0]
                print(f"Kiválasztott fájl: {selected_file}")

#Itt valamai nem jó, mert nem marad nyitva az új ablak
    def ujTerv(self, event):
        if event.button() == Qt.LeftButton:
            print("Új terv katt")
            self.dialog.show()
            OtthontervezoAblak.hide(self)


    def export(self, event):
        if event.button() == Qt.LeftButton:
            print("Export katt")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ablak = OtthontervezoAblak()
    ablak.show()
    sys.exit(app.exec_())
