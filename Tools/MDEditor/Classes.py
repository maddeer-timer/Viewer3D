# coding=utf-8
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5 import Qsci
# 实用工具类MyDocument, 用来接收并存储编辑器的值
class MyDocument(QtCore.QObject):
    textChanged=QtCore.pyqtSignal(str)
    def __init__(self,Parent=None):
        super(MyDocument,self).__init__(Parent)
        self.Text=""
    def setText(self,Text):
        if Text==self.Text: return
        self.Text=Text
        self.textChanged.emit(self.Text)
# 重载QsciLexerMarkdown
class MyLexerMarkdown(Qsci.QsciLexerMarkdown):
    pass
# 重载QWebEnginePage, 用来阻止页面切换
class MyWebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def acceptNavigationRequest(self,Url,Type,IsMainFrame):
        # 只允许加载 qrc:/index.html
        if Url.scheme()=="qrc": return True
        QtGui.QDesktopServices.openUrl(Url)
        return False