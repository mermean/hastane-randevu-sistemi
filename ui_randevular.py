# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randevular.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTimeEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1073, 531)
        self.randevu_table = QTableWidget(Form)
        self.randevu_table.setObjectName(u"randevu_table")
        self.randevu_table.setGeometry(QRect(310, 130, 721, 191))
        self.randevu_table.setStyleSheet(u"QTableWidget {\n"
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
        self.adsoyad_line = QLineEdit(Form)
        self.adsoyad_line.setObjectName(u"adsoyad_line")
        self.adsoyad_line.setGeometry(QRect(30, 180, 211, 51))
        self.adsoyad_line.setStyleSheet(u"QLineEdit {\n"
"    background: rgba(10,20,40,0.6);\n"
"    color: #e8eeff;\n"
"    border: 1px solid #1f2a44;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #3f63c8;\n"
"    background: rgba(20,30,60,0.8);\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #aab7e8;\n"
"}\n"
"")
        self.tc_line = QLineEdit(Form)
        self.tc_line.setObjectName(u"tc_line")
        self.tc_line.setGeometry(QRect(30, 280, 211, 51))
        self.tc_line.setStyleSheet(u"QLineEdit {\n"
"    background: rgba(10,20,40,0.6);\n"
"    color: #e8eeff;\n"
"    border: 1px solid #1f2a44;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #3f63c8;\n"
"    background: rgba(20,30,60,0.8);\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #aab7e8;\n"
"}\n"
"")
        self.tarih_edit = QDateEdit(Form)
        self.tarih_edit.setObjectName(u"tarih_edit")
        self.tarih_edit.setGeometry(QRect(30, 440, 141, 41))
        self.tarih_edit.setStyleSheet(u"QDateEdit {\n"
"    background: rgba(10,20,40,0.6);\n"
"    color: #e8eeff;\n"
"    border: 1px solid #1f2a44;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 1px solid #3f63c8;\n"
"}\n"
"\n"
"QDateEdit::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: right;\n"
"    width: 20px;\n"
"    border-left: 1px solid #1f2a44;\n"
"}\n"
"\n"
"QDateEdit::down-arrow {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"")
        self.saat_edit = QTimeEdit(Form)
        self.saat_edit.setObjectName(u"saat_edit")
        self.saat_edit.setGeometry(QRect(180, 440, 151, 41))
        self.saat_edit.setStyleSheet(u"QTimeEdit {\n"
"    background: rgba(10,20,40,0.6);\n"
"    color: #e8eeff;\n"
"    border: 1px solid #1f2a44;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"    border: 1px solid #3f63c8;\n"
"}\n"
"\n"
"QTimeEdit::up-button,\n"
"QTimeEdit::down-button {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QTimeEdit::up-arrow,\n"
"QTimeEdit::down-arrow {\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"")
        self.guncelle_button = QPushButton(Form)
        self.guncelle_button.setObjectName(u"guncelle_button")
        self.guncelle_button.setGeometry(QRect(510, 340, 161, 51))
        self.guncelle_button.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1:0 y1:0,\n"
"        x2:1 y2:1,\n"
"        stop:0 #2a3c63,\n"
"        stop:1 #3f63c8\n"
"    );\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"    font-size: 14px;\n"
"    border: 1px solid #324f9e;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0 y1:0,\n"
"        x2:1 y2:1,\n"
"        stop:0 #3f63c8,\n"
"        stop:1 #4f7fff\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #22345a;\n"
"}\n"
"")
        self.sil_button = QPushButton(Form)
        self.sil_button.setObjectName(u"sil_button")
        self.sil_button.setGeometry(QRect(510, 400, 161, 51))
        self.sil_button.setStyleSheet(u"QPushButton {\n"
"    background: qlineargradient(\n"
"        x1:0 y1:0,\n"
"        x2:1 y2:1,\n"
"        stop:0 #2a3c63,\n"
"        stop:1 #3f63c8\n"
"    );\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 14px;\n"
"    font-size: 14px;\n"
"    border: 1px solid #324f9e;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(\n"
"        x1:0 y1:0,\n"
"        x2:1 y2:1,\n"
"        stop:0 #3f63c8,\n"
"        stop:1 #4f7fff\n"
"    );\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: #22345a;\n"
"}\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(390, 40, 201, 41))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 130, 201, 41))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 240, 181, 31))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 20px;\n"
"}\n"
"")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 400, 181, 31))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 20px;\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.guncelle_button.setText(QCoreApplication.translate("Form", u"G\u00fcncelle", None))
        self.sil_button.setText(QCoreApplication.translate("Form", u"Sil", None))
        self.label.setText(QCoreApplication.translate("Form", u"RANDEVULAR", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Hasta Ad\u0131 Soyad\u0131:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Hasta TC:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Randevu Tarihi:", None))
    # retranslateUi

