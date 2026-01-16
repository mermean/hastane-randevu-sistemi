# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminpaneli.ui'
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(439, 250)
        self.kullaniciadi_line = QLineEdit(Form)
        self.kullaniciadi_line.setObjectName(u"kullaniciadi_line")
        self.kullaniciadi_line.setGeometry(QRect(50, 30, 341, 41))
        self.kullaniciadi_line.setStyleSheet(u"QLineEdit{\n"
"    background: rgba(255,255,255,20);\n"
"    color: white;\n"
"    padding: 8px 12px;\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(255,255,255,60);\n"
"\n"
"    selection-background-color: rgba(80,140,255,180);\n"
"\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Placeholder rengi */\n"
"QLineEdit::placeholder{\n"
"    color: rgba(255,255,255,120);\n"
"}\n"
"\n"
"/* \u00dczerine t\u0131klan\u0131nca */\n"
"QLineEdit:focus{\n"
"    background: rgba(255,255,255,35);\n"
"    border: 1px solid rgb(120,170,255);\n"
"}\n"
"\n"
"/* Disabled g\u00f6r\u00fcn\u00fcm\u00fc (gerekirse) */\n"
"QLineEdit:disabled{\n"
"    color: rgba(255,255,255,80);\n"
"}\n"
"")
        self.sifre_line = QLineEdit(Form)
        self.sifre_line.setObjectName(u"sifre_line")
        self.sifre_line.setGeometry(QRect(50, 90, 341, 41))
        self.sifre_line.setStyleSheet(u"QLineEdit{\n"
"    background: rgba(255,255,255,20);\n"
"    color: white;\n"
"    padding: 8px 12px;\n"
"    border-radius: 12px;\n"
"    border: 1px solid rgba(255,255,255,60);\n"
"\n"
"    selection-background-color: rgba(80,140,255,180);\n"
"\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"/* Placeholder rengi */\n"
"QLineEdit::placeholder{\n"
"    color: rgba(255,255,255,120);\n"
"}\n"
"\n"
"/* \u00dczerine t\u0131klan\u0131nca */\n"
"QLineEdit:focus{\n"
"    background: rgba(255,255,255,35);\n"
"    border: 1px solid rgb(120,170,255);\n"
"}\n"
"\n"
"/* Disabled g\u00f6r\u00fcn\u00fcm\u00fc (gerekirse) */\n"
"QLineEdit:disabled{\n"
"    color: rgba(255,255,255,80);\n"
"}\n"
"")
        self.sifre_line.setEchoMode(QLineEdit.EchoMode.Password)
        self.giris_button = QPushButton(Form)
        self.giris_button.setObjectName(u"giris_button")
        self.giris_button.setGeometry(QRect(120, 170, 191, 41))
        self.giris_button.setStyleSheet(u"QPushButton{\n"
"    background-color: #3F5BD8;        /* soft mavi */\n"
"    color: white;\n"
"    border-radius: 12px;\n"
"    padding: 10px 22px;\n"
"    font-size: 14px;\n"
"    border: 1px solid rgba(255,255,255,0.08);\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #4E6CFF;        /* hover = biraz parlak */\n"
"    border: 1px solid rgba(255,255,255,0.18);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #344AC0;        /* bas\u0131l\u0131 = biraz koyu */\n"
"    border: 1px solid rgba(255,255,255,0.25);\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"    background-color: #2E3A6C;\n"
"    color: #9AA4CC;\n"
"    border: 1px solid rgba(255,255,255,0.05);\n"
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.giris_button.setText(QCoreApplication.translate("Form", u"Giri\u015f Yap", None))
    # retranslateUi

