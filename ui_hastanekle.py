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
        self.label.setGeometry(QRect(160, 20, 101, 41))
        self.HastaneEkle_button = QPushButton(Form)
        self.HastaneEkle_button.setObjectName(u"HastaneEkle_button")
        self.HastaneEkle_button.setGeometry(QRect(170, 300, 80, 24))
        self.HastaneAdi_line = QLineEdit(Form)
        self.HastaneAdi_line.setObjectName(u"HastaneAdi_line")
        self.HastaneAdi_line.setGeometry(QRect(110, 180, 161, 24))
        self.sehir_line = QLineEdit(Form)
        self.sehir_line.setObjectName(u"sehir_line")
        self.sehir_line.setGeometry(QRect(70, 120, 161, 24))
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
        self.hastane_table.setGeometry(QRect(460, 150, 311, 192))
        self.HastaneGuncelle_button = QPushButton(Form)
        self.HastaneGuncelle_button.setObjectName(u"HastaneGuncelle_button")
        self.HastaneGuncelle_button.setGeometry(QRect(300, 380, 80, 24))
        self.HastaneSil_button = QPushButton(Form)
        self.HastaneSil_button.setObjectName(u"HastaneSil_button")
        self.HastaneSil_button.setGeometry(QRect(500, 400, 80, 24))

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
    # retranslateUi

