QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++11

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

VERSION = "1.0.0"
RC_ICONS = logo.ico
RC_LANG = 0x0004
#QMAKE_TARGET_COMPANY =
#QMAKE_TARGET_COPYRIGHT =
QMAKE_TARGET_PRODUCT = "Viewer3D"
QMAKE_TARGET_DESCRIPTION = 3D Models Viewer

SOURCES += \
    Core/exporterbase.cpp \
    Core/material.cpp \
    Core/model.cpp \
    Models/FbxLoader/fbxexporter.cpp \
    Models/ObjLoader/objexporter.cpp \
    Models/PmxLoader/pmdexporter.cpp \
    Models/PmxLoader/pmxexporter.cpp \
    Classes/mylabel.cpp \
    Classes/mywizard.cpp \
    Classes/mywizardpage.cpp \
    connector.cpp \
    main.cpp \
    mainwindow.cpp \
    utils.cpp

HEADERS += \
    Core/exporterbase.h \
    Core/material.h \
    Core/model.h \
    Models/FbxLoader/fbxexporter.h \
    Models/ObjLoader/objexporter.h \
    Models/PmxLoader/pmdexporter.h \
    Models/PmxLoader/pmxexporter.h \
    Classes/mylabel.h \
    Classes/mywizard.h \
    Classes/mywizardpage.h \
    connector.h \
    mainwindow.h \
    utils.h

FORMS += \
    mainwindow.ui

TRANSLATIONS += \
    Viewer3D_zh_CN.ts

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

RESOURCES += \
    Images/images.qrc

DISTFILES += \
    Models/FbxLoader/FbxLoader.json \
    Models/ObjLoader/ObjLoader.json \
    Models/PmxLoader/PmxLoader.json

win32:CONFIG(release, debug|release): LIBS += -L'D:/VS Resource/Autodesk FBX/FBX SDK/2020.2/lib/vs2019/x86/release/' -llibfbxsdk
else:win32:CONFIG(debug, debug|release): LIBS += -L'D:/VS Resource/Autodesk FBX/FBX SDK/2020.2/lib/vs2019/x86/debug/' -llibfbxsdk

win32:CONFIG(release, debug|release): LIBS += -L'D:/VS Resource/Autodesk FBX/FBX SDK/2020.2/lib/vs2019/x64/release/' -llibfbxsdk
else:win32:CONFIG(debug, debug|release): LIBS += -L'D:/VS Resource/Autodesk FBX/FBX SDK/2020.2/lib/vs2019/x64/debug/' -llibfbxsdk

INCLUDEPATH += 'D:/VS Resource/Autodesk FBX/FBX SDK/2020.2/include'
DEPENDPATH += 'D:/VS Resource/Autodesk FBX/FBX SDK/2020.2/include'
