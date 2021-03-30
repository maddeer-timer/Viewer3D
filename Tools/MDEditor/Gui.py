# coding=utf-8
from PyQt5 import QtWebChannel
from MainWindow import *
from Classes import *
# 重载Ui_MainWindow类
class MyUi_MainWindow(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super(MyUi_MainWindow,self).setupUi(MainWindow)
        # 对Editor(使用QsciScintilla)进行初始化

        # 对Preview(使用QWebEngineView)进行初始化
        WebEnginePage=MyWebEnginePage(MainWindow)
        self.webEngineView.setPage(WebEnginePage)
        self.webEngineView.setUrl(QtCore.QUrl("qrc:/Resources/Index.html"))
        # 设置Editor和Preview的显示与否
        self.displayEditor(True)
        self.displayPreview(False)
        # 连接信号和槽
        MainWindow.retranslateUi.connect(self.retranslateUi)
    def displayEditor(self,Visible):
        pass
    def displayPreview(self,Visible):
        pass