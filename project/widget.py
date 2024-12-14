# This Python file uses the following encoding: utf-8
import sys
import cv2
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.original_image = None
        self.current_image = None  # Geçici filtrelenmiş görüntü için

        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(255)
        self.ui.horizontalSlider.setValue(127)
        self.ui.horizontalSlider_2.setMinimum(0)
        self.ui.horizontalSlider_2.setMaximum(255)
        self.ui.horizontalSlider_2.setValue(127)

        self.ui.pushButton.clicked.connect(self.open_image)
        self.ui.horizontalSlider.valueChanged.connect(self.apply_combined_filters)
        self.ui.horizontalSlider_2.valueChanged.connect(self.apply_combined_filters)
        self.ui.pushButton_2.clicked.connect(self.apply_blur)

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Resim Seç",
            "",
            "Resim_Dosyaları(*.png *.jpg *.jpeg *.bmp *.tiff)"
        )
        if file_name:
            self.original_image = cv2.imread(file_name)
            self.current_image = self.original_image.copy()  # Geçici görüntüyü ayarla
            cv2.imwrite('sonuc.png', self.original_image)
            self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")

    def apply_combined_filters(self):
        if self.original_image is None:
            return

        min_value = self.ui.horizontalSlider.value()
        max_value = self.ui.horizontalSlider_2.value()

        # Use the original image to avoid accumulating effects
        temp_image = self.original_image.copy()

        # Apply threshold filter based on the sliders
        gray = cv2.cvtColor(temp_image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, min_value, 255, cv2.THRESH_TRUNC)

        # Apply second filter (binary threshold)
        _, second_thresh = cv2.threshold(thresh, max_value, 255, cv2.THRESH_BINARY)
        self.current_image = cv2.cvtColor(second_thresh, cv2.COLOR_GRAY2BGR)

        cv2.imwrite('sonuc.png', self.current_image)
        self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")

    def apply_blur(self):
        if self.current_image is None:
            return

        # Apply Gaussian blur on the current image
        self.current_image = cv2.GaussianBlur(self.current_image, (15, 15), 0)
        cv2.imwrite('sonuc.png', self.current_image)
        self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
