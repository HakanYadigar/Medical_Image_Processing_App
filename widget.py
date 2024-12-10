# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from ui_form import Ui_Widget  # ui_form.py dosyasını doğru oluşturduğunuzdan emin olun


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.resim_sec_ve_ac)

    def resim_sec_ve_ac(self):

        dosya_yolu, _ = QFileDialog.getOpenFileName(
            self,
            "Bir resim seçin",
            "",
            "Resim Dosyaları (*.png *.jpg *.jpeg *.bmp *.tiff)"
        )
        if dosya_yolu:
            resim = cv2.imread(dosya_yolu)
            cv2.imshow("Seçilen Resim", resim)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("Herhangi bir dosya seçilmedi.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
