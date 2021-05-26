# coding=utf-8
from PyQt5 import QtCore,QtGui,QtWidgets
from .MyLabel import MyLabel
from .Enumeration import WizardPageItems
from Panels.Utils import getTitleHtml
# 重载QWizardPage类
# IntroPage: 介绍(1)
class IntroPage(QtWidgets.QWizardPage):
    # 信号定义
    setHomeButtonEnabled=QtCore.pyqtSignal(bool)
    jumpToSpecifiedPage=QtCore.pyqtSignal(int)
    def __init__(self,Parent=None):
        super(IntroPage,self).__init__(Parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        self.setPixmap(QtWidgets.QWizard.WatermarkPixmap,QtGui.QPixmap(r"Images/watermark.png"))
        # 内容填充
        self.label=QtWidgets.QLabel(self)
        self.label.setWordWrap(True)
        self.labelList=[]
        for Counter in range(WizardPageItems.Page_Count-1):
            self.labelList.append([MyLabel(Counter+1,self),QtWidgets.QLabel(self)])
            self.labelList[Counter][1].setWordWrap(True)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addSpacing(40)
        self.subLayout=QtWidgets.QVBoxLayout()
        for Counter in range(len(self.labelList)):
            self.subLayout.addWidget(self.labelList[Counter][0])
            self.subLayout.addWidget(self.labelList[Counter][1])
        self.layout.addLayout(self.subLayout)
        self.setLayout(self.layout)
        self.retranslateUi()
        # 连接信号
        for Counter in range(len(self.labelList)):
            self.labelList[Counter][0].mouseDoubleClick.connect(self.jumpToSpecifiedPageEvent)
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setTitle(getTitleHtml(_translate("WizardPage","Introduction"),"Consolas"))
        self.label.setText(_translate("WizardPage",r"This wizard will help you learn how to "
            r"use <i>Viewer3D</i> and understand the notices when using it."))
        # ViewInfoPage
        self.labelList[WizardPageItems.Page_ViewInfo-1][0].setOriginalText(
            _translate("WizardPage","How to view the models"))
        self.labelList[WizardPageItems.Page_ViewInfo-1][1].setText(_translate(
            "WizardPage",""))
        # FileMenuPage
        self.labelList[WizardPageItems.Page_FileMenu-1][0].setOriginalText(
            _translate("WizardPage","About the file menu"))
        self.labelList[WizardPageItems.Page_FileMenu-1][1].setText(_translate(
            "WizardPage",""))
        # FormatInfoPage
        self.labelList[WizardPageItems.Page_FormatInfo-1][0].setOriginalText(
            _translate("WizardPage","About format conversion"))
        self.labelList[WizardPageItems.Page_FormatInfo-1][1].setText(_translate(
            "WizardPage",""))
        # DocumentPage
        self.labelList[WizardPageItems.Page_Document-1][0].setOriginalText(
            _translate("WizardPage","Get more help"))
        self.labelList[WizardPageItems.Page_Document-1][1].setText(_translate(
            "WizardPage",""))
    def showEvent(self,Event):
        super(IntroPage,self).showEvent(Event)
        self.setHomeButtonEnabled.emit(False)
    def hideEvent(self,Event):
        super(IntroPage,self).hideEvent(Event)
        self.setHomeButtonEnabled.emit(True)
    # 接收槽定义
    def jumpToSpecifiedPageEvent(self,LabelId):
        self.jumpToSpecifiedPage.emit(LabelId)
# ViewInfoPage: 模型的查看(2)
class ViewInfoPage(QtWidgets.QWizardPage):
    def __init__(self,Parent=None):
        super(ViewInfoPage,self).__init__(Parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        # 内容填充
        self.label=QtWidgets.QLabel(self)
        self.label.setWordWrap(True)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setTitle(getTitleHtml(_translate("WizardPage","How to view the models"),"Consolas"))
        self.setSubTitle(getTitleHtml(_translate("WizardPage","Hello"),"Consolas"))
        self.label.setText(_translate("WizardPage","Hello"))
# FileMenuPage: 文件菜单(3)
class FileMenuPage(QtWidgets.QWizardPage):
    def __init__(self,Parent=None):
        super(FileMenuPage,self).__init__(Parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        # 内容填充
        self.label=QtWidgets.QLabel(self)
        self.label.setWordWrap(True)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setTitle(getTitleHtml(_translate("WizardPage","About the file menu"),"Consolas"))
        self.setSubTitle(getTitleHtml(_translate("WizardPage","Hello"),"Consolas"))
        self.label.setText(_translate("WizardPage","Hello"))
# FormatInfoPage: 格式转换(4)
class FormatInfoPage(QtWidgets.QWizardPage):
    def __init__(self,Parent=None):
        super(FormatInfoPage,self).__init__(Parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        # 内容填充
        self.label=QtWidgets.QLabel(self)
        self.label.setWordWrap(True)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setTitle(getTitleHtml(_translate("WizardPage","About format conversion"),"Consolas"))
        self.setSubTitle(getTitleHtml(_translate("WizardPage","Hello"),"Consolas"))
        self.label.setText(_translate("WizardPage","Hello"))
# DocumentPage: 结束页-其他说明(5)
class DocumentPage(QtWidgets.QWizardPage):
    def __init__(self,Parent=None):
        super(DocumentPage,self).__init__(Parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        self.setPixmap(QtWidgets.QWizard.WatermarkPixmap,QtGui.QPixmap(r"Images/watermark.png"))
        # 内容填充
        self.label=QtWidgets.QLabel(self)
        self.label.setWordWrap(True)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setTitle(getTitleHtml(_translate("WizardPage","Get more help"),"Consolas"))
        self.label.setText(_translate("WizardPage","Hello"))
