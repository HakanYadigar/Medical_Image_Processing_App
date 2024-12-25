import sys
import cv2
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from ui_form import Ui_Widget
import matplotlib.pyplot as plt

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
        self.ui.horizontalSlider_3.setMinimum(0)
        self.ui.horizontalSlider_3.setMaximum(30)
        self.ui.horizontalSlider_3.setValue(0)

        self.ui.pushButton.clicked.connect(self.open_image)
        self.ui.horizontalSlider.valueChanged.connect(self.apply_filter_1)
        self.ui.horizontalSlider_2.valueChanged.connect(self.apply_filter_2)
        self.ui.pushButton_2.clicked.connect(self.apply_edges)
        self.ui.horizontalSlider_3.valueChanged.connect(self.apply_blur)

    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Resim Seç",
            "",
            "Resim_Dosyaları(*.png *.jpg *.jpeg *.bmp *.tiff)"
        )
        if file_name:
            self.original_image = cv2.imread(file_name)
            if self.original_image is not None:  # Görüntü yüklendiyse
                self.current_image = self.original_image.copy()  # Geçici görüntüyü ayarla
                cv2.imwrite('sonuc.png', self.original_image)
                self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")
            else:
                print("Hata: Resim yüklenemedi. Dosya bozuk olabilir.")
        else:
            print("Hata: Bir dosya seçilmedi.")

    def apply_filter_1(self):
        if self.current_image is None:
            return

        min_value = self.ui.horizontalSlider.value()

        # Original image üzerinden işlem yap!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, min_value, 255, cv2.THRESH_TRUNC)
        self.current_image = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

        cv2.imwrite('sonuc.png', self.current_image)
        self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")

    def apply_filter_2(self):
        if self.current_image is None:
            return

        max_value = self.ui.horizontalSlider_2.value()

        # Original image üzerinden işlem yap !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        _, second_thresh = cv2.threshold(gray, max_value, 255, cv2.THRESH_BINARY)
        self.current_image = cv2.cvtColor(second_thresh, cv2.COLOR_GRAY2BGR)

        cv2.imwrite('sonuc.png', self.current_image)
        self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")

    def apply_blur(self):
        if self.current_image is None:
            return

        blur_value = self.ui.horizontalSlider_3.value()
        if blur_value % 2 == 0:  # GaussianBlur kernel boyutu tek olmalı
            blur_value += 1

        # Current image üzerinden işlem yap
        blurred_image = cv2.GaussianBlur(self.current_image, (blur_value, blur_value), 0)
        self.current_image = blurred_image

        cv2.imwrite('sonuc.png', self.current_image)
        self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")

    def apply_edges(self):
        if self.original_image is None:
            return

        # Apply edges filter
        edges = cv2.Canny(image=self.original_image, threshold1=100, threshold2=700)

        # Create subplots
        fig, axs = plt.subplots(1, 2, figsize=(7, 4))

        # Plot the original image
        axs[0].imshow(cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB))
        axs[0].set_title('Original Image')

        # Plot the blurred image
        axs[1].imshow(edges, cmap='gray')
        axs[1].set_title('Image edges')

        # Remove ticks from the subplots
        for ax in axs:
            ax.set_xticks([])
            ax.set_yticks([])

        # Display the subplots
        plt.tight_layout()
        plt.show()

        cv2.imwrite('sonuc.png', self.original_image)
        self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
