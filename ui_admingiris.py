# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admingiris.ui'
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(714, 359)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(50, 40, 581, 271))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.hastane_button = QPushButton(self.verticalLayoutWidget)
        self.hastane_button.setObjectName(u"hastane_button")
        self.hastane_button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.hastane_button)

        self.poliklinik_button = QPushButton(self.verticalLayoutWidget)
        self.poliklinik_button.setObjectName(u"poliklinik_button")
        self.poliklinik_button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.poliklinik_button)

        self.doktor_button = QPushButton(self.verticalLayoutWidget)
        self.doktor_button.setObjectName(u"doktor_button")
        self.doktor_button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.doktor_button)

        self.randevu_button = QPushButton(self.verticalLayoutWidget)
        self.randevu_button.setObjectName(u"randevu_button")
        self.randevu_button.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.randevu_button)

        self.cikisyap = QPushButton(self.verticalLayoutWidget)
        self.cikisyap.setObjectName(u"cikisyap")
        self.cikisyap.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.cikisyap)


        self.retranslateUi(Form)
        self.cikisyap.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.hastane_button.setText(QCoreApplication.translate("Form", u"Hastane Ekle", None))
        self.poliklinik_button.setText(QCoreApplication.translate("Form", u"Poliklinik Ekle", None))
        self.doktor_button.setText(QCoreApplication.translate("Form", u"Doktor Ekle", None))
        self.randevu_button.setText(QCoreApplication.translate("Form", u"Randevular", None))
        self.cikisyap.setText(QCoreApplication.translate("Form", u"\u00c7IKI\u015e YAP", None))
    # retranslateUi

