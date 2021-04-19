#ifndef MYWEBENGINEVIEW_H
#define MYWEBENGINEVIEW_H

#include <QObject>
#include <QtWebEngineWidgets/QWebEngineView>

// 实用工具类MyDocument, 用来接收并存储编辑器的值
class MyDocument : public QObject
{
public:
    MyDocument();
};

// 重载QWebEnginePage, 用来阻止页面切换
class MyWebEnginePage : public QWebEnginePage
{
public:
    MyWebEnginePage();
};

class MyWebEngineView : public QWebEngineView
{
public:
    MyWebEngineView();
};

#endif // MYWEBENGINEVIEW_H
