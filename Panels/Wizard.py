from PyQt5 import QtCore,QtGui,QtWidgets
from Panels.Utils import getTitleHtml,getTextHtmlWithColor
# 重载QLabel类, 以实现接收鼠标双击事件
class MyLabel(QtWidgets.QLabel):
    # 信号定义
    mouseDoubleClick=QtCore.pyqtSignal(int)
    def __init__(self,Id,Parent=None):
        super(MyLabel,self).__init__(Parent)
        self.labelId=Id
    def mouseDoubleClickEvent(self,Event):
        super(MyLabel,self).mouseDoubleClickEvent(Event)
        self.mouseDoubleClick.emit(self.labelId)
# 在重载QLabel类的基础上定义MyLabelList类以实现类列表功能
class MyLabelList(object):
    pass
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
        for Counter in range(MyWizard.Page_Count-1):
            self.labelList.append([MyLabel(Counter+1,self),QtWidgets.QLabel(self)])
            self.labelList[Counter][1].setWordWrap(True)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
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
            r"use <i>View3D</i> and understand the notices when using it."))
        # ViewInfoPage
        self.labelList[MyWizard.Page_ViewInfo-1][0].setText(_translate(
            "WizardPage",getTextHtmlWithColor("How to view the models","Maroon")))
        self.labelList[MyWizard.Page_ViewInfo-1][1].setText(_translate("WizardPage","Hello"))
        # FileMenuPage
        self.labelList[MyWizard.Page_FileMenu-1][0].setText(_translate(
            "WizardPage",getTextHtmlWithColor("About the file menu","Maroon")))
        self.labelList[MyWizard.Page_FileMenu-1][1].setText(_translate("WizardPage","Hello"))
        # FormatInfoPage
        self.labelList[MyWizard.Page_FormatInfo-1][0].setText(_translate(
            "WizardPage",getTextHtmlWithColor("About format conversion","Maroon")))
        self.labelList[MyWizard.Page_FormatInfo-1][1].setText(_translate("WizardPage","Hello"))
        # DocumentPage
        self.labelList[MyWizard.Page_Document-1][0].setText(_translate(
            "WizardPage",getTextHtmlWithColor("Get more help","Maroon")))
        self.labelList[MyWizard.Page_Document-1][1].setText(_translate("WizardPage","Hello"))
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
# 重载QWizard类
class MyWizard(QtWidgets.QWizard):
    # 页码定义
    Page_Intro=0
    Page_ViewInfo=1
    Page_FileMenu=2
    Page_FormatInfo=3
    Page_Document=4
    # 基于页码的常量
    Page_Home=Page_Intro
    Page_Count=5
    def __init__(self,Parent=None):
        super(MyWizard,self).__init__(Parent)
        # 加入页面
        self.setPage(MyWizard.Page_Intro,IntroPage())
        self.setPage(MyWizard.Page_ViewInfo,ViewInfoPage())
        self.setPage(MyWizard.Page_FileMenu,FileMenuPage())
        self.setPage(MyWizard.Page_FormatInfo,FormatInfoPage())
        self.setPage(MyWizard.Page_Document,DocumentPage())
        self.setStartId(MyWizard.Page_Home)
        # 向导设置
        self.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        self.setOption(QtWidgets.QWizard.HaveCustomButton1,True)
        self.setPixmap(QtWidgets.QWizard.LogoPixmap,QtGui.QPixmap(r"Images/logo.png"))
        self.retranslateUi()
        # 连接信号
        self.customButtonClicked.connect(self.backToHomePage)
        self.page(MyWizard.Page_Home).setHomeButtonEnabled.connect(self.setHomeButtonEnabled)
        self.page(MyWizard.Page_Home).jumpToSpecifiedPage.connect(self.jumpToSpecifiedPage)
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Wizard","View3D Help"))
        self.setButtonText(QtWidgets.QWizard.CustomButton1,_translate("Wizard","&Home"))
    # 接收槽定义
    def backToHomePage(self,Which):
        if Which==QtWidgets.QWizard.CustomButton1: self.restart()
    def setHomeButtonEnabled(self,Enable):
        self.button(QtWidgets.QWizard.CustomButton1).setEnabled(Enable)
    def jumpToSpecifiedPage(self,Id):
        JumpTime=Id-self.currentId()
        if JumpTime<=0: return
        for Counter in range(JumpTime): self.next()