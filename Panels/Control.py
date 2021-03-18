# coding=utf-8
import os
import sys
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
import Panels.Gui as Gui
import Core
# 创建函数
def create():
    # 重要标志和变量
    pass
# 销毁函数
def destroy():
    pass
# 重载QMainWindow类
class MyMainWindow(QMainWindow):
    # 初始化,销毁及特殊函数
    def __init__(self):
        super(MyMainWindow,self).__init__()
        pass
    def closeEvent(self,event):
        destroy()
        sys.exit(0)
    # 输出槽(信号)
    pass
# 主函数
def main():
    create()
    app=QApplication(sys.argv)
    MainWindow=MyMainWindow()
    ui=Gui.MyUi_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    result=app.exec_()
    destroy()
    sys.exit(result)
