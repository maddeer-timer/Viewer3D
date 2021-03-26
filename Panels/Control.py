# coding=utf-8
import os
import sys
import traceback
from PyQt5 import QtCore,QtGui,QtWidgets
# QtCore:       pyqtSignal,QModelIndex,QCoreApplication,QTranslator
# QtWidgets:    QApplication,QMainWindow,QFileDialog,QMessageBox
import Panels.Gui as Gui
import Panels.Wizard as Wizard
from Core import *
import Core.Model as Model
# 重载QMainWindow类
class MyMainWindow(QtWidgets.QMainWindow):
    # 信号(请求槽)
    setMenuVisible=QtCore.pyqtSignal(bool)                  # 显示/隐藏文件菜单
    setCurrent=QtCore.pyqtSignal(QtCore.QModelIndex)        # 切换当前选择的内容
    updateList=QtCore.pyqtSignal(list)                      # 请求更新文件菜单
    updateView=QtCore.pyqtSignal(object,list,list)          # 请求刷新OpenGL显示界面
    getSelected=QtCore.pyqtSignal()                         # 获取当前选择的内容
    retranslateUi=QtCore.pyqtSignal(QtWidgets.QMainWindow)  # 请求刷新界面
    # 初始化,销毁函数
    def __init__(self,App,Translators):
        super(MyMainWindow,self).__init__()
        # 主变量
        self.App=App
        self.Translators=Translators
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
            self.updateView.emit(self.ModelDictionary[self.CurrentModelName],
                                 self.Location,self.Rotation)
    # 处理函数
    def action_open(self):
        global SuffixList
        # 选择本地3D模型文件
        _translate=QtCore.QCoreApplication.translate
        FileDialog=QtWidgets.QFileDialog(self,_translate("FileDialog","Open 3D model files"))
        FileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        FileDialog.setViewMode(QtWidgets.QFileDialog.Detail)
        FileDialog.setFileMode(QtWidgets.QFileDialog.ExistingFiles)
        FileDialog.setNameFilters(SuffixList)
        if FileDialog.exec()==QtWidgets.QFileDialog.Accepted:
            FilepathList=FileDialog.selectedFiles()
        else: return
        # 读取模型文件内容
        for Filepath in FilepathList:
            try:
                Importer=exec("{}.Importer()".format(
                    LoaderDictionary[os.path.splitext(Filepath)[1]]))
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
            _translate=QtCore.QCoreApplication.translate
            FileDialog=QtWidgets.QFileDialog(self,_translate("FileDialog","Export 3D model files"))
            FileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptSave)
            FileDialog.setViewMode(QtWidgets.QFileDialog.Detail)
            FileDialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
            FileDialog.setNameFilters(SuffixList)
            FileDialog.setLabelText(FileDialog.Accept,_translate("FileDialog","&Export"))
            if FileDialog.exec()==QtWidgets.QFileDialog.Accepted:
                FilepathList=FileDialog.selectedFiles()
            else: return
        else:
            # 对于多个文件
            _translate=QtCore.QCoreApplication.translate
            FileDialog=QtWidgets.QFileDialog(self,_translate("FileDialog","Export 3D model files"))
            FileDialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
            FileDialog.setViewMode(QtWidgets.QFileDialog.Detail)
            FileDialog.setFileMode(QtWidgets.QFileDialog.DirectoryOnly)
            FileDialog.setLabelText(FileDialog.Accept,_translate("FileDialog","&Export"))
            if FileDialog.exec()==QtWidgets.QFileDialog.Accepted:
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
        WizardWindow=Wizard.MyWizard()
        WizardWindow.exec()
    def action_Chinese(self):
        self.App.installTranslator(self.Translators[0])
        self.App.installTranslator(self.Translators[1])
        self.App.removeTranslator(self.Translators[2])
        self.retranslateUi.emit(self)
    def action_English(self):
        self.App.removeTranslator(self.Translators[0])
        self.App.removeTranslator(self.Translators[1])
        self.App.installTranslator(self.Translators[2])
        self.retranslateUi.emit(self)
    def action_about(self):
        _translate=QtCore.QCoreApplication.translate
        QtWidgets.QMessageBox.about(self,_translate("MessageBox","About View3D"),
                                    _translate("MessageBox",r"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <style type="text/css">
        body {
            font-family: "Consolas",monospace;
        }
    </style>
</head>
<body>
<h2><font color=Maroon>About View3D</font></h2>
<ul style="font-size: 15px;">
    <li>This is a software for reading and<br/>
        displaying 3D models, and it can also<br/>
        be used for format conversion.</li>
    <li>It loads and displays the model by<br/>
        using PyQt and PyOpenGL.</li>
    <li>You can use the mouse and the keyboard<br/>
        to move, rotate or scale the model.</li>
</ul>
<h3 style="text-align: right;"><font color=Green>Code by Maddeer(China)</font></h3>
</body>
</html>
"""))
    # 槽(接收信号)
    def triggered(self,Action):
        # 直接执行对应的函数代码
        try:
            exec("self.{}()".format(Action.objectName()))
        except:
            traceback.print_exc()
            self.close()
    def selectModel(self,ModelItem):
        pass
# 主函数
def main():
    # 初始化部分
    App=QtWidgets.QApplication(sys.argv)
    SystemTranslationsPath=QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    # 翻译和安装部分
    Translator=QtCore.QTranslator()
    TranslatorSystem=QtCore.QTranslator()
    TranslatorSystemEn=QtCore.QTranslator()
    if not Translator.load("zh_CN",directory="Translations") or \
            not TranslatorSystem.load("qt_zh_CN",directory=SystemTranslationsPath) or \
            not TranslatorSystemEn.load("qt_en",directory=SystemTranslationsPath):
        sys.exit()
    App.installTranslator(Translator)
    App.installTranslator(TranslatorSystem)
    # 窗口创建
    MainWindow=MyMainWindow(App,Translators=[Translator,TranslatorSystem,TranslatorSystemEn])
    Ui=Gui.MyUi_MainWindow()
    Ui.setupUi(MainWindow)
    MainWindow.show()
    # 执行和关闭部分
    Result=App.exec_()
    sys.exit(Result)
