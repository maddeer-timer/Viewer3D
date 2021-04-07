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
        return self.__text
    @text.setter
    def text(self,Text):
        self.__text=Text
    # 初始化
    def __init__(self,Parent=None):
        super(MyDocument,self).__init__(Parent)
        self.text=""
    # 槽函数定义
    def setText(self,Text):
        if Text==self.text: return
        self.text=Text
        self.textChanged.emit(self.text)
# 实用工具类MyContextMenuBuilder, 用于建立MyWebEnginePage的上下文菜单
# 根据Qt5.15.2中的工具类(非API)RenderViewContextMenuQt和QContextMenuBuilder进行Python实现
class MyContextMenuBuilder(object):
    # 初始化
    def __init__(self,ContextMenuDate:QtWebEngineWidgets.QWebEngineContextMenuData,
                 WebEnginePage:QtWebEngineWidgets.QWebEnginePage,
                 ContextMenu:QtWidgets.QMenu,Ui):
        # 需求对象存储
        self._date=ContextMenuDate
        self._page=WebEnginePage
        self._menu=ContextMenu
        self._ui=Ui
        # QAction对象记忆
        self._actions={}
    # 构造菜单函数
    def initMenu(self):
        if self.isFullScreenMode():
            self.appendExitFullscreenItem()
            self.appendSeparatorItem()
        if self._date.isContentEditable() and len(self._date.spellCheckerSuggestions())!=0:
            self.appendSpellingSuggestionItems()
            self.appendSeparatorItem()
        if len(self._date.linkText())==0 and not self._date.linkUrl().isValid() \
                and not self._date.mediaUrl().isValid():
            if self._date.isContentEditable(): self.appendEditableItems()
            elif len(self._date.selectedText())!=0: self.appendCopyItem()
            else: self.appendPageItems()
        else: self.appendPageItems()
        # 无法使用私有类的unfilteredLinkUrl函数
        if self._date.linkUrl().isValid() or len(self._date.linkUrl())!=0:
            self.appendLinkItems()
        if self._date.mediaUrl().isValid():
            MediaType=self._date.mediaType()
            if MediaType==QtWebEngineWidgets.QWebEngineContextMenuData.MediaTypeImage:
                self.appendSeparatorItem()
                self.appendImageItems()
            elif MediaType==QtWebEngineWidgets.QWebEngineContextMenuData.MediaTypeCanvas:
                raise TypeError("Q_UNREACHABLE: MediaUrl is invalid for canvases")
            elif MediaType==QtWebEngineWidgets.QWebEngineContextMenuData.MediaTypeAudio \
                    or MediaType==QtWebEngineWidgets.QWebEngineContextMenuData.MediaTypeVideo:
                self.appendSeparatorItem()
                self.appendMediaItems()
        elif self._date.mediaType()==\
                QtWebEngineWidgets.QWebEngineContextMenuData.MediaTypeCanvas:
            self.appendSeparatorItem()
            self.appendCanvasItems()
        if self.canViewSource() or self.hasInspector():
            self.appendSeparatorItem()
            self.appendDeveloperItems()
    def addMenuItem(self,MenuItem):
        if MenuItem in self._actions:
            Action=self._actions[MenuItem]
            Action.setEnabled(self.isMenuItemEnabled(MenuItem))
            self._menu.addAction(Action)
            return
        _translate=QtCore.QCoreApplication.translate
        Action=None
        DefineFlag=False
        if MenuItem==ContextMenuItem.Back:
            Action=self._ui.action_Back
            Action.setData(QtWebEngineWidgets.QWebEnginePage.Back)
            DefineFlag=True
        elif MenuItem==ContextMenuItem.Forward:
            Action=self._ui.action_Forward
            Action.setData(QtWebEngineWidgets.QWebEnginePage.Forward)
            DefineFlag=True
        elif MenuItem==ContextMenuItem.Reload:
            Action=self._ui.action_Reload
            Action.setData(QtWebEngineWidgets.QWebEnginePage.Reload)
            DefineFlag=True
        elif MenuItem==ContextMenuItem.Cut:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Icon=QtGui.QIcon()
            Icon.addPixmap(QtGui.QPixmap(":/Edit/Images/editcut.png"),
                           QtGui.QIcon.Normal,QtGui.QIcon.Off)
            Action.setIcon(Icon)
            Action.setObjectName("action_Web_Cut")
            Action.setText(_translate("MainWindow","Cu&t"))
            Action.setStatusTip(_translate("MainWindow","Cut to the clipboard"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.Cut)
        elif MenuItem==ContextMenuItem.Copy:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Icon=QtGui.QIcon()
            Icon.addPixmap(QtGui.QPixmap(":/Edit/Images/editcopy.png"),
                           QtGui.QIcon.Normal,QtGui.QIcon.Off)
            Action.setIcon(Icon)
            Action.setObjectName("action_Web_Copy")
            Action.setText(_translate("MainWindow","&Copy"))
            Action.setStatusTip(_translate("MainWindow","Copy to the clipboard"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.Copy)
        elif MenuItem==ContextMenuItem.Paste:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Icon=QtGui.QIcon()
            Icon.addPixmap(QtGui.QPixmap(":/Edit/Images/editpaste.png"),
                           QtGui.QIcon.Normal,QtGui.QIcon.Off)
            Action.setIcon(Icon)
            Action.setObjectName("action_Web_Paste")
            Action.setText(_translate("MainWindow","&Paste"))
            Action.setStatusTip(_translate("MainWindow","Paste from the clipboard"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.Paste)
        elif MenuItem==ContextMenuItem.Undo:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Icon=QtGui.QIcon()
            Icon.addPixmap(QtGui.QPixmap(":/Edit/Images/editundo.png"),
                           QtGui.QIcon.Normal,QtGui.QIcon.Off)
            Action.setIcon(Icon)
            Action.setObjectName("action_Web_Undo")
            Action.setText(_translate("MainWindow","&Undo"))
            Action.setStatusTip(_translate("MainWindow","Undo the last action"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.Undo)
        elif MenuItem==ContextMenuItem.Redo:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Icon=QtGui.QIcon()
            Icon.addPixmap(QtGui.QPixmap(":/Edit/Images/editredo.png"),
                           QtGui.QIcon.Normal,QtGui.QIcon.Off)
            Action.setIcon(Icon)
            Action.setObjectName("action_Web_Redo")
            Action.setText(_translate("MainWindow","&Redo"))
            Action.setStatusTip(_translate("MainWindow","Redo the last undo action"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.Redo)
        elif MenuItem==ContextMenuItem.SelectAll:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Web_Select_All")
            Action.setText(_translate("MainWindow","Select &All"))
            Action.setStatusTip(_translate("MainWindow","Select all"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.SelectAll)
        elif MenuItem==ContextMenuItem.PasteAndMatchStyle:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Web_Paste_And_Match_Style")
            Action.setText(_translate("MainWindow","Paste and match style"))
            Action.setStatusTip(_translate("MainWindow","Paste and match style from the clipboard"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.PasteAndMatchStyle)
        elif MenuItem==ContextMenuItem.OpenLinkInNewWindow:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Open_Link_In_New_Window")
            Action.setText(_translate("MainWindow","Open link in new window"))
            Action.setStatusTip(_translate("MainWindow","Open the link in a new window"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.OpenLinkInNewWindow)
        elif MenuItem==ContextMenuItem.OpenLinkInNewTab:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Open_Link_In_New_Tab")
            Action.setText(_translate("MainWindow","Open link in new tab"))
            Action.setStatusTip(_translate("MainWindow","Open the link in a new tab"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.OpenLinkInNewTab)
        elif MenuItem==ContextMenuItem.CopyLinkToClipboard:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Copy_Link_To_Clipboard")
            Action.setText(_translate("MainWindow","Copy link address"))
            Action.setStatusTip(_translate("MainWindow","Copy link address to the clipboard"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.CopyLinkToClipboard)
        elif MenuItem==ContextMenuItem.DownloadLinkToDisk:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Download_Link_To_Disk")
            Action.setText(_translate("MainWindow","Save link"))
            Action.setStatusTip(_translate("MainWindow","Download content from the link to the disk"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.DownloadLinkToDisk)
        elif MenuItem==ContextMenuItem.CopyImageToClipboard:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Copy_Image_To_Clipboard")
            Action.setText(_translate("MainWindow","Copy image"))
            Action.setStatusTip(_translate("MainWindow","Copy the image to the clipboard"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.CopyImageToClipboard)
        elif MenuItem==ContextMenuItem.CopyImageUrlToClipboard:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Copy_Image_Url_To_Clipboard")
            Action.setText(_translate("MainWindow","Copy image address"))
            Action.setStatusTip(_translate("MainWindow","Copy image address to the clipboard"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.CopyImageUrlToClipboard)
        elif MenuItem==ContextMenuItem.DownloadImageToDisk:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Download_Image_To_Disk")
            Action.setText(_translate("MainWindow","Save image"))
            Action.setStatusTip(_translate("MainWindow","Download the image to the disk"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.DownloadImageToDisk)
        elif MenuItem==ContextMenuItem.CopyMediaUrlToClipboard:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Copy_Media_Url_To_Clipboard")
            Action.setText(_translate("MainWindow","Copy media address"))
            Action.setStatusTip(_translate("MainWindow","Copy media address to the clipboard"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.CopyMediaUrlToClipboard)
        elif MenuItem==ContextMenuItem.ToggleMediaControls:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Toggle_Media_Controls")
            Action.setText(_translate("MainWindow","Show controls"))
            Action.setStatusTip(_translate("MainWindow","Show media controls"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.ToggleMediaControls)
        elif MenuItem==ContextMenuItem.ToggleMediaLoop:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Toggle_Media_Loop")
            Action.setText(_translate("MainWindow","Loop"))
            Action.setStatusTip(_translate("MainWindow","Toggle the media loop mode"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.ToggleMediaLoop)
        elif MenuItem==ContextMenuItem.DownloadMediaToDisk:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Download_Media_To_Disk")
            Action.setText(_translate("MainWindow","Save media"))
            Action.setStatusTip(_translate("MainWindow","Download the media to the disk"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.DownloadMediaToDisk)
        elif MenuItem==ContextMenuItem.InspectElement:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Inspect_Element")
            Action.setText(_translate("MainWindow","Inspect"))
            Action.setStatusTip(_translate("MainWindow","Inspect the elements"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.InspectElement)
        elif MenuItem==ContextMenuItem.ExitFullScreen:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Exit_Full_Screen")
            Action.setText(_translate("MainWindow","Exit full screen"))
            Action.setStatusTip(_translate("MainWindow","Exit the full screen mode"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.ExitFullScreen)
        elif MenuItem==ContextMenuItem.SavePage:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_Save_Page")
            Action.setText(_translate("MainWindow","Save page"))
            Action.setStatusTip(_translate("MainWindow","Save the web page"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.SavePage)
        elif MenuItem==ContextMenuItem.ViewSource:
            Action=QtWidgets.QAction(self._ui.MainWindow)
            Action.setObjectName("action_View_Source")
            Action.setText(_translate("MainWindow","View page source"))
            Action.setStatusTip(_translate("MainWindow","View the page source code"))
            Action.setData(QtWebEngineWidgets.QWebEnginePage.ViewSource)
        elif MenuItem==ContextMenuItem.SpellingSuggestions:
            self.spellCheckerSuggestions=self._date.spellCheckerSuggestions()
            for Index in range(0,min(len(self.spellCheckerSuggestions),4)):
                Action=QtWidgets.QAction(self._ui.MainWindow)
                Action.triggered.connect(lambda:self._page.replaceMisspelledWord(
                    self.spellCheckerSuggestions[Index]))
                Action.setText(self.spellCheckerSuggestions[Index])
                self._menu.addAction(Action)
            return
        elif MenuItem==ContextMenuItem.Separator:
            if not self._menu.isEmpty(): self._menu.addSeparator()
            return
        if not DefineFlag:
            Action.triggered.connect(eval("self._ui.MainWindow.{}".format(
                Action.objectName())))
            self._actions[MenuItem]=Action
        Action.setEnabled(self.isMenuItemEnabled(MenuItem))
        self._menu.addAction(Action)
    def isMenuItemEnabled(self,MenuItem):
        if MenuItem==ContextMenuItem.Back:
            return self.canGoBack()
        elif MenuItem==ContextMenuItem.Forward:
            return self.canGoForward()
        elif MenuItem==ContextMenuItem.Reload:
            return True
        elif MenuItem==ContextMenuItem.Cut:
            return int(self._date.editFlags())\
                   &QtWebEngineWidgets.QWebEngineContextMenuData.CanCut
        elif MenuItem==ContextMenuItem.Copy:
            return int(self._date.editFlags())\
                   &QtWebEngineWidgets.QWebEngineContextMenuData.CanCopy
        elif MenuItem==ContextMenuItem.Paste:
            return int(self._date.editFlags())\
                   &QtWebEngineWidgets.QWebEngineContextMenuData.CanPaste
        elif MenuItem==ContextMenuItem.Undo:
            return int(self._date.editFlags())\
                   &QtWebEngineWidgets.QWebEngineContextMenuData.CanUndo
        elif MenuItem==ContextMenuItem.Redo:
            return int(self._date.editFlags())\
                   &QtWebEngineWidgets.QWebEngineContextMenuData.CanRedo
        elif MenuItem==ContextMenuItem.SelectAll:
            return int(self._date.editFlags())\
                   &QtWebEngineWidgets.QWebEngineContextMenuData.CanSelectAll
        elif MenuItem==ContextMenuItem.PasteAndMatchStyle:
            return int(self._date.editFlags())\
                   &QtWebEngineWidgets.QWebEngineContextMenuData.CanPaste
        elif MenuItem==ContextMenuItem.OpenLinkInNewWindow \
                or MenuItem==ContextMenuItem.OpenLinkInNewTab \
                or MenuItem==ContextMenuItem.CopyLinkToClipboard \
                or MenuItem==ContextMenuItem.DownloadLinkToDisk \
                or MenuItem==ContextMenuItem.CopyImageToClipboard \
                or MenuItem==ContextMenuItem.CopyImageUrlToClipboard \
                or MenuItem==ContextMenuItem.DownloadImageToDisk \
                or MenuItem==ContextMenuItem.CopyMediaUrlToClipboard \
                or MenuItem==ContextMenuItem.ToggleMediaControls \
                or MenuItem==ContextMenuItem.ToggleMediaLoop \
                or MenuItem==ContextMenuItem.DownloadMediaToDisk \
                or MenuItem==ContextMenuItem.InspectElement \
                or MenuItem==ContextMenuItem.ExitFullScreen \
                or MenuItem==ContextMenuItem.SavePage:
            return True
        elif MenuItem==ContextMenuItem.ViewSource:
            return self.canViewSource()
        elif MenuItem==ContextMenuItem.SpellingSuggestions \
                or MenuItem==ContextMenuItem.Separator:
            return True
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
    def hasInspector(self):
        return False
    def isFullScreenMode(self):
        return self._page.view().isFullScreen()
    def canGoBack(self):
        return len(self._ui.BackHistory)==0
    def canGoForward(self):
        return len(self._ui.ForwardHistory)==0
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
        # 初始化菜单及其数据
        ContextMenuDate=self.contextMenuData()
        if not ContextMenuDate: return None
        ContextMenu=QtWidgets.QMenu(self.view())
        # 使用MyContextMenuBuilder添加Action并进行设置
        self.contextMenuBuilder=MyContextMenuBuilder(
            ContextMenuDate,self,ContextMenu,self.view().ui)
        self.contextMenuBuilder.initMenu()
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