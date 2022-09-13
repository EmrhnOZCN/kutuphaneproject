import sqlite3
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_Form(object):
    def setupUi(self, Form):
        self.baglanti_olustur()
        Form.setObjectName("Form")
        Form.resize(455, 765)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 50, 271, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.kitap_adi = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.kitap_adi.setFont(font)
        self.kitap_adi.setObjectName("kitap_adi")
        self.horizontalLayout.addWidget(self.kitap_adi)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 150, 271, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.yazar_adi = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yazar_adi.setFont(font)
        self.yazar_adi.setObjectName("yazar_adi")
        self.horizontalLayout_2.addWidget(self.yazar_adi)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(90, 260, 271, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.basim_yili = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.basim_yili.setFont(font)
        self.basim_yili.setObjectName("basim_yili")
        self.horizontalLayout_3.addWidget(self.basim_yili)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 370, 271, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.temizle_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.temizle_buton.setFont(font)
        self.temizle_buton.setObjectName("temizle_buton")
        self.verticalLayout_2.addWidget(self.temizle_buton)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.kaydet_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.kaydet_buton.setFont(font)
        self.kaydet_buton.setObjectName("kaydet_buton")
        self.horizontalLayout_4.addWidget(self.kaydet_buton)
        self.sil_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.sil_buton.setFont(font)
        self.sil_buton.setObjectName("sil_buton")
        self.horizontalLayout_4.addWidget(self.sil_buton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.ara_buton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.ara_buton.setFont(font)
        self.ara_buton.setObjectName("ara_buton")
        self.verticalLayout_2.addWidget(self.ara_buton)
        self.sonuc_ = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.sonuc_.setFont(font)
        self.sonuc_.setGeometry(QtCore.QRect(101, 630, 391, 101))
        self.sonuc_.setText("             ")
        self.sonuc_.setObjectName("sonuc_")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



        self.kaydet_buton.clicked.connect(self.kayit_veri)
        self.temizle_buton.clicked.connect(self.temiz_hepsi)
        self.sil_buton.clicked.connect(lambda : self.kayit_veri_sil(self.kitap_adi.text(),self.yazar_adi.text(),self.basim_yili.text()))
        self.ara_buton.clicked.connect(self.ara_veri)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kitaplık                 EMİRHAN ÖZCAN"))
        self.label.setText(_translate("Form", "KİTAP ADI :"))
        self.label_2.setText(_translate("Form", "YAZAR ADI :"))
        self.label_3.setText(_translate("Form", "BASIM YILI :"))
        self.temizle_buton.setText(_translate("Form", "TEMZİLE"))
        self.kaydet_buton.setText(_translate("Form", "KAYDET"))
        self.sil_buton.setText(_translate("Form", "SİL"))
        self.ara_buton.setText(_translate("Form", "ARA"))

    def baglanti_olustur(self):

        
        self.baglanti = sqlite3.connect("database_.db")

        self.cursor = self.baglanti.cursor()

        self.cursor.execute("Create Table If not exists kütüphane (kitap_adı TEXT,yazar_adı TEXT,basım_yılı TEXT)")
        
    def kayit_veri(self):
        self.cursor.execute("INSERT INTO kütüphane Values(?,?,?)",(self.kitap_adi.text(),self.yazar_adi.text(),self.basim_yili.text()))
        self.baglanti.commit()

    def temiz_hepsi(self):
        self.kitap_adi.clear()
        self.yazar_adi.clear()
        self.basim_yili.clear()

    def kayit_veri_sil(self,kitap_adi_,yazar_adi_,basim_yili_):
        
        if(kitap_adi_==self.kitap_adi.text()):
             self.cursor.execute("Delete  From kütüphane where kitap_adı= ?",(kitap_adi_,))
             
            
             self.baglanti.commit()
    def ara_veri(self):
        kitapad = self.kitap_adi.text()
        yazarad = self.yazar_adi.text()
        basımyıl=self.basim_yili.text()
        self.cursor.execute("Select * From kütüphane where kitap_adı = ? and yazar_adı = ? and basım_yılı=?",(kitapad,yazarad,basımyıl))

        data = self.cursor.fetchall()

        for i in data:
            print(i)

        if len(data) == 0:
            self.sonuc_.setText("Böyle Bir Kitap Bulunmamaktadır!")
            self.sonuc_.setGeometry(QtCore.QRect(80, 630, 391, 101))
           
            
        else:
            self.sonuc_.setText("KİTAP BULUNMAKTADIR")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('kütüphanepng.png'))
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
