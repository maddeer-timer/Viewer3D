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
        WorkDirectory=(os.pardir+os.sep)*len(re.split(r'[\\|/]',WorkDirectory[Pointer:]))
        return WorkDirectory+Filepath[Pointer:]
    else: return Filepath[Pointer+2:]