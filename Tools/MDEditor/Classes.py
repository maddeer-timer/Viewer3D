# coding=utf-8
import os
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtCore import pyqtProperty
from PyQt5 import QtWebEngineWidgets
from PyQt5 import Qsci
from Enumeration import ContextMenuItem
# 实用工具类MyDocument, 用来接收并存储编辑器的值
class MyDocument(QtCore.QObject):
    # 信号及宏定义
    textChanged=QtCore.pyqtSignal(str)
    # 类属性定义
    @pyqtProperty(str)
    def text(self):
        return self._text
    # 初始化
    def __init__(self,Parent=None):
        super(MyDocument,self).__init__(Parent)
        self._text=""
    # 槽函数定义
    def setText(self,Text):
        if Text==self._text: return
        self._text=Text
        self.textChanged.emit(self._text)
# 实用工具类MyContextMenuBuilder, 用于建立MyWebEnginePage的上下文菜单
# 根据Qt5.15.2中的工具类(非API)RenderViewContextMenuQt和QContextMenuBuilder进行Python实现
class MyContextMenuBuilder(object):
    # 初始化
    def __init__(self,ContextMenuDate:QtWebEngineWidgets.QWebEngineContextMenuData,
                 WebEnginePage:QtWebEngineWidgets.QWebEnginePage,
                 ContextMenu:QtWidgets.QMenu):
        self._date=ContextMenuDate
        self._page=WebEnginePage
        self._menu=ContextMenu
    # 构造菜单函数
    def initMenu(self):
        pass
    def addMenuItem(self,MenuItem):
        pass
    def isMenuItemEnabled(self,MenuItem):
        pass
    # 工具函数
    def appendCanvasItems(self):
        self.addMenuItem(ContextMenuItem.DownloadImageToDisk)
        self.addMenuItem(ContextMenuItem.CopyImageToClipboard)
    def appendCopyItem(self):
        self.addMenuItem(ContextMenuItem.Copy)
    def appendDeveloperItems(self):
        if self.canViewSource(): self.addMenuItem(ContextMenuItem.ViewSource)
        if self.hasInspector(): self.addMenuItem(ContextMenuItem.InspectElement)
    def appendEditableItems(self):
        self.addMenuItem(ContextMenuItem.Undo)
        self.addMenuItem(ContextMenuItem.Redo)
        self.appendSeparatorItem()
        self.addMenuItem(ContextMenuItem.Cut)
        self.addMenuItem(ContextMenuItem.Copy)
        self.addMenuItem(ContextMenuItem.Paste)
        if len(self._date.misspelledWord())==0:
            self.addMenuItem(ContextMenuItem.PasteAndMatchStyle)
            self.addMenuItem(ContextMenuItem.SelectAll)
    def appendExitFullscreenItem(self):
        self.addMenuItem(ContextMenuItem.ExitFullScreen)
    def appendImageItems(self):
        self.addMenuItem(ContextMenuItem.DownloadImageToDisk)
        self.addMenuItem(ContextMenuItem.CopyImageToClipboard)
        self.addMenuItem(ContextMenuItem.CopyImageUrlToClipboard)
    def appendLinkItems(self):
        self.addMenuItem(ContextMenuItem.OpenLinkInNewTab)
        self.addMenuItem(ContextMenuItem.OpenLinkInNewWindow)
        self.appendSeparatorItem()
        self.addMenuItem(ContextMenuItem.DownloadImageToDisk)
        self.addMenuItem(ContextMenuItem.CopyLinkToClipboard)
    def appendMediaItems(self):
        self.addMenuItem(ContextMenuItem.ToggleMediaLoop)
        if int(self._date.mediaFlags())\
                &QtWebEngineWidgets.QWebEngineContextMenuData.MediaCanToggleControls:
            self.addMenuItem(ContextMenuItem.ToggleMediaControls)
        self.addMenuItem(ContextMenuItem.DownloadMediaToDisk)
        self.addMenuItem(ContextMenuItem.CopyMediaUrlToClipboard)
    def appendPageItems(self):
        self.addMenuItem(ContextMenuItem.Back)
        self.addMenuItem(ContextMenuItem.Forward)
        self.addMenuItem(ContextMenuItem.Reload)
        self.appendSeparatorItem()
        self.addMenuItem(ContextMenuItem.SavePage)
    def appendSpellingSuggestionItems(self):
        self.addMenuItem(ContextMenuItem.SpellingSuggestions)
    def appendSeparatorItem(self):
        self.addMenuItem(ContextMenuItem.Separator)
    # 判断函数
    def hasInspector(self): return False
    def isFullScreenMode(self): return self._page.view().isFullScreen()
    def canViewSource(self):
        return len(self._date.linkText())==0 \
               and not self._date.linkUrl().isValid() \
               and not self._date.mediaUrl().isValid() \
               and not self._date.isContentEditable() \
               and len(self._date.selectedText())==0
# 重载QsciLexerMarkdown
class MyLexerMarkdown(Qsci.QsciLexerMarkdown):
    def __init__(self,Parent=None):
        super(MyLexerMarkdown,self).__init__(Parent)
        # 界面设置
        self.setFont(QtGui.QFont("Consolas"))
        self.setPaper(QtGui.QColor("Snow"))
        # 特殊设置
        # -> Default(0): 默认
        # -> Special(1): 特殊
        # -> StrongEmphasisAsterisks(2): 星号重点强调
        # like "**StrongEmphasisAsterisks**"
        Font=QtGui.QFont("Consolas")
        Font.setBold(True)
        self.setFont(Font,Qsci.QsciLexerMarkdown.StrongEmphasisAsterisks)
        # -> StrongEmphasisUnderscores(3): 下划重点强调
        # like "__StrongEmphasisUnderscores__"
        Font=QtGui.QFont("Consolas")
        Font.setBold(True)
        self.setFont(Font,Qsci.QsciLexerMarkdown.StrongEmphasisUnderscores)
        # -> EmphasisAsterisks(4): 星号强调
        # like "*EmphasisAsterisks*"
        Font=QtGui.QFont("Consolas")
        Font.setItalic(True)
        self.setFont(Font,Qsci.QsciLexerMarkdown.EmphasisAsterisks)
        # -> EmphasisUnderscores(5): 下划强调
        # like "_EmphasisUnderscores_"
        Font=QtGui.QFont("Consolas")
        Font.setItalic(True)
        self.setFont(Font,Qsci.QsciLexerMarkdown.EmphasisUnderscores)
        # -> Header(6-11): 标题
        # like "# Header1"
        Font=QtGui.QFont("Consolas")
        Font.setBold(True)
        self.setFont(Font,Qsci.QsciLexerMarkdown.Header1)
        self.setFont(Font,Qsci.QsciLexerMarkdown.Header2)
        self.setFont(Font,Qsci.QsciLexerMarkdown.Header3)
        self.setFont(Font,Qsci.QsciLexerMarkdown.Header4)
        self.setFont(Font,Qsci.QsciLexerMarkdown.Header5)
        self.setFont(Font,Qsci.QsciLexerMarkdown.Header6)
        # -> Prechar(12):
        # -> UnorderedListItem(13): 无序列表项
        # like "* UnorderedListItem"
        Font=QtGui.QFont("Consolas")
        Font.setItalic(True)
        self.setFont(Font,Qsci.QsciLexerMarkdown.UnorderedListItem)
        # -> OrderedListItem(14): 有序列表项
        # like "1. OrderedListItem"
        # -> BlockQuote(15): 块引用
        # like "> BlockQuote"
        Font=QtGui.QFont("Consolas")
        Font.setBold(True)
        self.setFont(Font,Qsci.QsciLexerMarkdown.BlockQuote)
        # -> StrikeOut(16): 删除线
        # like "~~StrikeOut~~"
        self.setColor(QtGui.QColor("Gray"),Qsci.QsciLexerMarkdown.StrikeOut)
        # -> HorizontalRule(17): 水平线
        # -> Link(18): 链接
        # like "[Link](Link)" or "[1]: Link"

        # -> CodeBackticks(19):
        # -> CodeDoubleBackticks(20):
        # -> CodeBlock(21):
# 重载QWebEnginePage, 用来阻止页面切换
class MyWebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    openFile=QtCore.pyqtSignal(str,str)
    def __init__(self,Parent=None):
        super(MyWebEnginePage,self).__init__(Parent)
        self.CurrentUrl=""
    def acceptNavigationRequest(self,Url,Type,IsMainFrame):
        UrlScheme=Url.scheme()
        UrlText=Url.url().replace("/%5C","\\")
        if UrlText=="qrc:/Resources/index.html": return True
        if UrlScheme=="qrc":
            if "qrc:/Resources/" in UrlText: RealPath=UrlText.replace("qrc:/Resources/","")
            else: RealPath=os.path.join("..",UrlText.replace("qrc:/",""))
            RealPath=os.path.abspath(os.path.join(os.path.dirname(
                self.CurrentUrl),RealPath))
            self.openFile.emit(RealPath,"qrc")
        elif UrlScheme=="file": self.openFile.emit(UrlText.replace("file:///",""),"file")
        else: QtGui.QDesktopServices.openUrl(Url)
        return False
    def createStandardContextMenu(self):
        # 初始化
        if not hasattr(self,"ui"): self.ui=self.view().ui
        ContextMenuDate=self.contextMenuData()
        if not ContextMenuDate: return None
        ContextMenu=QtWidgets.QMenu(self.view())
        # 使用MyContextMenuBuilder添加Action并进行设置
        ContextMenuBuilder=MyContextMenuBuilder(ContextMenuDate,self,ContextMenu)
        ContextMenuBuilder.initMenu()
        return ContextMenu
# 重载QsciScintilla
class MysciScintilla(Qsci.QsciScintilla):
    mousePress=QtCore.pyqtSignal(int)
    def __init__(self,Parent=None):
        # 初始设置
        super(MysciScintilla,self).__init__(Parent)
        self.ui=None
        # 编辑器配置
        self.setUtf8(True)
        LexerMarkdown=MyLexerMarkdown(self)
        self.setLexer(LexerMarkdown)
    def mousePressEvent(self,*args,**kwargs):
        super(MysciScintilla,self).mousePressEvent(*args,**kwargs)
        self.mousePress.emit(1)
    def contextMenuEvent(self,Event):
        # 目前不能完全实现原功能
        ContextMenu=self.createStandardContextMenu()
        if ContextMenu is not None:
            ContextMenu.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
            ContextMenu.popup(Event.globalPos())
    def createStandardContextMenu(self):
        ReadOnly=self.isReadOnly()
        HasSelectedText=self.hasSelectedText()
        ContextMenu=QtWidgets.QMenu(self)
        if not ReadOnly:
            ContextMenu.addAction(self.ui.action_Undo)
            self.ui.action_Undo.setEnabled(self.isUndoAvailable())
            ContextMenu.addAction(self.ui.action_Redo)
            self.ui.action_Redo.setEnabled(self.isRedoAvailable())
            ContextMenu.addSeparator()
            ContextMenu.addAction(self.ui.action_Cut)
            self.ui.action_Cut.setEnabled(HasSelectedText)
        ContextMenu.addAction(self.ui.action_Copy)
        self.ui.action_Copy.setEnabled(HasSelectedText)
        if not ReadOnly:
            ContextMenu.addAction(self.ui.action_Paste)
            self.ui.action_Paste.setEnabled(self.SendScintilla(
                Qsci.QsciScintilla.SCI_CANPASTE))
            ContextMenu.addAction(self.ui.action_Delete)
            self.ui.action_Delete.setEnabled(HasSelectedText)
        if not ContextMenu.isEmpty(): ContextMenu.addSeparator()
        ContextMenu.addAction(self.ui.action_Select_All)
        self.ui.action_Select_All.setEnabled(self.length()!=0)
        return ContextMenu
# 重载QWebEngineView
class MyWebEngineView(QtWebEngineWidgets.QWebEngineView):
    mousePress=QtCore.pyqtSignal(int)
    def __init__(self,Parent=None):
        super(MyWebEngineView,self).__init__(Parent)
        self._ChildObject=None
        self.ui=None
    def event(self,Event):
        if Event.type()==QtCore.QEvent.ChildPolished:
            self._ChildObject=Event.child()
            if self._ChildObject!=None: self._ChildObject.installEventFilter(self)
        return super(MyWebEngineView,self).event(Event)
    def eventFilter(self,Object,Event):
        if Object==self._ChildObject and \
                Event.type()==QtCore.QEvent.MouseButtonPress:
            self.mousePress.emit(0)
        return super(MyWebEngineView,self).eventFilter(Object,Event)
    def contextMenuEvent(self,Event):
        # 目前不能完全实现原功能
        ContextMenu=self.page().createStandardContextMenu()
        if ContextMenu is not None:
            ContextMenu.setAttribute(QtCore.Qt.WA_DeleteOnClose,True)
            ContextMenu.popup(Event.globalPos())