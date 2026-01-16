# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'poliklinik_ekle.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(914, 467)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 30, 521, 71))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 30px;\n"
"}\n"
"")
        self.hastaneler_combo = QComboBox(Form)
        self.hastaneler_combo.setObjectName(u"hastaneler_combo")
        self.hastaneler_combo.setGeometry(QRect(20, 140, 261, 51))
        self.hastaneler_combo.setStyleSheet(u"/* =========================\n"
"   COMBOBOX - MODERN ST\u0130L\n"
"   ========================= */\n"
"\n"
"QComboBox {\n"
"    background: rgba(20, 30, 60, 0.6);\n"
"    color: #d6e0ff;\n"
"    border: 1px solid #2a3c63;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* \u00dczerine gelince */\n"
"QComboBox:hover {\n"
"    border: 1px solid #4d79ff;\n"
"}\n"
"\n"
"/* Se\u00e7im yaparken (focus) */\n"
"QComboBox:focus {\n"
"    border: 1px solid #6d8cff;\n"
"    background: rgba(30, 45, 90, 0.7);\n"
"}\n"
"\n"
"/* A\u015fa\u011f\u0131 ok butonu */\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"    width: 28px;\n"
"}\n"
"\n"
"/* Ok simgesi alan\u0131 */\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 0px;\n"
"    height: 0px;\n"
"    border-left: 6px solid #a8b9ff;\n"
"    border-top: 4px solid transparent;\n"
"    border-bottom: 4px solid transparent;\n"
"    margin-right: 8px;\n"
"}\n"
"\n"
"/* A\u00e7\u0131l\u0131r liste */\n"
"QComboBox "
                        "QAbstractItemView {\n"
"    background-color: #0f1729;\n"
"    color: #d6e0ff;\n"
"    border: 1px solid #2a3c63;\n"
"    selection-background-color: #324f9e;\n"
"    selection-color: white;\n"
"    outline: 0;\n"
"}\n"
"\n"
"")
        self.klinik_line = QLineEdit(Form)
        self.klinik_line.setObjectName(u"klinik_line")
        self.klinik_line.setGeometry(QRect(20, 250, 261, 51))
        self.klinik_line.setStyleSheet(u"QLineEdit {\n"
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
        self.kaydet_klinik = QPushButton(Form)
        self.kaydet_klinik.setObjectName(u"kaydet_klinik")
        self.kaydet_klinik.setGeometry(QRect(120, 370, 111, 51))
        self.kaydet_klinik.setStyleSheet(u"QPushButton {\n"
"    background-color: #324f9e;\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3f63c8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2a3d78;\n"
"}\n"
"")
        self.poliklinik_table = QTableWidget(Form)
        if (self.poliklinik_table.columnCount() < 3):
            self.poliklinik_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.poliklinik_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.poliklinik_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.poliklinik_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.poliklinik_table.setObjectName(u"poliklinik_table")
        self.poliklinik_table.setGeometry(QRect(480, 120, 371, 192))
        self.poliklinik_table.setStyleSheet(u"QTableWidget {\n"
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
        self.poliklinik_table.setAlternatingRowColors(True)
        self.klinik_guncelle = QPushButton(Form)
        self.klinik_guncelle.setObjectName(u"klinik_guncelle")
        self.klinik_guncelle.setGeometry(QRect(350, 370, 111, 51))
        self.klinik_guncelle.setStyleSheet(u"QPushButton {\n"
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
        self.klinik_sil = QPushButton(Form)
        self.klinik_sil.setObjectName(u"klinik_sil")
        self.klinik_sil.setGeometry(QRect(240, 370, 101, 51))
        self.klinik_sil.setStyleSheet(u"QPushButton {\n"
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
        self.label_2.setGeometry(QRect(20, 110, 151, 16))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 210, 211, 31))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(490, 330, 331, 31))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"POL\u0130KL\u0130N\u0130K EKLE", None))
        self.kaydet_klinik.setText(QCoreApplication.translate("Form", u"Kaydet", None))
        ___qtablewidgetitem = self.poliklinik_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.poliklinik_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Poliklinik Ad\u0131", None));
        ___qtablewidgetitem2 = self.poliklinik_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Hastane", None));
        self.klinik_guncelle.setText(QCoreApplication.translate("Form", u"G\u00fcncelle", None))
        self.klinik_sil.setText(QCoreApplication.translate("Form", u"Sil", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Hastane Se\u00e7iniz:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Poliklinik Ad\u0131:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"D\u00fczenlemek / silmek istedi\u011finiz veriye t\u0131klay\u0131n.", None))
    # retranslateUi

