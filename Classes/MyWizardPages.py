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
        self.labelList=[]
        for Counter in range(3):
            self.labelList.append(QtWidgets.QLabel(self))
            self.labelList[Counter].setWordWrap(True)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        for Counter in range(len(self.labelList)):
            if Counter!=0: self.layout.addSpacing(10)
            self.layout.addWidget(self.labelList[Counter])
        self.setLayout(self.layout)
        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setTitle(getTitleHtml(_translate(
            "WizardPage","How to view the models<br/>"),"Consolas"))
        self.setSubTitle(getTitleHtml(_translate(
            "WizardPage","Explain how to move, rotate and scale the model."),"Consolas"))
        self.labelList[0].setText(_translate(
            "WizardPage","<ul><li>You can use the left mouse button to move the model, the \
model will be moved to the same position relative to the mouse position.</li></ul>"))
        self.labelList[1].setText(_translate(
            "WizardPage","<ul><li>You can use the right mouse button to rotate the model, \
according to the rotation mode \"XYZ Euler\", move the mouse left and right to rotate \
horizontally (change the Z value), move the mouse up and down to flip vertically (change \
the Y value), Alt+any direction to rotate in the plane (change the X value), the specific \
rotation Angle is determined by the distance from the mouse to its initial position.</li></ul>"))
        self.labelList[2].setText(_translate(
            "WizardPage","<ul><li>You can scroll the middle mouse button to zoom in and out \
the model. scroll forward to zoom in, and scroll backwards to zoom out.</li></ul>"))
# FileMenuPage: 文件菜单(3)
class FileMenuPage(QtWidgets.QWizardPage):
    def __init__(self,Parent=None):
        super(FileMenuPage,self).__init__(Parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        # 内容填充
        self.labelList=[]
        for Counter in range(1):
            self.labelList.append(QtWidgets.QLabel(self))
            self.labelList[Counter].setWordWrap(True)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        for Counter in range(len(self.labelList)):
            if Counter!=0: self.layout.addSpacing(10)
            self.layout.addWidget(self.labelList[Counter])
        self.setLayout(self.layout)
        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setTitle(getTitleHtml(_translate(
            "WizardPage","About the file menu<br/>"),"Consolas"))
        self.setSubTitle(getTitleHtml(_translate(
            "WizardPage","Explain the related problems of the file menu."),"Consolas"))
        self.labelList[0].setText(_translate(
            "WizardPage","<ul><li>The Model doesn't close while opening another model. You \
can use the shortcut \"Ctrl+F\" or click \"View>File menu\" to view the opened models. To \
close the current model, please use the shortcut \"Ctrl+C\" or click \"File>Close\".</li></ul>"))
# FormatInfoPage: 格式转换(4)
class FormatInfoPage(QtWidgets.QWizardPage):
    def __init__(self,Parent=None):
        super(FormatInfoPage,self).__init__(Parent)
        # 基本设置
        self.setFont(QtGui.QFont("Consolas"))
        # 内容填充
        self.labelList=[]
        for Counter in range(2):
            self.labelList.append(QtWidgets.QLabel(self))
            self.labelList[Counter].setWordWrap(True)
        # 布局设置
        self.layout=QtWidgets.QVBoxLayout()
        for Counter in range(len(self.labelList)):
            if Counter!=0: self.layout.addSpacing(10)
            self.layout.addWidget(self.labelList[Counter])
        self.setLayout(self.layout)
        self.retranslateUi()
    def retranslateUi(self):
        _translate=QtCore.QCoreApplication.translate
        self.setTitle(getTitleHtml(_translate(
            "WizardPage","About format conversion<br/>"),"Consolas"))
        self.setSubTitle(getTitleHtml(_translate(
            "WizardPage","Explain the related problems of format conversion."),"Consolas"))
        self.labelList[0].setText(_translate(
            "WizardPage","<ul><li>You can use the shortcut \"Ctrl+E\" or click \
\"File>Export\" to export the model.</li></ul>"))
        self.labelList[1].setText(_translate("WizardPage","""
<ul>
	<li>Only support some common formats, the list is as follows: 
		<ol>
			<li>Wavefront(Default)(.obj)</li>
			<li>FBX(.fbx)</li>
			<li>MikuMikuDance Model(.pmx)</li>
		</ol>
	</li>
</ul>"""))
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
            # self.labelList[Counter].setWordWrap(True)
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
