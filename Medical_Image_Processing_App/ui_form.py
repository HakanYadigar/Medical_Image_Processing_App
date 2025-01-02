# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QSlider, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(800, 600)
        self.widget_2 = QWidget(Widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(400, 60, 341, 311))
        self.pushButton_5 = QPushButton(Widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(220, 530, 171, 31))
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(500, 370, 141, 31))
        self.horizontalSlider_3 = QSlider(Widget)
        self.horizontalSlider_3.setObjectName(u"horizontalSlider_3")
        self.horizontalSlider_3.setGeometry(QRect(10, 510, 171, 20))
        self.horizontalSlider_3.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider = QSlider(Widget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(10, 430, 171, 20))
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(220, 490, 171, 31))
        self.horizontalSlider_2 = QSlider(Widget)
        self.horizontalSlider_2.setObjectName(u"horizontalSlider_2")
        self.horizontalSlider_2.setGeometry(QRect(10, 470, 171, 20))
        self.horizontalSlider_2.setOrientation(Qt.Orientation.Horizontal)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 410, 81, 20))
        self.pushButton_4 = QPushButton(Widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(220, 450, 171, 31))
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 490, 91, 20))
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 410, 171, 31))
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(300, 10, 161, 41))
        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(130, 370, 131, 21))
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 450, 91, 20))
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 60, 331, 311))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"Specturum", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"SELECT IMAGE", None))
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Detect Circle", None))
        self.label.setText(QCoreApplication.translate("Widget", u"Trunc Filter", None))
        self.pushButton_4.setText(QCoreApplication.translate("Widget", u"Precise Edge Detection", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"Blur Filter", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Edges", None))
        self.textEdit.setHtml(QCoreApplication.translate("Widget", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:700;\"> IMAGE FILTERING</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"ORIGINAL IMAGE", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"B\u0131nary Filter", None))
    # retranslateUi

