import sys
import cv2
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from ui_form import Ui_Widget
import matplotlib.pyplot as plt
import numpy as np

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.original_image = None
        self.current_image = None  # For temporally filtered image

        # Setting the values ​​of sliders.
        self.ui.horizontalSlider.setMinimum(0)
        self.ui.horizontalSlider.setMaximum(255)
        self.ui.horizontalSlider.setValue(127)
        self.ui.horizontalSlider_2.setMinimum(0)
        self.ui.horizontalSlider_2.setMaximum(255)
        self.ui.horizontalSlider_2.setValue(127)
        self.ui.horizontalSlider_3.setMinimum(0)
        self.ui.horizontalSlider_3.setMaximum(30)
        self.ui.horizontalSlider_3.setValue(0)

        # Defining sliders and buttons.
        self.ui.pushButton.clicked.connect(self.open_image)
        self.ui.horizontalSlider.valueChanged.connect(self.apply_filter_1)
        self.ui.horizontalSlider_2.valueChanged.connect(self.apply_filter_2)
        self.ui.pushButton_2.clicked.connect(self.apply_edges)
        self.ui.horizontalSlider_3.valueChanged.connect(self.apply_blur)
        self.ui.pushButton_3.clicked.connect(self.apply_circle)
        self.ui.pushButton_4.clicked.connect(self.apply_precise_edge)
        self.ui.pushButton_5.clicked.connect(self.magnitude_spectrum)


    # Opening the image from file.
    def open_image(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Select image",
            "",
            "Image_Files(*.png *.jpg *.jpeg *.bmp *.tiff)"
        )
        if file_name:
            self.original_image = cv2.imread(file_name)
            if self.original_image is not None:  # If the image is uploaded
                cv2.imwrite('original_image.png', self.original_image)
                cv2.imwrite('sonuc.png', self.original_image)
                self.current_image = cv2.imread('sonuc.png')
                self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")
                self.ui.widget.setStyleSheet("border-image: url(original_image.png);")
            else:
                print("Error: Could not load image. The file may be corrupt.")
        else:
            print("Error: A file was not selected.")


    # Applying TRUNC filter.
    def apply_filter_1(self):
        if self.current_image is None:
            return
        min_value = self.ui.horizontalSlider.value()

        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, min_value, 255, cv2.THRESH_TRUNC)
        self.current_image = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)

        cv2.imwrite('sonuc.png', self.current_image)
        self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")



    # Applying BINARY filter.
    def apply_filter_2(self):
        if self.current_image is None:
            return

        max_value = self.ui.horizontalSlider_2.value()
        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        _, second_thresh = cv2.threshold(gray, max_value, 255, cv2.THRESH_BINARY)
        self.current_image = cv2.cvtColor(second_thresh, cv2.COLOR_GRAY2BGR)

        cv2.imwrite('sonuc.png', self.current_image)
        self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")


    # Applying Blur filter.
    def apply_blur(self):
        if self.current_image is None:
            return

        blur_value = self.ui.horizontalSlider_3.value()
        if blur_value % 2 == 0:  # GaussianBlur kernel size must be odd
            blur_value += 1
        self.apply_filter_1()
        self.apply_filter_2()
        self.current_image = cv2.imread('sonuc.png')

        blurred_image = cv2.GaussianBlur(self.current_image, (blur_value, blur_value), 0)
        self.current_image = blurred_image

        cv2.imwrite('sonuc.png', self.current_image)
        self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")



    # Applying adge detection.
    def apply_edges(self):
        if self.original_image is None:
            return

        edges = cv2.Canny(image=self.original_image, threshold1=100, threshold2=700)

        fig, axs = plt.subplots(1, 2, figsize=(7, 4))

        axs[0].imshow(cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB))
        axs[0].set_title('Original Image')

        axs[1].imshow(edges, cmap='gray')
        axs[1].set_title('Image edges')

        for ax in axs:
            ax.set_xticks([])
            ax.set_yticks([])

        plt.tight_layout()
        plt.show()

        cv2.imwrite('sonuc.png', self.original_image)
        self.ui.widget_2.setStyleSheet("border-image: url(sonuc.png);")



    # Checking if image is X ray or MR image or not.
    def is_grayscale(self, image):
        if len(image.shape) < 3 or image.shape[2] == 1:
            return True
        b, g, r = cv2.split(image)
        if np.array_equal(b, g) and np.array_equal(b, r):
            return True
        return False


    # Applying circle detection.
    def apply_circle(self):
        if not self.is_grayscale(self.original_image):
            QMessageBox.warning(self, "Warning", "This is not an MRI/X-Ray image. Circle detection does not work properly on such images. Please try a different option.")
            return

        gray = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
        gray_blurred = cv2.blur(gray, (3, 3))

        detected_circles = cv2.HoughCircles(
            gray_blurred,
            cv2.HOUGH_GRADIENT,
            1,
            20,
            param1=50,
            param2=30,
            minRadius=20,  # Minimum circle radius increased. In this way, small spots will not be identified.

            maxRadius=40
        )
        if detected_circles is not None:
            detected_circles = np.uint16(np.around(detected_circles))
            if len(detected_circles[0]) > 10: # If there are more than 10 detected circles, a warning message appears.
                QMessageBox.warning(self, "Warning", "More than 10 circles detected in the image. The transaction has been cancelled.")
                return

            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                cv2.circle(self.current_image, (a, b), r, (0, 0, 255), 2)
                cv2.circle(self.current_image, (a, b), 1, (255, 0, 0), 3)

            cv2.imshow("Detected Circles", self.current_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()



    # Applying precise edge detection
    def apply_precise_edge(self):
        if self.original_image is None:
            return

        scharr_x = cv2.Scharr(self.original_image, cv2.CV_64F, 1, 0)
        scharr_y = cv2.Scharr(self.original_image, cv2.CV_64F, 0, 1)
        cv2.imshow("Precise edge detected image", scharr_x)



    # Applying spectrum.
    def magnitude_spectrum(self):
        if self.current_image is None:
            print("Error: Image not loaded.")
            return

        gray_image = cv2.cvtColor(self.current_image, cv2.COLOR_BGR2GRAY)
        float_image = np.float32(gray_image)

        dft = cv2.dft(float_image, flags=cv2.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)

        magnitude = cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])
        magnitude_spectrum = 20 * np.log(magnitude + 1)

        magnitude_spectrum_normalized = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
        magnitude_spectrum_normalized = np.uint8(magnitude_spectrum_normalized)

        cv2.imshow("Magnitude Spectrum", magnitude_spectrum_normalized)
        cv2.imwrite('magnitude_spectrum.png', magnitude_spectrum_normalized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
