# coding=utf-8
import sys
from chardet import detect
from PyQt5 import QtWebChannel
from MainWindow import *
from Classes import *
# 重载Ui_MainWindow类
class MyUi_MainWindow(Ui_MainWindow):
    # 初始化
    def __init__(self):
        super(MyUi_MainWindow,self).__init__()
        self.Content=MyDocument()
        self.Home="Resources/default.md"
        # self.Home=os.path.abspath(r"..\..\readme.md")
        self.BackHistory=[]
        self.ForwardHistory=[]
    def setupUi(self,MainWindow):
        super(MyUi_MainWindow,self).setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.sciScintilla.ui=self
        self.webEngineView.ui=self
        # 对Preview(使用QWebEngineView)进行初始化
        self.webEnginePage=MyWebEnginePage(self.MainWindow)
        self.webEngineView.setPage(self.webEnginePage)
        self.sciScintilla.textChanged.connect(lambda:self.Content.setText(
            self.sciScintilla.text()))
        WebChannel=QtWebChannel.QWebChannel(self.MainWindow)
        WebChannel.registerObject("content",self.Content)
        self.webEnginePage.setWebChannel(WebChannel)
        self.webEngineView.setUrl(QtCore.QUrl("qrc:/Resources/index.html"))
        # 对Editor(使用QsciScintilla)进行初始化
        self.openFile(self.Home,"file")
        # 设置各控件是否显示
        self.sciScintilla.setVisible(True)
        # self.webEngineView.setVisible(False)
        self.webEngineView.setVisible(True)
        self.selectToolBar(1)
        # 连接信号和槽
        self.MainWindow.retranslateUi.connect(self.retranslateUi)
        self.webEnginePage.openFile.connect(self.openFile)
        self.sciScintilla.mousePress.connect(self.selectToolBar)
        self.webEngineView.mousePress.connect(self.selectToolBar)
    # 槽函数(接收信号)
    def openFile(self,Filepath,UrlScheme):
        _translate=QtCore.QCoreApplication.translate
        TextFile=QtCore.QFile(Filepath)
        if not TextFile.open(QtCore.QIODevice.ReadOnly):
            if UrlScheme=="qrc":
                QtWidgets.QMessageBox.warning(self.MainWindow,_translate(
                    "MessageBox","Warning Dialog"),_translate(
                    "MessageBox","Failed to open the file on the path \"")+Filepath+_translate(
                    "MessageBox","\"\nThis may be because there is no support for opening \
relative paths that are not in the default file directory or its parent directory"))
            else:
                QtWidgets.QMessageBox.warning(self.MainWindow,_translate(
                    "MessageBox","Warning Dialog"),_translate(
                    "MessageBox","Failed to open the file on the path \"")+Filepath+"\"")
            return
        FileContent=TextFile.readAll().data()
        encoding=detect(FileContent)["encoding"]
        if encoding is None:
            encoding=sys.getdefaultencoding()
            QtWidgets.QMessageBox.warning(self.MainWindow,_translate(
                "MessageBox","Warning Dialog"),_translate(
                "MessageBox","Failed to detect the file encoding, \
the system default encoding will be used, which is \"")+encoding+"\"")
        self.sciScintilla.setText(FileContent.decode(encoding,"replace"))
        self.webEnginePage.CurrentUrl=Filepath
        self.BackHistory.append(self.webEnginePage.CurrentUrl)
    def selectToolBar(self,WidgetNumber):
        self.toolBar_Editor.setVisible(bool(WidgetNumber))
        self.toolBar_Preview.setVisible(bool(not WidgetNumber))