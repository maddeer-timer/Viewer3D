#ifndef MYSCISCINTILLA_H
#define MYSCISCINTILLA_H

#include "Qsci/qscilexermarkdown.h"
#include "Qsci/qsciscintilla.h"

class MyLexerMarkdown : public QsciLexerMarkdown
{
public:
    MyLexerMarkdown();
};

class MysciScintilla : public QsciScintilla
{
public:
    MysciScintilla();
};

#endif // MYSCISCINTILLA_H
