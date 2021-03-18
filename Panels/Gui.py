# coding=utf-8
from Panels.MainWindow import *
# 重载Ui_MainWindow
class MyUi_MainWindow(Ui_MainWindow):
    def setupUi(self,MainWindow):
        super(MyUi_MainWindow,self).setupUi(MainWindow)
        self.openGLWidget=QtWidgets.QOpenGLWidget(self.centralwidget)
        self.openGLWidget.setGeometry(QtCore.QRect(0,0,640,435))
        self.openGLWidget.setObjectName("openGLWidget")