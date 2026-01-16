# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'randevual.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTimeEdit,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(793, 454)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 0, 311, 71))
        self.label.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 25px;\n"
"}\n"
"")
        self.adsoyad_line = QLineEdit(Form)
        self.adsoyad_line.setObjectName(u"adsoyad_line")
        self.adsoyad_line.setGeometry(QRect(10, 100, 201, 51))
        self.adsoyad_line.setStyleSheet(u"QLineEdit {\n"
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
        self.tc_line = QLineEdit(Form)
        self.tc_line.setObjectName(u"tc_line")
        self.tc_line.setGeometry(QRect(10, 200, 191, 41))
        self.tc_line.setStyleSheet(u"QLineEdit {\n"
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
        self.dogum_date = QDateEdit(Form)
        self.dogum_date.setObjectName(u"dogum_date")
        self.dogum_date.setGeometry(QRect(10, 290, 181, 41))
        self.dogum_date.setStyleSheet(u"QDateEdit {\n"
"    background-color: rgba(15, 23, 41, 0.7);\n"
"    border: 1px solid #2a3c63;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    color: #d6e0ff;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 1px solid #3c5aa6;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 1px solid #5f8cff;\n"
"    background-color: rgba(20, 30, 60, 0.9);\n"
"}\n"
"\n"
"/* A\u00e7\u0131l\u0131r ok butonu */\n"
"QDateEdit::drop-down {\n"
"    border: none;\n"
"    width: 22px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Ok simgesi alan\u0131 */\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/qt-project.org/styles/commonstyle/images/arrowdown.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Takvim popup */\n"
"QCalendarWidget {\n"
"    background-color: #0f1729;\n"
"    border: 1px solid #2a3c63;\n"
"    color: #e3e7ff;\n"
"}\n"
"\n"
"/* G\u00fcn ba\u015fl\u0131klar\u0131 */\n"
"QCalendarWidget QWidget {\n"
"    alternate-background-color: #13203b;\n"
"}"
                        "\n"
"\n"
"/* G\u00fcnler */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    selection-background-color: #3f63c8;\n"
"    selection-color: white;\n"
"    background-color: #0f1729;\n"
"    color: #d6e0ff;\n"
"    outline: 0;\n"
"}\n"
"\n"
"/* Hover efekti */\n"
"QCalendarWidget QAbstractItemView:item:hover {\n"
"    background-color: #243a70;\n"
"}\n"
"\n"
"/* Bug\u00fcn vurgusu */\n"
"QCalendarWidget QAbstractItemView:item:selected {\n"
"    background-color: #4f7fff;\n"
"    color: white;\n"
"}\n"
"")
        self.cinsiyet_combo = QComboBox(Form)
        self.cinsiyet_combo.addItem("")
        self.cinsiyet_combo.addItem("")
        self.cinsiyet_combo.addItem("")
        self.cinsiyet_combo.setObjectName(u"cinsiyet_combo")
        self.cinsiyet_combo.setGeometry(QRect(10, 380, 191, 51))
        self.cinsiyet_combo.setStyleSheet(u"/* =========================\n"
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
        self.randevu_date = QDateEdit(Form)
        self.randevu_date.setObjectName(u"randevu_date")
        self.randevu_date.setGeometry(QRect(250, 110, 121, 41))
        self.randevu_date.setStyleSheet(u"QDateEdit {\n"
"    background-color: rgba(15, 23, 41, 0.7);\n"
"    border: 1px solid #2a3c63;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    color: #d6e0ff;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QDateEdit:hover {\n"
"    border: 1px solid #3c5aa6;\n"
"}\n"
"\n"
"QDateEdit:focus {\n"
"    border: 1px solid #5f8cff;\n"
"    background-color: rgba(20, 30, 60, 0.9);\n"
"}\n"
"\n"
"/* A\u00e7\u0131l\u0131r ok butonu */\n"
"QDateEdit::drop-down {\n"
"    border: none;\n"
"    width: 22px;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
"/* Ok simgesi alan\u0131 */\n"
"QDateEdit::down-arrow {\n"
"    image: url(:/qt-project.org/styles/commonstyle/images/arrowdown.png);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"}\n"
"\n"
"/* Takvim popup */\n"
"QCalendarWidget {\n"
"    background-color: #0f1729;\n"
"    border: 1px solid #2a3c63;\n"
"    color: #e3e7ff;\n"
"}\n"
"\n"
"/* G\u00fcn ba\u015fl\u0131klar\u0131 */\n"
"QCalendarWidget QWidget {\n"
"    alternate-background-color: #13203b;\n"
"}"
                        "\n"
"\n"
"/* G\u00fcnler */\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    selection-background-color: #3f63c8;\n"
"    selection-color: white;\n"
"    background-color: #0f1729;\n"
"    color: #d6e0ff;\n"
"    outline: 0;\n"
"}\n"
"\n"
"/* Hover efekti */\n"
"QCalendarWidget QAbstractItemView:item:hover {\n"
"    background-color: #243a70;\n"
"}\n"
"\n"
"/* Bug\u00fcn vurgusu */\n"
"QCalendarWidget QAbstractItemView:item:selected {\n"
"    background-color: #4f7fff;\n"
"    color: white;\n"
"}\n"
"")
        self.randevu_date.setMinimumDate(QDate(2026, 1, 3))
        self.randevu_date.setCalendarPopup(True)
        self.randevu_time = QTimeEdit(Form)
        self.randevu_time.setObjectName(u"randevu_time")
        self.randevu_time.setGeometry(QRect(390, 110, 151, 41))
        self.randevu_time.setStyleSheet(u"QTimeEdit {\n"
"    background-color: rgba(15, 23, 41, 0.7);\n"
"    border: 1px solid #2a3c63;\n"
"    border-radius: 8px;\n"
"    padding: 6px 10px;\n"
"    color: #d6e0ff;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QTimeEdit:hover {\n"
"    border: 1px solid #3c5aa6;\n"
"}\n"
"\n"
"QTimeEdit:focus {\n"
"    border: 1px solid #5f8cff;\n"
"    background-color: rgba(20, 30, 60, 0.9);\n"
"}\n"
"\n"
"/* Ok butonlar\u0131 alan\u0131 */\n"
"QTimeEdit::up-button,\n"
"QTimeEdit::down-button {\n"
"    background: transparent;\n"
"    border: none;\n"
"    width: 18px;\n"
"}\n"
"\n"
"/* Yukar\u0131 ok */\n"
"QTimeEdit::up-arrow {\n"
"    image: url(:/qt-project.org/styles/commonstyle/images/arrowup.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* A\u015fa\u011f\u0131 ok */\n"
"QTimeEdit::down-arrow {\n"
"    image: url(:/qt-project.org/styles/commonstyle/images/arrowdown.png);\n"
"    width: 10px;\n"
"    height: 10px;\n"
"}\n"
"\n"
"/* Se\u00e7ili alan */\n"
"QTimeEdit::section {\n"
"    color: #e5ebf"
                        "f;\n"
"}\n"
"")
        self.randevu_kayit = QPushButton(Form)
        self.randevu_kayit.setObjectName(u"randevu_kayit")
        self.randevu_kayit.setGeometry(QRect(550, 230, 191, 51))
        self.randevu_kayit.setStyleSheet(u"QPushButton {\n"
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
        self.hastane_combo = QComboBox(Form)
        self.hastane_combo.setObjectName(u"hastane_combo")
        self.hastane_combo.setGeometry(QRect(250, 210, 221, 41))
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
        self.poliklinik_combo.setGeometry(QRect(250, 290, 251, 41))
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
        self.doktor_combo = QComboBox(Form)
        self.doktor_combo.setObjectName(u"doktor_combo")
        self.doktor_combo.setGeometry(QRect(250, 380, 271, 51))
        self.doktor_combo.setStyleSheet(u"/* =========================\n"
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
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 201, 51))
        self.label_2.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 150, 201, 51))
        self.label_3.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 330, 191, 51))
        self.label_4.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 240, 181, 51))
        self.label_5.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(250, 170, 131, 31))
        self.label_6.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(250, 60, 361, 51))
        self.label_7.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(250, 260, 131, 31))
        self.label_8.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, 340, 131, 31))
        self.label_9.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 15px;\n"
"}\n"
"")
        self.label_10 = QLabel(Form)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(390, 140, 251, 41))
        self.label_10.setStyleSheet(u"QLabel {\n"
"    color: #a8b7ff;\n"
"    font-size: 13px;\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Hasta bilgilerini giriniz.", None))
        self.cinsiyet_combo.setItemText(0, "")
        self.cinsiyet_combo.setItemText(1, QCoreApplication.translate("Form", u"Erkek", None))
        self.cinsiyet_combo.setItemText(2, QCoreApplication.translate("Form", u"K\u0131z", None))

        self.randevu_kayit.setText(QCoreApplication.translate("Form", u"Randevu al", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Ad\u0131n\u0131z ve soyad\u0131n\u0131z\u0131 giriniz:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"TC Kimlik numaran\u0131z\u0131 giriniz:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Cinsiyetinizi se\u00e7iniz:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Do\u011fum Tarihinizi giriniz:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Hastane se\u00e7iminiz:", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Randevu almak istedi\u011finiz tarihi ve saati giriniz ", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Poliklinik se\u00e7iminiz:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Doktor se\u00e7iminiz:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Sadece yar\u0131m saatte bir randevu al\u0131nabilir.", None))
    # retranslateUi

