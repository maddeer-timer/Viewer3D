# coding=utf-8
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import pyqtProperty
from PyQt5 import QtWebEngineWidgets
from PyQt5 import Qsci
# 实用工具类MyDocument, 用来接收并存储编辑器的值
class MyDocument(QtCore.QObject):
    # 信号及宏定义
    textChanged=QtCore.pyqtSignal(str)
    # 类属性定义
    @pyqtProperty(str)
    def text(self):
        return self._text
    # 初始化
    def __init__(self,Parent=None):
        super(MyDocument,self).__init__(Parent)
        self._text=""
    # 槽函数定义
    def setText(self,Text):
        if Text==self._text: return
        self._text=Text
        self.textChanged.emit(self._text)
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