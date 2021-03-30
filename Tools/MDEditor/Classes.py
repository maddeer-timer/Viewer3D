# coding=utf-8
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5 import QtWebChannel,QtWebEngineWidgets
from PyQt5 import Qsci
# 重载QsciLexerMarkdown
class MyLexerMarkdown(Qsci.QsciLexerMarkdown):
    pass
# 重载QWebEnginePage, 用来显示预览
class MyWebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    pass