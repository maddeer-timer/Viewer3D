# coding=utf-8
import os
import sys
import traceback
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
import Panels.Gui as Gui
import Core
# 创建函数
def create():
    # 重要标志和变量
    global MenuChecked,StatusChecked
    MenuChecked=False
    StatusChecked=True
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
        super(MyMainWindow,self).closeEvent(event)
        destroy()
        sys.exit(0)
    # 处理函数
    def action_open(self,action):
        pass
    def action_recent(self, action):
        pass
    def action_export(self,action):
        pass
    def action_export_all(self,action):
        pass
    def action_save_image(self,action):
        pass
    def action_close(self,action):
        pass
    def action_close_all(self,action):
        pass
    def action_exit(self,action):
        pass
    def action_menu(self,action):
        pass
    def action_status(self,action):
        pass
    def action_help(self,action):
        pass
    def action_about(self,action):
        pass
    # 输出槽(信号)
    def triggered(self,action):
        # 直接执行对应的函数代码
        try:
            eval("self.{}(action)".format(action.objectName()))
        except:
            traceback.print_exc()
            self.close()
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
