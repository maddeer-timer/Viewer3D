# coding=utf-8
from PyQt5 import QtCore,QtGui,QtWidgets
from .MyWizardPages import IntroPage,ViewInfoPage,FileMenuPage,FormatInfoPage,DocumentPage
from .Enumeration import WizardPageItems
# 重载QWizard类
class MyWizard(QtWidgets.QWizard):
    def __init__(self,Parent=None):
        super(MyWizard,self).__init__(Parent)
        # 加入页面
        self.setPage(WizardPageItems.Page_Intro,IntroPage())
        self.setPage(WizardPageItems.Page_ViewInfo,ViewInfoPage())
        self.setPage(WizardPageItems.Page_FileMenu,FileMenuPage())
        self.setPage(WizardPageItems.Page_FormatInfo,FormatInfoPage())
        self.setPage(WizardPageItems.Page_Document,DocumentPage())
        self.setStartId(WizardPageItems.Page_Home)
        # 向导设置
        self.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        self.setOption(QtWidgets.QWizard.HaveCustomButton1,True)
        self.setPixmap(QtWidgets.QWizard.LogoPixmap,QtGui.QPixmap(r"Images/logo.png"))
        self.retranslateUi()
        # 连接信号
        self.customButtonClicked.connect(self.backToHomePage)
        self.page(WizardPageItems.Page_Home).setHomeButtonEnabled\
            .connect(self.setHomeButtonEnabled)
        self.page(WizardPageItems.Page_Home).jumpToSpecifiedPage\
            .connect(self.jumpToSpecifiedPage)
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Wizard","Viewer3D Help"))
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
