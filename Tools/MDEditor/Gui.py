# coding=utf-8
from MainWindow import *
# 重载Ui_MainWindow类
class MyUi_MainWindow(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super(MyUi_MainWindow,self).setupUi(MainWindow)
        MainWindow.retranslateUi.connect(self.retranslateUi)