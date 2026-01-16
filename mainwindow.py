import sys
import math
import random
import pyodbc

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem
)
from PySide6.QtCore import Qt, QTimer, QPointF, QDate, QTime
from PySide6.QtGui import QPainter, QColor, QLinearGradient

from ui_form import Ui_MainWindow as UiAnaEkran
from ui_adminpaneli import Ui_Form as UiAdminLogin
from ui_admingiris import Ui_Form as UiAdminPanel
from ui_poliklinik_ekle import Ui_Form as UiPoliklinik
from ui_hastane_ekle import Ui_Form as UiHastane
from ui_doktorekle import Ui_Form as UiDoktor
from ui_randevual import Ui_Form as UiRandevuEkran
from ui_randevular import Ui_Form as UiRandevular


class StarBackgroundMixin:
    def setup_star_background(self):
        self.angle = 0
        self.stars = []

        for i in range(120):
            x = random.randint(-400, 400)
            y = random.randint(-400, 400)
            size = random.choice([1, 1, 2, 2, 3])
            alpha = random.randint(180, 255)
            speed = random.uniform(0.002, 0.006)
            self.stars.append([x, y, size, alpha, speed, random.random()])

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(40)

    def update_animation(self):
        self.angle += 0.002
        for s in self.stars:
            s[5] += s[4]
            s[3] = 200 + int(math.sin(s[5]) * 40)
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self)
        grad = QLinearGradient(0, 0, 0, self.height())
        grad.setColorAt(0, QColor(6, 15, 50))
        grad.setColorAt(1, QColor(1, 5, 20))
        painter.fillRect(self.rect(), grad)

        cx = self.width() / 2
        cy = self.height() / 2

        for x, y, size, alpha, _, _ in self.stars:
            rx = x * math.cos(self.angle) - y * math.sin(self.angle)
            ry = x * math.sin(self.angle) + y * math.cos(self.angle)

            painter.setBrush(QColor(255, 255, 255, alpha))
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(QPointF(cx + rx, cy + ry), size, size)


class HastaneWindow(StarBackgroundMixin, QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = UiHastane()
        self.ui.setupUi(self)
        self.setup_star_background()

        self.init_db()
        self.secili_id = None

        self.ui.HastaneEkle_button.clicked.connect(self.ekle)
        self.ui.HastaneGuncelle_button.clicked.connect(self.guncelle)
        self.ui.HastaneSil_button.clicked.connect(self.sil)
        self.ui.hastane_table.cellClicked.connect(self.satir_sec)

        self.listele()

    def init_db(self):
        try:
            conn_master = pyodbc.connect(
                "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;Trusted_Connection=yes;",
                autocommit=True
            )
            c = conn_master.cursor()
            c.execute("IF DB_ID('HastaneDB') IS NULL CREATE DATABASE HastaneDB")
            c.close()
            conn_master.close()
        except:
            pass

        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=HastaneDB;Trusted_Connection=yes;",
            autocommit=True
        )

        c = self.conn.cursor()
        c.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Hastaneler')
        BEGIN
            CREATE TABLE Hastaneler(
                Id INT IDENTITY PRIMARY KEY,
                HastaneAdi NVARCHAR(200),
                Sehir NVARCHAR(100)
            )
        END
        """)
        c.close()

    def listele(self):
        c = self.conn.cursor()
        c.execute("SELECT Id,HastaneAdi,Sehir FROM Hastaneler")
        rows = c.fetchall()
        c.close()

        self.ui.hastane_table.setRowCount(len(rows))
        self.ui.hastane_table.setColumnCount(3)
        self.ui.hastane_table.setHorizontalHeaderLabels(["ID","Hastane","Şehir"])

        for i,row in enumerate(rows):
            for j,val in enumerate(row):
                self.ui.hastane_table.setItem(i,j,QTableWidgetItem(str(val)))

    def ekle(self):
        adi = self.ui.HastaneAdi_line.text().strip()
        sehir = self.ui.sehir_line.text().strip()

        if not adi or not sehir:
            QMessageBox.warning(self,"Uyarı","Boş bırakılamaz")
            return

        c = self.conn.cursor()
        c.execute("INSERT INTO Hastaneler VALUES (?,?)", adi, sehir)
        c.close()
        self.listele()

    def satir_sec(self,row,col):
        self.secili_id = self.ui.hastane_table.item(row,0).text()
        self.ui.HastaneAdi_line.setText(self.ui.hastane_table.item(row,1).text())
        self.ui.sehir_line.setText(self.ui.hastane_table.item(row,2).text())

    def guncelle(self):
        if not self.secili_id:
            return

        c = self.conn.cursor()
        c.execute("""
        UPDATE Hastaneler SET HastaneAdi=?, Sehir=? WHERE Id=?
        """, self.ui.HastaneAdi_line.text(), self.ui.sehir_line.text(), self.secili_id)
        c.close()
        self.listele()

    def sil(self):
        if not self.secili_id:
            QMessageBox.warning(self,"Uyarı","Silinecek kayıt seçilmedi.")
            return

        reply = QMessageBox.question(
            self, "Onay",
            "Bu hastaneye bağlı veriler de silinebilir. Devam edilsin mi?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        try:
            c = self.conn.cursor()
            c.execute("DELETE FROM Hastaneler WHERE Id=?", self.secili_id)
            c.close()
            self.listele()
        except Exception as e:
            QMessageBox.critical(self,"Hata",str(e))


class PoliklinikWindow(StarBackgroundMixin, QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = UiPoliklinik()
        self.ui.setupUi(self)
        self.setup_star_background()

        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=HastaneDB;Trusted_Connection=yes;",
            autocommit=True
        )

        c=self.conn.cursor()
        c.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Poliklinikler')
        BEGIN
            CREATE TABLE Poliklinikler(
                Id INT IDENTITY PRIMARY KEY,
                PoliklinikAdi NVARCHAR(200),
                HastaneId INT
            )
        END
        """)
        c.close()

        self.secili_id=None
        self.map={}

        self.hastaneleri_yukle()

        self.ui.kaydet_klinik.clicked.connect(self.ekle)
        self.ui.klinik_guncelle.clicked.connect(self.guncelle)
        self.ui.klinik_sil.clicked.connect(self.sil)
        self.ui.poliklinik_table.cellClicked.connect(self.satir_sec)

        self.listele()

    def hastaneleri_yukle(self):
        self.ui.hastaneler_combo.clear()
        self.map = {}
        self.ui.hastaneler_combo.clear()
        c=self.conn.cursor()
        c.execute("SELECT Id,HastaneAdi FROM Hastaneler")
        for Id,Ad in c.fetchall():
            self.map[Ad]=Id
            self.ui.hastaneler_combo.addItem(Ad)
        c.close()

    def listele(self):
        c=self.conn.cursor()
        c.execute("""
        SELECT p.Id,p.PoliklinikAdi,h.HastaneAdi
        FROM Poliklinikler p
        JOIN Hastaneler h ON p.HastaneId=h.Id
        """)
        rows=c.fetchall()
        c.close()

        self.ui.poliklinik_table.setRowCount(len(rows))
        self.ui.poliklinik_table.setColumnCount(3)
        self.ui.poliklinik_table.setHorizontalHeaderLabels(["ID","Poliklinik","Hastane"])

        for i,row in enumerate(rows):
            for j,val in enumerate(row):
                self.ui.poliklinik_table.setItem(i,j,QTableWidgetItem(str(val)))

    def ekle(self):
        ad=self.ui.klinik_line.text().strip()
        if not ad or not self.ui.hastaneler_combo.currentText():
            return
        hid=self.map[self.ui.hastaneler_combo.currentText()]
        c=self.conn.cursor()
        c.execute("INSERT INTO Poliklinikler VALUES (?,?)",ad,hid)
        c.close()
        self.listele()

    def satir_sec(self,row,col):
        self.secili_id=self.ui.poliklinik_table.item(row,0).text()
        self.ui.klinik_line.setText(self.ui.poliklinik_table.item(row,1).text())

    def guncelle(self):
        if not self.secili_id:return
        ad=self.ui.klinik_line.text()
        hid=self.map[self.ui.hastaneler_combo.currentText()]
        c=self.conn.cursor()
        c.execute("""
        UPDATE Poliklinikler SET PoliklinikAdi=?,HastaneId=? WHERE Id=?
        """,ad,hid,self.secili_id)
        c.close()
        self.listele()

    def sil(self):
        if not self.secili_id:
            return

        reply = QMessageBox.question(
            self,
            "Onay",
            "Bu polikliniğe bağlı doktorlar ve randevular da silinecek.\n\nDevam edilsin mi?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        c = self.conn.cursor()

        # 🔥 1. Bu polikliniğe bağlı doktorların randevularını sil
        c.execute("""
            DELETE FROM Randevular
            WHERE DoktorId IN (
                SELECT Id FROM Doktorlar WHERE PoliklinikId=?
            )
        """, self.secili_id)

        # 🔥 2. Bu polikliniğe bağlı doktorları sil
        c.execute("DELETE FROM Doktorlar WHERE PoliklinikId=?", self.secili_id)

        # 🔥 3. Polikliniği sil
        c.execute("DELETE FROM Poliklinikler WHERE Id=?", self.secili_id)

        c.close()

        QMessageBox.information(
            self,
            "Bilgi",
            "Poliklinik, bağlı doktorlar ve randevular silindi."
        )

        self.secili_id = None
        self.listele()



class DoktorWindow(StarBackgroundMixin, QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = UiDoktor()
        self.ui.setupUi(self)
        self.setup_star_background()

        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=HastaneDB;Trusted_Connection=yes;",
            autocommit=True
        )

        c=self.conn.cursor()
        c.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Doktorlar')
        BEGIN
            CREATE TABLE Doktorlar(
                Id INT IDENTITY PRIMARY KEY,
                DoktorAdi NVARCHAR(200),
                PoliklinikId INT
            )
        END
        """)
        c.close()

        self.hmap={}
        self.pmap={}
        self.secili_id=None

        self.hastaneleri_yukle()

        self.ui.hastane_combo.currentTextChanged.connect(self.poliklinikleri_yukle)
        self.ui.doktor_ekle.clicked.connect(self.ekle)
        self.ui.doktor_guncelle.clicked.connect(self.guncelle)
        self.ui.doktor_sil.clicked.connect(self.sil)
        self.ui.doktor_table.cellClicked.connect(self.satir_sec)
        self.listele()

    def hastaneleri_yukle(self):
        self.ui.hastane_combo.clear()
        c=self.conn.cursor()
        c.execute("SELECT Id,HastaneAdi FROM Hastaneler")
        for Id,Ad in c.fetchall():
            self.hmap[Ad]=Id
            self.ui.hastane_combo.addItem(Ad)
        c.close()
        self.poliklinikleri_yukle()

    def poliklinikleri_yukle(self):
        self.pmap={}
        self.ui.poliklinik_combo.clear()
        if not self.ui.hastane_combo.currentText(): return
        hid=self.hmap[self.ui.hastane_combo.currentText()]
        c=self.conn.cursor()
        c.execute("SELECT Id,PoliklinikAdi FROM Poliklinikler WHERE HastaneId=?",hid)
        for Id,Ad in c.fetchall():
            self.pmap[Ad]=Id
            self.ui.poliklinik_combo.addItem(Ad)
        c.close()

    def listele(self):
        c=self.conn.cursor()
        c.execute("""
        SELECT d.Id,d.DoktorAdi,p.PoliklinikAdi,h.HastaneAdi
        FROM Doktorlar d
        JOIN Poliklinikler p ON d.PoliklinikId=p.Id
        JOIN Hastaneler h ON p.HastaneId=h.Id
        """)
        rows=c.fetchall()
        c.close()
        self.ui.doktor_table.setRowCount(len(rows))
        self.ui.doktor_table.setColumnCount(4)
        self.ui.doktor_table.setHorizontalHeaderLabels(["ID","Doktor","Poliklinik","Hastane"])
        for i,row in enumerate(rows):
            for j,val in enumerate(row):
                self.ui.doktor_table.setItem(i,j,QTableWidgetItem(str(val)))

    def ekle(self):
        ad=self.ui.doktoradi_line.text()
        if not ad or not self.ui.poliklinik_combo.currentText(): return
        pid=self.pmap[self.ui.poliklinik_combo.currentText()]
        c=self.conn.cursor()
        c.execute("INSERT INTO Doktorlar VALUES (?,?)",ad,pid)
        c.close()
        self.listele()

    def satir_sec(self,row,col):
        self.secili_id=self.ui.doktor_table.item(row,0).text()
        self.ui.doktoradi_line.setText(self.ui.doktor_table.item(row,1).text())

    def guncelle(self):
        if not self.secili_id:return
        ad=self.ui.doktoradi_line.text()
        pid=self.pmap[self.ui.poliklinik_combo.currentText()]
        c=self.conn.cursor()
        c.execute("UPDATE Doktorlar SET DoktorAdi=?,PoliklinikId=? WHERE Id=?",ad,pid,self.secili_id)
        c.close()
        self.listele()

    def sil(self):
        if not self.secili_id:
            return

        reply = QMessageBox.question(
            self,
            "Onay",
            "Bu doktora bağlı randevular da silinecek.\n\nDevam edilsin mi?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        c = self.conn.cursor()

        c.execute("DELETE FROM Randevular WHERE DoktorId=?", self.secili_id)

        c.execute("DELETE FROM Doktorlar WHERE Id=?", self.secili_id)

        c.close()

        QMessageBox.information(
            self,
            "Bilgi",
            "Doktor ve bağlı randevular silindi."
        )

        self.secili_id = None
        self.listele()



class RandevuWindow(StarBackgroundMixin, QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = UiRandevuEkran()
        self.ui.setupUi(self)
        self.setup_star_background()

        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=HastaneDB;Trusted_Connection=yes;",
            autocommit=True
        )

        c=self.conn.cursor()
        c.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Randevular')
        BEGIN
            CREATE TABLE Randevular(
                Id INT IDENTITY PRIMARY KEY,
                AdSoyad NVARCHAR(200),
                TC NVARCHAR(11),
                DogumTarihi DATE,
                Cinsiyet NVARCHAR(20),
                HastaneId INT,
                PoliklinikId INT,
                DoktorId INT,
                RandevuTarihi DATE,
                RandevuSaati NVARCHAR(5)
            )
        END
        """)
        c.close()

        self.hmap={}
        c=self.conn.cursor()
        c.execute("SELECT Id,HastaneAdi FROM Hastaneler")
        for Id,Ad in c.fetchall():
            self.hmap[Ad]=Id
            self.ui.hastane_combo.addItem(Ad)
        c.close()

        self.ui.tc_line.textChanged.connect(self.tc_kontrol)
        self.ui.hastane_combo.currentTextChanged.connect(self.poliklinik_yukle)
        self.ui.poliklinik_combo.currentTextChanged.connect(self.doktor_yukle)
        self.ui.randevu_time.setDisplayFormat("HH:mm")
        self.ui.randevu_time.setTime(QTime(9,0))
        self.ui.randevu_time.timeChanged.connect(self.round_time)
        self.ui.randevu_kayit.clicked.connect(self.kaydet)
        self.poliklinik_yukle()

    def tc_kontrol(self):
        t=self.ui.tc_line.text()
        self.ui.tc_line.setText(''.join(ch for ch in t if ch.isdigit()))

    def round_time(self):
        t=self.ui.randevu_time.time()
        h=t.hour()
        m=t.minute()
        if h<9: h=9;m=0
        if h>17 or (h==17 and m>0): h=17;m=0
        m=0 if m<30 else 30
        self.ui.randevu_time.blockSignals(True)
        self.ui.randevu_time.setTime(QTime(h,m))
        self.ui.randevu_time.blockSignals(False)

    def poliklinik_yukle(self):
        self.pmap={}
        self.ui.poliklinik_combo.clear()
        if not self.ui.hastane_combo.currentText(): return
        hid=self.hmap[self.ui.hastane_combo.currentText()]
        c=self.conn.cursor()
        c.execute("SELECT Id,PoliklinikAdi FROM Poliklinikler WHERE HastaneId=?",hid)
        for Id,Ad in c.fetchall():
            self.pmap[Ad]=Id
            self.ui.poliklinik_combo.addItem(Ad)
        c.close()
        self.doktor_yukle()

    def doktor_yukle(self):
        self.dmap={}
        self.ui.doktor_combo.clear()
        if not self.ui.poliklinik_combo.currentText(): return
        pid=self.pmap[self.ui.poliklinik_combo.currentText()]
        c=self.conn.cursor()
        c.execute("SELECT Id,DoktorAdi FROM Doktorlar WHERE PoliklinikId=?",pid)
        for Id,Ad in c.fetchall():
            self.dmap[Ad]=Id
            self.ui.doktor_combo.addItem(Ad)
        c.close()

    def kaydet(self):
        if not self.ui.doktor_combo.currentText():
            return

        doktor_id = self.dmap[self.ui.doktor_combo.currentText()]
        tarih = self.ui.randevu_date.date().toString("yyyy-MM-dd")
        saat = self.ui.randevu_time.time().toString("HH:mm")

        c = self.conn.cursor()

        c.execute("""
            SELECT COUNT(*) FROM Randevular
            WHERE DoktorId = ? AND RandevuTarihi = ? AND RandevuSaati = ?
        """, doktor_id, tarih, saat)

        if c.fetchone()[0] > 0:
            QMessageBox.warning(self, "Randevu Dolu",
                                f"Seçilen saatte ({saat}) bu doktorun randevusu zaten doludur.")
            c.close()
            return

        c.execute("""
        INSERT INTO Randevular VALUES (?,?,?,?,?,?,?,?,?)
        """,
        self.ui.adsoyad_line.text(), self.ui.tc_line.text(), self.ui.dogum_date.date().toString("yyyy-MM-dd"),
        self.ui.cinsiyet_combo.currentText(), self.hmap[self.ui.hastane_combo.currentText()],
        self.pmap[self.ui.poliklinik_combo.currentText()], doktor_id, tarih, saat)
        c.close()
        QMessageBox.information(self,"Başarılı","Randevu oluşturuldu.")


class RandevularWindow(StarBackgroundMixin, QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = UiRandevular()
        self.ui.setupUi(self)
        self.setup_star_background()

        self.conn = pyodbc.connect(
            "DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=HastaneDB;Trusted_Connection=yes;",
            autocommit=True
        )

        self.secili_id = None
        self.ui.randevu_table.setColumnCount(8)
        self.ui.randevu_table.setHorizontalHeaderLabels([
            "ID","Ad Soyad","TC","Doktor","Poliklinik","Hastane","Tarih","Saat"
        ])
        self.ui.randevu_table.cellClicked.connect(self.satir_sec)
        self.ui.guncelle_button.clicked.connect(self.guncelle)
        self.ui.sil_button.clicked.connect(self.sil)
        self.listele()

    def listele(self):
        c = self.conn.cursor()
        c.execute("""
        SELECT r.Id, r.AdSoyad, r.TC, d.DoktorAdi, p.PoliklinikAdi, h.HastaneAdi, r.RandevuTarihi, r.RandevuSaati
        FROM Randevular r
        JOIN Doktorlar d ON r.DoktorId=d.Id
        JOIN Poliklinikler p ON r.PoliklinikId=p.Id
        JOIN Hastaneler h ON r.HastaneId=h.Id
        ORDER BY r.RandevuTarihi,r.RandevuSaati
        """)
        rows = c.fetchall()
        c.close()
        self.ui.randevu_table.setRowCount(len(rows))
        for i,row in enumerate(rows):
            for j,val in enumerate(row):
                self.ui.randevu_table.setItem(i, j, QTableWidgetItem(str(val)))

    def satir_sec(self,row,col):
        self.secili_id = self.ui.randevu_table.item(row,0).text()
        self.ui.adsoyad_line.setText(self.ui.randevu_table.item(row,1).text())
        self.ui.tc_line.setText(self.ui.randevu_table.item(row,2).text())
        tarih_str = self.ui.randevu_table.item(row,6).text()
        saat_str = self.ui.randevu_table.item(row,7).text()
        self.ui.tarih_edit.setDate(QDate.fromString(tarih_str,"yyyy-MM-dd"))
        self.ui.saat_edit.setTime(QTime.fromString(saat_str,"HH:mm"))

    def guncelle(self):
        if not self.secili_id:
            QMessageBox.warning(self,"Uyarı","Randevu seçmedin")
            return
        ad = self.ui.adsoyad_line.text()
        tc = self.ui.tc_line.text()
        tarih = self.ui.tarih_edit.date().toString("yyyy-MM-dd")
        saat = self.ui.saat_edit.time().toString("HH:mm")
        c = self.conn.cursor()
        c.execute("""
        UPDATE Randevular SET AdSoyad=?, TC=?, RandevuTarihi=?, RandevuSaati=? WHERE Id=?
        """, ad, tc, tarih, saat, self.secili_id)
        c.close()
        QMessageBox.information(self,"Başarılı","Randevu güncellendi")
        self.listele()

    def sil(self):
        if not self.secili_id:
            QMessageBox.warning(self,"Uyarı","Randevu seçmedin")
            return
        cevap = QMessageBox.question(self, "Sil", "Bu randevu silinsin mi?", QMessageBox.Yes | QMessageBox.No)
        if cevap == QMessageBox.No: return
        c = self.conn.cursor()
        c.execute("DELETE FROM Randevular WHERE Id=?", self.secili_id)
        c.close()
        self.listele()
        self.secili_id = None


class AdminPanelWindow(StarBackgroundMixin, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiAdminPanel()
        self.ui.setupUi(self)
        self.setup_star_background()
        self.ui.hastane_button.clicked.connect(self.open_hastane)
        self.ui.poliklinik_button.clicked.connect(self.open_poliklinik)
        self.ui.doktor_button.clicked.connect(self.open_doktor)
        self.ui.randevu_button.clicked.connect(self.open_randevu)

    def open_hastane(self):
        self.win = HastaneWindow()
        self.win.show()

    def open_poliklinik(self):
        self.win = PoliklinikWindow()
        self.win.show()

    def open_doktor(self):
        self.win = DoktorWindow()
        self.win.show()

    def open_randevu(self):
        self.win = RandevularWindow()
        self.win.show()


class AdminLoginWindow(StarBackgroundMixin, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiAdminLogin()
        self.ui.setupUi(self)
        self.setup_star_background()
        self.ui.giris_button.clicked.connect(self.login)

    def login(self):
        if self.ui.kullaniciadi_line.text()=="admin" and self.ui.sifre_line.text()=="1234":
            self.panel = AdminPanelWindow()
            self.panel.show()
            self.hide()
        else:
            QMessageBox.warning(self,"Hata","Yanlış giriş")


class MainWindow(StarBackgroundMixin, QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiAnaEkran()
        self.ui.setupUi(self)
        self.setup_star_background()
        self.ui.pushButton.clicked.connect(self.randevu_ac)
        self.ui.pushButton_2.clicked.connect(self.admin_ac)

    def admin_ac(self):
        self.login = AdminLoginWindow()
        self.login.show()

    def randevu_ac(self):
        self.randevu = RandevuWindow()
        self.randevu.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
