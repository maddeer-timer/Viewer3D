# coding=utf-8
from Panels.MainWindow import *
# 重载QOpenGLWidget类
class MyOpenGLWidget(QtWidgets.QOpenGLWidget):
    pass
# 重载Ui_MainWindow类
class MyUi_MainWindow(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super(MyUi_MainWindow,self).setupUi(MainWindow)
        self.listWidget.setVisible(False)
        self.openGLWidget=MyOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(0,0,640,435))
        self.openGLWidget.setObjectName("openGLWidget")
        MainWindow.updateList.connect(self.updateList)
        MainWindow.updateView.connect(self.updateView)
        MainWindow.getSelected.connect(self.getSelected)
        MainWindow.retranslateUi.connect(self.retranslateUi)
    def updateList(self,ModelList):
        # 更新文件菜单列表
        for ModelName in ModelList:
            ModelItem=QtWidgets.QListWidgetItem(ModelName)
            self.listWidget.addItem(ModelItem)
    def updateView(self,CurrentModel,Location,Rotation):
        # 刷新OpenGL显示界面内容
        pass
    def getSelected(self):
        # 获取当前选择的内容
        pass