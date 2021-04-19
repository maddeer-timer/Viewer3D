QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11 qscintilla2

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

VERSION = "1.0.0"
RC_ICONS = logo.ico
RC_LANG = 0x0004
#QMAKE_TARGET_COMPANY =
#QMAKE_TARGET_COPYRIGHT =
QMAKE_TARGET_PRODUCT = "MDEditor"
QMAKE_TARGET_DESCRIPTION = MarkDown Editor

SOURCES += \
    Classes/mycontextmenubuilder.cpp \
    Classes/mysciscintilla.cpp \
    Classes/mywebengineview.cpp \
    main.cpp \
    mainwindow.cpp

HEADERS += \
    Classes/mycontextmenubuilder.h \
    Classes/mysciscintilla.h \
    Classes/mywebengineview.h \
    mainwindow.h

FORMS += \
    mainwindow.ui

TRANSLATIONS += \
    MDEditor_zh_CN.ts

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES += \
    Images/images.qrc \
    Resources/resources.qrc

DISTFILES +=
