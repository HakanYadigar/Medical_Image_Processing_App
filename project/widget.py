# This Python file uses the following encoding: utf-8
import sys
import cv2
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.goster)

    def goster(self):
        dosya_yolu, _ =QFileDialog.getOpenFileName(
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
