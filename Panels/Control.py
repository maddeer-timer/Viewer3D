# coding=utf-8
import os
import sys
import traceback
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
import Panels.Gui as Gui
from Core import *
# 创建函数
def create():
    pass
# 销毁函数
def destroy():
    pass
# 重载QMainWindow类
class MyMainWindow(QMainWindow):
    # 信号(发送给槽)
    UpdateView=pyqtSignal(object,list,list) # 请求刷新视图内容
    # 初始化,销毁及特殊函数
    def __init__(self):
        super(MyMainWindow,self).__init__()
        # 状态变量
        self.MenuChecked=False
        self.StatusChecked=True
        self.PathHistory=[sys.path[0]]
        self.ModelDictionary={}
        self.CurrentModelName=None
        # 模型状态变量
        self.IsRotating=False
        self.IsMoving=False
        self.Location=[0,0,0]
        self.Rotation=[0,0,0]               # 使用xyz欧拉
    def closeEvent(self,event):
        super(MyMainWindow,self).closeEvent(event)
        destroy()
        sys.exit(0)
    def updateList(self,ModelList):
        # 更新文件菜单列表
        pass
    def updateDisplay(self):
        # 更新程序界面
        if self.MenuChecked:
            self.updateList(self.ModelDictionary.keys())
        if self.CurrentModelName!=None:
            self.UpdateView.emit(self.ModelDictionary[self.CurrentModelName],self.Location,self.Rotation)
    # 处理函数
    def action_open(self,action):
        global SuffixList
        # 选择本地3D模型文件
        FileDialog=QFileDialog(self,"打开3D模型文件")
        FileDialog.setAcceptMode(QFileDialog.AcceptOpen)
        FileDialog.setViewMode(QFileDialog.Detail)
        FileDialog.setFileMode(QFileDialog.ExistingFiles)
        FileDialog.setHistory(self.PathHistory)
        FileDialog.setNameFilters(SuffixList)
        if FileDialog.exec()==QFileDialog.Accepted:
            FilepathList=FileDialog.selectedFiles()
        else: return
        # 读取模型文件内容
        for filepath in FilepathList:
            try:
                Importer=eval("{}.Importer()".format(LoaderDictionary[os.path.splitext(filepath)[1]]))
                self.ModelDictionary[filepath]=Importer.execute(filepath)
                self.updateDisplay()
            except:
                traceback.print_exc()
                self.close()
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
    # 槽(接收信号)
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
