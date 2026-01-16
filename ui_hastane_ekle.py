# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'hastane_ekle.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(939, 468)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(340, 20, 201, 41))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.HastaneEkle_button = QPushButton(Form)
        self.HastaneEkle_button.setObjectName(u"HastaneEkle_button")
        self.HastaneEkle_button.setGeometry(QRect(130, 380, 121, 51))
        self.HastaneEkle_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #324f9e;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #3f63c8;\n"
"}\n"
"\n"
"/* Bas\u0131l\u0131 tutarken */\n"
"QPushButton:pressed {\n"
"    background-color: #2a3d78;\n"
"}\n"
"")
        self.HastaneAdi_line = QLineEdit(Form)
        self.HastaneAdi_line.setObjectName(u"HastaneAdi_line")
        self.HastaneAdi_line.setGeometry(QRect(20, 240, 191, 61))
        self.HastaneAdi_line.setStyleSheet(u"QLineEdit {\n"
"    background: rgba(20, 30, 60, 0.6);\n"
"    color: #d6e0ff;\n"
"    border: 1px solid #2a3c63;\n"
"    border-radius: 10px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Placeholder rengi */\n"
"QLineEdit[echoMode=\"0\"] {\n"
"    color: #9aa8d4;\n"
"}\n"
"\n"
"/* Focus oldu\u011funda */\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4d79ff;\n"
"    background: rgba(30, 45, 90, 0.8);\n"
"}\n"
"")
        self.sehir_line = QLineEdit(Form)
        self.sehir_line.setObjectName(u"sehir_line")
        self.sehir_line.setGeometry(QRect(20, 130, 181, 61))
        self.sehir_line.setStyleSheet(u"QLineEdit {\n"
"    background: rgba(20, 30, 60, 0.6);\n"
"    color: #d6e0ff;\n"
"    border: 1px solid #2a3c63;\n"
"    border-radius: 10px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Placeholder rengi */\n"
"QLineEdit[echoMode=\"0\"] {\n"
"    color: #9aa8d4;\n"
"}\n"
"\n"
"/* Focus oldu\u011funda */\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4d79ff;\n"
"    background: rgba(30, 45, 90, 0.8);\n"
"}\n"
"")
        self.hastane_table = QTableWidget(Form)
        if (self.hastane_table.columnCount() < 3):
            self.hastane_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.hastane_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.hastane_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.hastane_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.hastane_table.setObjectName(u"hastane_table")
        self.hastane_table.setEnabled(True)
        self.hastane_table.setGeometry(QRect(480, 150, 401, 192))
        self.hastane_table.setStyleSheet(u"QTableWidget {\n"
"    background: rgba(10,20,40,0.6);\n"
"    color: #d6e0ff;\n"
"    border: 1px solid #1f2a44;\n"
"    border-radius: 10px;\n"
"    gridline-color: #2a3c63;\n"
"    font-size: 14px;\n"
"    selection-background-color: #324f9e;\n"
"    selection-color: white;\n"
"}\n"
"\n"
"/* Header */\n"
"QHeaderView::section {\n"
"    background-color: #1f2a44;\n"
"    color: #c7d2ff;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* Alternating row colors */\n"
"QTableWidget::item {\n"
"    background-color: #111b31;\n"
"}\n"
"\n"
"QTableWidget::item:alternate {\n"
"    background-color: #16223d;\n"
"}\n"
"\n"
"/* Selected row */\n"
"QTableWidget::item:selected {\n"
"    background-color: #3f63c8;\n"
"    color: white;\n"
"}\n"
"")
        self.HastaneGuncelle_button = QPushButton(Form)
        self.HastaneGuncelle_button.setObjectName(u"HastaneGuncelle_button")
        self.HastaneGuncelle_button.setGeometry(QRect(260, 380, 121, 51))
        self.HastaneGuncelle_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #324f9e;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #3f63c8;\n"
"}\n"
"\n"
"/* Bas\u0131l\u0131 tutarken */\n"
"QPushButton:pressed {\n"
"    background-color: #2a3d78;\n"
"}\n"
"")
        self.HastaneSil_button = QPushButton(Form)
        self.HastaneSil_button.setObjectName(u"HastaneSil_button")
        self.HastaneSil_button.setGeometry(QRect(390, 380, 141, 51))
        self.HastaneSil_button.setStyleSheet(u"QPushButton {\n"
"    background-color: #324f9e;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"/* Hover */\n"
"QPushButton:hover {\n"
"    background-color: #3f63c8;\n"
"}\n"
"\n"
"/* Bas\u0131l\u0131 tutarken */\n"
"QPushButton:pressed {\n"
"    background-color: #2a3d78;\n"
"}\n"
"")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 210, 181, 21))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 90, 171, 31))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"HASTANE EKLE", None))
        self.HastaneEkle_button.setText(QCoreApplication.translate("Form", u"Ekle", None))
        ___qtablewidgetitem = self.hastane_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.hastane_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Hastane Ad\u0131", None));
        ___qtablewidgetitem2 = self.hastane_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"\u015eehir", None));
        self.HastaneGuncelle_button.setText(QCoreApplication.translate("Form", u"G\u00fcncelle", None))
        self.HastaneSil_button.setText(QCoreApplication.translate("Form", u"Hastane Sil", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Hastane Ad\u0131 giriniz:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u015eehir giriniz:", None))
    # retranslateUi

