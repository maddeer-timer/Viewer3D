# coding=utf-8
from PyQt5 import QtCore,QtGui,QtWidgets
from .MyLabel import MyLabel
from .Enumeration import WizardPageItems
from Panels.Utils import getTitleHtml,getFileNameFromHtml
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
            self.labelList.append([MyLabel(Counter,self),QtWidgets.QLabel(self)])
            self.labelList[Counter][1].setWordWrap(True)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addSpacing(25)
        self.subLayout=QtWidgets.QVBoxLayout()
        for Counter in range(len(self.labelList)):
            if Counter!=0: self.subLayout.addSpacing(10)
            HBoxLayout=QtWidgets.QHBoxLayout()
            HBoxLayout.addWidget(self.labelList[Counter][0])
            SpacerItem=QtWidgets.QSpacerItem(0,0,QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
            HBoxLayout.addSpacerItem(SpacerItem)
            self.subLayout.addLayout(HBoxLayout)
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
        self.label.setText(_translate(
            "WizardPage",r"This wizard will help you learn how to use <i>Viewer3D</i> "
                         r"and understand the notices when using it."))
        # ViewInfoPage
        self.labelList[WizardPageItems.Page_ViewInfo-1][0].setOriginalText(
            _translate("WizardPage","View"))
        self.labelList[WizardPageItems.Page_ViewInfo-1][1].setText(_translate(
            "WizardPage","How to view the models"))
        # FileMenuPage
        self.labelList[WizardPageItems.Page_FileMenu-1][0].setOriginalText(
            _translate("WizardPage","File Menu"))
        self.labelList[WizardPageItems.Page_FileMenu-1][1].setText(_translate(
            "WizardPage","About the file menu"))
        # FormatInfoPage
        self.labelList[WizardPageItems.Page_FormatInfo-1][0].setOriginalText(
            _translate("WizardPage","Format"))
        self.labelList[WizardPageItems.Page_FormatInfo-1][1].setText(_translate(
            "WizardPage","About format conversion"))
        # DocumentPage
        self.labelList[WizardPageItems.Page_Document-1][0].setOriginalText(
            _translate("WizardPage","Help"))
        self.labelList[WizardPageItems.Page_Document-1][1].setText(_translate(
            "WizardPage","Get more help"))
    def showEvent(self,Event):
        super(IntroPage,self).showEvent(Event)
        self.setHomeButtonEnabled.emit(False)
    def hideEvent(self,Event):
        super(IntroPage,self).hideEvent(Event)
        self.setHomeButtonEnabled.emit(True)
    # 接收槽定义
    def jumpToSpecifiedPageEvent(self,LabelId):
        self.jumpToSpecifiedPage.emit(LabelId+1)
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
        self.label1=QtWidgets.QLabel(self)
        self.label1.setWordWrap(True)
        self.labelList=[]
        for Counter in range(1):
            self.labelList.append(MyLabel(Counter,self))
            self.labelList[Counter].setWordWrap(True)
        self.label2=QtWidgets.QLabel(self)
        self.label2.setWordWrap(True)
        self.UrlLabel=MyLabel(0,self)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label1)
        self.layout.addSpacing(25)
        self.subLayout=QtWidgets.QVBoxLayout()
        for Counter in range(len(self.labelList)):
            if Counter!=0: self.subLayout.addSpacing(10)
            HBoxLayout=QtWidgets.QHBoxLayout()
            HBoxLayout.addWidget(self.labelList[Counter])
            SpacerItem=QtWidgets.QSpacerItem(0,0,QtWidgets.QSizePolicy.Expanding,
                                             QtWidgets.QSizePolicy.Minimum)
            HBoxLayout.addSpacerItem(SpacerItem)
            self.subLayout.addLayout(HBoxLayout)
        self.layout.addLayout(self.subLayout)
        self.layout.addSpacing(25)
        self.layout.addWidget(self.label2)
        HBoxLayout=QtWidgets.QHBoxLayout()
        HBoxLayout.addWidget(self.UrlLabel)
        SpacerItem=QtWidgets.QSpacerItem(0,0,QtWidgets.QSizePolicy.Expanding,
                                         QtWidgets.QSizePolicy.Minimum)
        HBoxLayout.addSpacerItem(SpacerItem)
        self.layout.addLayout(HBoxLayout)
        self.setLayout(self.layout)
        self.retranslateUi()
        # 连接信号
        for Counter in range(len(self.labelList)):
            self.labelList[Counter].mouseDoubleClick.connect(self.openSpecifiedFile)
        self.UrlLabel.mouseDoubleClick.connect(self.openSpecifiedUrl)
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setTitle(getTitleHtml(_translate("WizardPage","Get more help"),"Consolas"))
        self.label1.setText(_translate(
            "WizardPage","For more help, see the files in the application root directory: "))
        self.labelList[0].setOriginalText(_translate(
            "WizardPage","<ul><li>readme.md&nbsp;(English)</li></ul>"))
        self.label2.setText(_translate(
            "WizardPage","you can use <i>MDEditor</i> to view these Markdown documents."))
        self.UrlLabel.setOriginalText(_translate("WizardPage","You can find it here."))
    # 接收槽定义
    def openSpecifiedFile(self,LabelId):
        FileName=getFileNameFromHtml(self.labelList[LabelId].text())[0]
        OpenSuccess=QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(FileName))
        if not OpenSuccess:
            _translate=QtCore.QCoreApplication.translate
            QtWidgets.QMessageBox.warning(self.wizard(),_translate(
                "MessageBox","Warning Dialog"),_translate(
                "MessageBox","Failed to open the file named \"")+FileName+_translate(
                "MessageBox","\"","Dialog for failed file open"))
    def openSpecifiedUrl(self,LabelId):
        UrlPath="https://www.github.com/maddeer-timer/MDEditor"
        OpenSuccess=QtGui.QDesktopServices.openUrl(QtCore.QUrl(UrlPath))
        if not OpenSuccess:
            _translate=QtCore.QCoreApplication.translate
            QtWidgets.QMessageBox.warning(self.wizard(),_translate(
                "MessageBox","Warning Dialog"),_translate(
                "MessageBox","Failed to open \"")+UrlPath+_translate(
                "MessageBox","\"","Dialog for failed URL open"))
