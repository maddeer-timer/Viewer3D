from PyQt5 import QtCore,QtGui,QtWidgets
# 重载QWizardPage类
class MyWizardPage(QtWidgets.QWizardPage):
    def __init__(self):
        super(MyWizardPage,self).__init__()
    pass
# 重载QWizard类
class MyWizard(QtWidgets.QWizard):
    def __init__(self):
        super(MyWizard,self).__init__()
    pass