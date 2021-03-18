# coding=utf-8
import os
import sys
import traceback
from PyQt5.QtCore import pyqtSignal,QModelIndex
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QMessageBox
import Panels.Gui as Gui
from Core import *
# 重载QMainWindow类
class MyMainWindow(QMainWindow):
    # 信号(请求槽)
    setMenuEnabled=pyqtSignal(bool)          # 显示/隐藏文件菜单
    setCurrent=pyqtSignal(QModelIndex)      # 切换当前选择的内容
    updateList=pyqtSignal(list)             # 请求更新文件菜单
    updateView=pyqtSignal(object,list,list) # 请求刷新OpenGL显示界面
    getSelected=pyqtSignal()                # 获取当前选择的内容
    # 初始化,销毁函数
    def __init__(self):
        super(MyMainWindow,self).__init__()
        # 状态变量
        self.MenuChecked=False
        self.StatusChecked=True
        self.ModelDictionary={}
        self.CurrentModelName=None
        self.SelectedModelList=[]
        # 模型状态变量
        self.IsRotating=False
        self.IsMoving=False
        self.Location=[0,0,0]
        self.Rotation=[0,0,0]               # 使用xyz欧拉
    def closeEvent(self,Event):
        super(MyMainWindow,self).closeEvent(Event)
        # destroy()
        sys.exit(0)
    # 特殊函数
    def updateDisplay(self):
        # 更新程序界面
        if self.MenuChecked:
            ModelList=self.ModelDictionary.keys()
            self.updateList.emit(ModelList)
            self.setCurrent.emit(list(ModelList).index(self.CurrentModelName))
        if self.CurrentModelName is not None:
            self.updateView.emit(self.ModelDictionary[self.CurrentModelName],self.Location,self.Rotation)
    # 处理函数
    def action_open(self):
        global SuffixList
        # 选择本地3D模型文件
        FileDialog=QFileDialog(self,"打开3D模型文件")
        FileDialog.setAcceptMode(QFileDialog.AcceptOpen)
        FileDialog.setViewMode(QFileDialog.Detail)
        FileDialog.setFileMode(QFileDialog.ExistingFiles)
        FileDialog.setNameFilters(SuffixList)
        if FileDialog.exec()==QFileDialog.Accepted:
            FilepathList=FileDialog.selectedFiles()
        else: return
        # 读取模型文件内容
        for Filepath in FilepathList:
            try:
                Importer=eval("{}.Importer()".format(LoaderDictionary[os.path.splitext(Filepath)[1]]))
                self.ModelDictionary[Filepath]=Importer.execute(Filepath)
                self.updateDisplay()
            except:
                traceback.print_exc()
                self.close()
    def action_export(self):
        global SuffixList
        # 获取当前选择的内容
        self.getSelected.emit()
        length=len(self.SelectedModelList)
        if length==0:
            pass
        # 选择本地路径
        if length==1:
            # 对于单文件
            FileDialog=QFileDialog(self,"导出3D模型文件")
            FileDialog.setAcceptMode(QFileDialog.AcceptSave)
            FileDialog.setViewMode(QFileDialog.Detail)
            FileDialog.setFileMode(QFileDialog.AnyFile)
            FileDialog.setNameFilters(SuffixList)
            FileDialog.setLabelText(FileDialog.Accept,"导出(&E)")
            if FileDialog.exec()==QFileDialog.Accepted:
                FilepathList=FileDialog.selectedFiles()
            else: return
        else:
            # 对于多个文件
            FileDialog=QFileDialog(self,"导出3D模型文件")
            FileDialog.setAcceptMode(QFileDialog.AcceptOpen)
            FileDialog.setViewMode(QFileDialog.Detail)
            FileDialog.setFileMode(QFileDialog.DirectoryOnly)
            FileDialog.setLabelText(FileDialog.Accept,"导出(&E)")
            if FileDialog.exec()==QFileDialog.Accepted:
                FilepathList=FileDialog.selectedFiles()
            else: return
    def action_export_all(self):
        pass
    def action_save_image(self):
        pass
    def action_close(self):
        pass
    def action_close_all(self):
        pass
    def action_exit(self):
        pass
    def action_menu(self):
        pass
    def action_status(self):
        pass
    def action_help(self):
        pass
    def action_about(self):
        pass
    # 槽(接收信号)
    def triggered(self,Action):
        # 直接执行对应的函数代码
        try:
            eval("self.{}()".format(Action.objectName()))
        except:
            traceback.print_exc()
            self.close()
    def selectModel(self,ModelItem):
        pass
# 主函数
def main():
    # create()
    App=QApplication(sys.argv)
    MainWindow=MyMainWindow()
    Ui=Gui.MyUi_MainWindow()
    Ui.setupUi(MainWindow)
    MainWindow.show()
    Result=App.exec_()
    # destroy()
    sys.exit(Result)
