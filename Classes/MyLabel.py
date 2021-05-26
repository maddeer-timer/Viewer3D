# coding=utf-8
from PyQt5 import QtCore,QtGui,QtWidgets
from Panels.Utils import getTextHtmlWithColor
# 重载QLabel类, 以实现接收鼠标双击事件
class MyLabel(QtWidgets.QLabel):
    # 信号定义
    mouseDoubleClick=QtCore.pyqtSignal(int)
    def __init__(self,Id,Parent=None):
        super(MyLabel,self).__init__(Parent)
        self.labelId=Id
        self.colors=["DarkGreen","DarkOliveGreen"]
    def setOriginalText(self,Text):
        self.originalText=Text
        self.textList=[
            getTextHtmlWithColor(self.originalText,self.colors[0]),
            getTextHtmlWithColor(self.originalText,self.colors[1],True),
        ]
        self.setText(self.textList[0])
    def mouseDoubleClickEvent(self,Event):
        super(MyLabel,self).mouseDoubleClickEvent(Event)
        self.mouseDoubleClick.emit(self.labelId)
    def enterEvent(self,Event):
        super(MyLabel,self).enterEvent(Event)
        self.setText(self.textList[1])
        self.setCursor(QtCore.Qt.PointingHandCursor)
    def leaveEvent(self,Event):
        super(MyLabel,self).leaveEvent(Event)
        self.setText(self.textList[0])
        self.setCursor(QtCore.Qt.ArrowCursor)
