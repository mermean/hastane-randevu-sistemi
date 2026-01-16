# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doktorekle.ui'
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
        Form.resize(764, 481)
        self.doktoradi_line = QLineEdit(Form)
        self.doktoradi_line.setObjectName(u"doktoradi_line")
        self.doktoradi_line.setGeometry(QRect(20, 150, 201, 41))
        self.doktoradi_line.setStyleSheet(u"QLineEdit {\n"
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
        self.hastane_combo = QComboBox(Form)
        self.hastane_combo.setObjectName(u"hastane_combo")
        self.hastane_combo.setGeometry(QRect(20, 220, 201, 41))
        self.hastane_combo.setStyleSheet(u"/* =========================\n"
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
        self.poliklinik_combo = QComboBox(Form)
        self.poliklinik_combo.setObjectName(u"poliklinik_combo")
        self.poliklinik_combo.setGeometry(QRect(20, 300, 201, 41))
        self.poliklinik_combo.setStyleSheet(u"/* =========================\n"
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
        self.doktor_ekle = QPushButton(Form)
        self.doktor_ekle.setObjectName(u"doktor_ekle")
        self.doktor_ekle.setGeometry(QRect(110, 380, 111, 41))
        self.doktor_ekle.setStyleSheet(u"QPushButton {\n"
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
        self.doktor_sil = QPushButton(Form)
        self.doktor_sil.setObjectName(u"doktor_sil")
        self.doktor_sil.setGeometry(QRect(230, 380, 111, 41))
        self.doktor_sil.setStyleSheet(u"QPushButton {\n"
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
        self.doktor_guncelle = QPushButton(Form)
        self.doktor_guncelle.setObjectName(u"doktor_guncelle")
        self.doktor_guncelle.setGeometry(QRect(350, 380, 131, 41))
        self.doktor_guncelle.setStyleSheet(u"QPushButton {\n"
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
        self.doktor_table = QTableWidget(Form)
        if (self.doktor_table.columnCount() < 4):
            self.doktor_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.doktor_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.doktor_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.doktor_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.doktor_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.doktor_table.setObjectName(u"doktor_table")
        self.doktor_table.setGeometry(QRect(300, 120, 461, 221))
        self.doktor_table.setStyleSheet(u"QTableWidget {\n"
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
        self.doktor_table.setAlternatingRowColors(True)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 141, 31))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 190, 141, 31))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 260, 141, 31))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(260, 30, 141, 31))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 20px;\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.doktor_ekle.setText(QCoreApplication.translate("Form", u"Ekle", None))
        self.doktor_sil.setText(QCoreApplication.translate("Form", u"Sil", None))
        self.doktor_guncelle.setText(QCoreApplication.translate("Form", u"G\u00fcncelle", None))
        ___qtablewidgetitem = self.doktor_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.doktor_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"New Column", None));
        ___qtablewidgetitem2 = self.doktor_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Doktor Ad\u0131", None));
        ___qtablewidgetitem3 = self.doktor_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Hastane", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"Doktor Ad\u0131 giriniz:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Hastane se\u00e7iniz:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Poliklinik se\u00e7iniz:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"DOKTOR EKLE", None))
    # retranslateUi

