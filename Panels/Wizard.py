from PyQt5 import QtCore,QtGui,QtWidgets
# 重载QWizardPage类
# IntroPage: 介绍(1)
class IntroPage(QtWidgets.QWizardPage):
    def __init__(self,parent=None):
        super(IntroPage,self).__init__(parent)
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
        self.setTitle(_translate("WizardPage","Introduction"))
        self.label.setText(_translate("WizardPage","Hello"))
# ViewInfoPage: 模型的查看(2)
class ViewInfoPage(QtWidgets.QWizardPage):
    def __init__(self,parent=None):
        super(ViewInfoPage,self).__init__(parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        # 内容填充

        # 布局设置

        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        pass
# FileMenuPage: 文件菜单(3)
class FileMenuPage(QtWidgets.QWizardPage):
    def __init__(self,parent=None):
        super(FileMenuPage,self).__init__(parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        # 内容填充

        # 布局设置

        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        pass
# FormatInfoPage: 格式转换(4)
class FormatInfoPage(QtWidgets.QWizardPage):
    def __init__(self,parent=None):
        super(FormatInfoPage,self).__init__(parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        # 内容填充

        # 布局设置

        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        pass
# DocumentPage: 结束页-其他说明(5)
class DocumentPage(QtWidgets.QWizardPage):
    def __init__(self,parent=None):
        super(DocumentPage,self).__init__(parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        # 内容填充

        # 布局设置

        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        pass
# 重载QWizard类
class MyWizard(QtWidgets.QWizard):
    # 页码定义
    Page_Intro=0
    Page_ViewInfo=1
    Page_FileMenu=2
    Page_FormatInfo=3
    Page_Document=4
    def __init__(self,parent=None):
        super(MyWizard,self).__init__(parent)
        # 加入页面
        self.setPage(MyWizard.Page_Intro,IntroPage())
        self.setPage(MyWizard.Page_ViewInfo,ViewInfoPage())
        self.setPage(MyWizard.Page_FileMenu,FileMenuPage())
        self.setPage(MyWizard.Page_FormatInfo,FormatInfoPage())
        self.setPage(MyWizard.Page_Document,DocumentPage())
        self.setStartId(MyWizard.Page_Intro)
        # 向导设置
        self.setWizardStyle(QtWidgets.QWizard.ModernStyle)
        self.setPixmap(QtWidgets.QWizard.LogoPixmap,QtGui.QPixmap(r"Images/logo.png"))
        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Wizard","View3D Help"))