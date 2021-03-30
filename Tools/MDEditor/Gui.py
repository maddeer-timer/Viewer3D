# coding=utf-8
from PyQt5 import QtWebChannel
from MainWindow import *
from Classes import *
# 重载Ui_MainWindow类
class MyUi_MainWindow(Ui_MainWindow):
    # 初始化
    def __init__(self):
        super(MyUi_MainWindow,self).__init__()
        self.Content=MyDocument()
    def setupUi(self,MainWindow):
        super(MyUi_MainWindow,self).setupUi(MainWindow)
        # 对Editor(使用QsciScintilla)进行设置
        self.sciScintilla.setUtf8(True)
        LexerMarkdown=MyLexerMarkdown(self.sciScintilla)
        self.sciScintilla.setLexer(LexerMarkdown)
        # 对Preview(使用QWebEngineView)进行初始化
        WebEnginePage=MyWebEnginePage(MainWindow)
        self.webEngineView.setPage(WebEnginePage)
        self.sciScintilla.textChanged.connect(lambda:self.Content.setText(
            self.sciScintilla.text()))
        WebChannel=QtWebChannel.QWebChannel(MainWindow)
        WebChannel.registerObject("content",self.Content)
        WebEnginePage.setWebChannel(WebChannel)
        self.webEngineView.setUrl(QtCore.QUrl("qrc:/Resources/index.html"))
        # 对Editor(使用QsciScintilla)进行初始化
        defaultTextFile=QtCore.QFile(":/Resources/default.md")
        defaultTextFile.open(QtCore.QIODevice.ReadOnly)
        self.sciScintilla.setText(defaultTextFile.readAll().data().decode("UTF-8"))
        # 设置Editor和Preview的显示与否
        self.sciScintilla.setVisible(True)
        self.webEngineView.setVisible(False)
        # 连接信号和槽
        MainWindow.retranslateUi.connect(self.retranslateUi)