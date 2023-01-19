from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
from threading import Thread
import pandas as pd
from time import sleep
import logging
debug = 1
try:
    with open("programlog.log","r") as f:
        pass
except IOError:
    with open("programlog.log","w") as f:
        pass
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
    filename="programlog.log"
)
logger = logging.getLogger(__name__)
logging.info("program %s: starting", "Dsi-kayit")

data_path = "uye_kayitlari.xlsx"

class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.uyelik = 0
        self.uyeliky = 0
    def setupUi(self, MainWindow):
        self.today = date.today()
        self.gun = [int(x) for x in self.today.strftime("%d/%m/%Y").split("/")]
    

        self.bitis_gun = [int(x) for x in self.today.strftime("%d/%m/%Y").split("/")]
        MainWindow.setObjectName("Main Window")
        MainWindow.resize(613, 270)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 80, 113, 25))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(330, 50, 110, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(self.gun[2], self.gun[1], self.gun[0]), QtCore.QTime(1, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(320, 10, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(470, 10, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 40, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(470, 90, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(470, 120, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(360, 90, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(360, 120, 92, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 190, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 130, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 120, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 210, 220, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 22))
        self.menubar.setObjectName("menubar")
        self.menu_ye_Kay_t = QtWidgets.QMenu(self.menubar)
        self.menu_ye_Kay_t.setObjectName("menu_ye_Kay_t")
        self.menu_yelik_Uzatma = QtWidgets.QMenu(self.menubar)
        self.menu_yelik_Uzatma.setObjectName("menu_yelik_Uzatma")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu_ye_Kay_t.menuAction())
        self.menubar.addAction(self.menu_yelik_Uzatma.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        ###########################
        self.checkBox.stateChanged.connect(self.aylik1)
        self.checkBox_2.stateChanged.connect(self.aylik3)
        self.checkBox_3.stateChanged.connect(self.aylik6)
        self.checkBox_4.stateChanged.connect(self.yillik)
        self.pushButton.clicked.connect(self.kayit)
     #######################
    def date(self,ay=0,yil=0):
        return str(self.gun[0])+"/"+str(self.gun[1]+ay)+"/"+str(self.gun[2]+yil)
    def aylik1(self,x):
        if x:
            self.uyelik = 1
            self.label_8.setText(self.date(1))
        else:
            self.label_8.setText(self.date())
    def aylik3(self,x):
        if x:
            self.uyelik = 3
            self.label_8.setText(self.date(3))
        else:
            self.label_8.setText(self.date())
    def aylik6(self,x):
        if x:
            self.uyelik = 6
            self.label_8.setText(self.date(6))
        else:
            self.label_8.setText(self.date())
    def yillik(self,x):
        if x:
            self.uyeliky = 1
            self.label_8.setText(self.date(0,1))
        else:
            self.label_8.setText(self.date())
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dsi Üye Kayıt"))
        self.label.setText(_translate("MainWindow", "Üye İsim"))
        self.label_2.setText(_translate("MainWindow", "Üye Soyisim"))
        self.label_3.setText(_translate("MainWindow", "Üyelik Başlangıç"))
        self.label_4.setText(_translate("MainWindow", "Üyelik Bitiş"))
        self.checkBox.setText(_translate("MainWindow", "1 Aylık"))
        self.checkBox_2.setText(_translate("MainWindow", "3 Aylık"))
        self.pushButton.setText(_translate("MainWindow", "Kaydet"))
        self.label_5.setText(_translate("MainWindow", "        Tel No"))
        self.checkBox_3.setText(_translate("MainWindow", "6 Aylık"))
        self.checkBox_4.setText(_translate("MainWindow", "Yıllık"))
        self.label_7.setText(_translate("MainWindow",""))
        self.label_8.setText(_translate("Main Window", self.date()))
    def kayit(self):
        uyedf = pd.read_excel(data_path, index_col=None)
        _translate = QtCore.QCoreApplication.translate
        #yeni_df["Üyelik Başlangıç Tarihi"] = 
        #yeni_df["Üyelik Bitiş Tarihi"] = 
        #yeni_df["Telefon Numarası"] = 
        ad1 = self.lineEdit.text()
        ad2 = self.lineEdit_2.text()
        baslangic = str(self.gun[0])+"-"+str(self.gun[1])+"-"+str(self.gun[2])
        bitis = str(self.bitis_gun[0])+"-"+str(self.bitis_gun[1]+self.uyelik)+"-"+str(self.bitis_gun[2]+self.uyeliky)
        telno = str(self.lineEdit_3.text())
        if not debug:
            if ad1 == "" or ad2 == "":
                self.label_7.setText(_translate("MainWindow","Üye İsim Soyismini kontrol edin"))
            elif baslangic == bitis:
                self.label_7.setText(_translate("MainWindow","Üyelik Bitiş Tarihi Hatalı"))
            elif telno == "":
                self.label_7.setText(_translate("MainWindow","Lütfen Telefon Numarası Giriniz"))
            else:
                df_dict = {"İsim Soyisim" : ad1 + ad2,
                        "Üyelik Başlangıç Tarihi": baslangic,
                        "Üyelik Bitiş Tarihi" :bitis,
                        "Telefon Numarası": telno
                        }
                yeni_df = pd.DataFrame(df_dict,index=[0])
                son_df =pd.concat([uyedf,yeni_df], ignore_index=True)
                son_df.to_excel(data_path,index=False)
                self.label_7.setText(_translate("MainWindow","Üye Başarıyla Kaydedildi"))
                sleep(1)
                self.label_7.setText(_translate("MainWindow",""))
                self.clear_edit()
                print(son_df)
        else:
            df_dict = {"İsim Soyisim" : ad1 + ad2,
                        "Üyelik Başlangıç Tarihi": baslangic,
                        "Üyelik Bitiş Tarihi" :bitis,
                        "Telefon Numarası": telno
                        }
            yeni_df = pd.DataFrame(df_dict,index=[0])
            son_df =pd.concat([uyedf,yeni_df], ignore_index=True)
            son_df.to_excel(data_path,index=False)
            self.label_7.setText(_translate("MainWindow","Üye Başarıyla Kaydedildi"))
            sleep(1)
            self.label_7.setText(_translate("MainWindow",""))
            self.clear_edit()
            print(son_df)
    def clear_edit(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.checkBox.setCheckState(0)
        self.checkBox_2.setCheckState(0)
        self.checkBox_3.setCheckState(0)
        self.checkBox_4.setCheckState(0)
        self.uyelik,self.uyeliky = 0,0 


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

