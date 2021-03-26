from PyQt5 import QtCore,QtGui,QtWidgets
# 重载QWizardPage类
# IntroPage: 介绍(1)
class IntroPage(QtWidgets.QWizardPage):
    def __init__(self):
        super(IntroPage,self).__init__()
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
        self.setTitle(_translate("WizardPage","Introduction"))
        self.label.setText(_translate("WizardPage","Hello"))
# ViewInfoPage: 模型的查看(2)
class ViewInfoPage(QtWidgets.QWizardPage):
    def __init__(self):
        super(ViewInfoPage,self).__init__()
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
    def __init__(self):
        super(FileMenuPage,self).__init__()
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
    def __init__(self):
        super(FormatInfoPage,self).__init__()
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
    def __init__(self):
        super(DocumentPage,self).__init__()
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
    def __init__(self):
        super(MyWizard,self).__init__()
        # 加入页面
        self.addPage(IntroPage())
        self.addPage(ViewInfoPage())
        self.addPage(FileMenuPage())
        self.addPage(FormatInfoPage())
        self.addPage(DocumentPage())
        # 向导设置
        self.retranslateUi()
        self.setWizardStyle(QtWidgets.QWizard.ClassicStyle)
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Wizard","Help Wizard"))