# coding=utf-8
import os
import re
# 替换字符字典
EscapeCharacterList={'\\': r'\\', '.': r'\.', '^': r'\^', '$': r'\$', '?': r'\?',
                     '+' : r'\+', '*': r'\*', '{': r'\{', '}': r'\}', '(': r'\(',
                     ')' : r'\)', '[': r'\[', ']': r'\]', '|': r'\|'}
def escapeString(RawString):
    """
    用来将原字符串转义为不会引起歧义的字符串\n
    返回这样的字符串\n
    """
    for RawCharacter,EscapeCharacter in EscapeCharacterList.items():
        RawString=RawString.replace(RawCharacter,EscapeCharacter)
    return RawString
def getRelativePath(WorkDirectory,Filepath):
    """
    用来获取相对路径的工具\n
    返回从WorkDirectory到Filepath的相对路径\n
    """
    # 获取WorkDirectory和Filepath的重复部分
    WorkDirectory=os.path.abspath(WorkDirectory)
    Filepath=os.path.abspath(Filepath)
    MinLength=min(len(WorkDirectory),len(Filepath))
    Pointer=-1
    for Pointer in range(MinLength):
        if WorkDirectory[Pointer]!=Filepath[Pointer]: break
    if Pointer!=MinLength-1:
        for Pointer in range(Pointer,-1,-1):
            if WorkDirectory[Pointer]=='\\' or WorkDirectory[Pointer]=='/':
                break
    # 切除WorkDirectory的重复部分并将剩余部分转化为逆向路径
    if WorkDirectory[Pointer]=='\\' or WorkDirectory[Pointer]=='/':
        Pointer+=1
        WorkDirectory=(os.pardir+os.sep)*len(re.split(r'[\\/]',WorkDirectory[Pointer:]))
        return WorkDirectory+Filepath[Pointer:]
    else: return Filepath[Pointer+2:]
def getTitleHtml(PageTitle,TitleFont="monospace"):
    """
    将标题变成HTML标签的形式\n
    这样才可以改变字体\n
    """
    return '<font face="'+TitleFont+'">'+PageTitle+'</font>'
def getTextHtmlWithColor(RawText,TextColor="Black",Underline=False):
    """
    将文本变成HTML标签的形式\n
    用于改变文本颜色并可添加下滑线\n
    """
    if not Underline: return '<font color="'+TextColor+'">'+RawText+'</font>'
    else: return '<u><font color="'+TextColor+'">'+RawText+'</font></u>'