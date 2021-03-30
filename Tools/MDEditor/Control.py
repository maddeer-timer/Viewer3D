# coding=utf-8
import os
import sys
import traceback
import argparse
from PyQt5 import QtCore,QtGui,QtWidgets
import Gui
import Classes
# 重载QMainWindow类
class MyMainWindow(QtWidgets.QMainWindow):
    # 信号(请求槽)
    retranslateUi=QtCore.pyqtSignal(QtWidgets.QMainWindow)  # 请求刷新界面
    # 初始化,销毁函数
    def __init__(self,App,Translators):
        super(MyMainWindow,self).__init__()
        # 主变量
        self.App=App
        self.Translators=Translators
        pass
    def closeEvent(self,Event):
        super(MyMainWindow,self).closeEvent(Event)
        # destroy()
        sys.exit()
    # 处理函数
    # -> Menu_File
    def action_New(self):
        pass
    def action_Open(self):
        pass
    def action_Open_Folder(self):
        pass
    def action_Save(self):
        pass
    def action_Save_As(self):
        pass
    def action_Rename(self):
        pass
    def action_Reload(self):
        pass
    def action_Close(self):
        pass
    def action_Setting(self):
        pass
    def action_Encoding(self):
        pass
    def action_Read_Only(self):
        pass
    def action_CRLF_Windows(self):
        pass
    def action_LF_Unix(self):
        pass
    def action_CR_MacOS(self):
        pass
    def action_Exit(self):
        pass
    # -> Menu_Edit
    def action_Undo(self):
        pass
    def action_Redo(self):
        pass
    def action_Cut(self):
        pass
    def action_Copy(self):
        pass
    def action_Paste(self):
        pass
    def action_Delete(self):
        pass
    def action_Select_All(self):
        pass
    def action_Find(self):
        pass
    def action_Replace(self):
        pass
    def action_Goto(self):
        pass
    def action_Always_On_Top(self):
        pass
    def action_Word_Wrap(self):
        pass
    # -> Menu_View
    def action_Editor(self):
        pass
    def action_Preview(self):
        pass
    def action_Both(self):
        pass
    # -> Menu_Help
    def action_Help(self):
        pass
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
    def action_About(self):
        pass
    def action_About_MarkDown(self):
        pass
    # 槽(接收信号)
    def menubarTriggered(self,Action):
        # 直接执行对应的函数代码
        try:
            exec("self.{}()".format(Action.objectName()))
        except:
            traceback.print_exc()
            self.close()
    def toolbarTriggered(self,Action):
        # 直接执行对应的函数代码(因为会重复执行所以pass)
        pass
# 主函数
def main():
    # 初始化部分
    App=QtWidgets.QApplication(sys.argv)
    SystemTranslationsPath=QtCore.QLibraryInfo.location(QtCore.QLibraryInfo.TranslationsPath)
    # 翻译载入部分
    Translator=QtCore.QTranslator()
    TranslatorSystem=QtCore.QTranslator()
    TranslatorSystemEn=QtCore.QTranslator()
    if not Translator.load("MDEditor_zh_CN",directory="Translations") or \
            not TranslatorSystem.load("qt_zh_CN", directory=SystemTranslationsPath) or \
            not TranslatorSystemEn.load("qt_en", directory=SystemTranslationsPath):
        # sys.exit()
        pass
    # 窗口创建
    MainWindow=MyMainWindow(App,Translators=[Translator,TranslatorSystem,TranslatorSystemEn])
    Ui=Gui.MyUi_MainWindow()
    Ui.setupUi(MainWindow)
    MainWindow.show()
    # 解析其他命令行参数
    parse=argparse.ArgumentParser(
        description="MarkDown Editor: 一个Markdown编辑器, 可以用来编写"
                    "和预览Markdown文档, 主要通过Qt实现。",
        epilog="关于其他命令行选项, 请参照Qt的官方文档 "
               "https://doc.qt.io/qt-5/qapplication.html#QApplication",
        allow_abbrev=False)
    parse.add_argument("file",nargs='?',default=argparse.SUPPRESS,help="要打开的Markdown文件")
    parse.add_argument("-l","--language",default="zh_CN",choices=["zh_CN","en_US"],
                       help="设置应用程序界面使用的语言")
    args=parse.parse_args()
    # 处理得到的命令行参数
    if args.language=="zh_CN": MainWindow.action_Chinese()
    elif args.languaga=="en_US": MainWindow.action_English()
    if "file" in args:
        pass
    # 执行和关闭部分
    Result=App.exec_()
    sys.exit(Result)