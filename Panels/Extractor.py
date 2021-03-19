#!/usr/bin/env python
# coding=utf-8
import os
import sys
import re
import subprocess
import traceback
EscapeCharacterList={'\\': r'\\', '.': r'\.', '^': r'\^', '$': r'\$', '?': r'\?',
                     '+' : r'\+', '*': r'\*', '{': r'\{', '}': r'\}', '(': r'\(',
                     ')' : r'\)', '[': r'\[', ']': r'\]', '|': r'\|'}
def escapeString(RawString):
    """
    用来将原字符串转义为不会引起歧义的字符串
    返回这样的字符串
    """
    for RawCharacter,EscapeCharacter in EscapeCharacterList.items():
        RawString=RawString.replace(RawCharacter,EscapeCharacter)
    return RawString
def getRelativePath(WorkDirectory,Filepath):
    """
    用来获取相对路径的工具
    返回从WorkDirectory到Filepath的相对路径
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
        WorkDirectory=('..'+os.sep)*len(re.split(r'[\\|/]',WorkDirectory[Pointer:]))
        return WorkDirectory+Filepath[Pointer:]
    else: return Filepath[Pointer+2:]
def extractor(FilepathList,TargetPath):
    """
    实用工具Extractor\n
    用于将Python文件打包进一个C++文件并调用LUpdate转化成ts文件\n
    做出该文件的原因是因为PyQT5的PyLUpdate无法正常使用\n
    """
    print("正在读取Python文件...",end="",flush=True)
    FilesContent=""
    for FileIndex,Filepath in enumerate(FilepathList):
        try:
            # 读取Python文件
            if os.path.splitext(Filepath)[1].lower()!=".py":
                raise ValueError("\"{}\" isn't a Python file".format(Filepath))
            with open(Filepath,"r",encoding="utf-8") as File:
                ThisContent=File.read()
                TrFuncList=re.findall(r'_translate\(".*?",\s*?".*?"\)',ThisContent)
                CppTrFuncList=[re.sub(r'"\s*\)','\a{}")'.format(str(FileIndex)),
                                      TrFunc.replace("\n","").replace("_translate","Object::tr"))
                               for TrFunc in TrFuncList]
                FilesContent+="\n".join(CppTrFuncList)
        except:
            traceback.print_exc()
            break
    print("done",flush=True)
    try:
        # 合并入C++文件
        print("正在写入临时文件\"_translate.bak\"...",end="",flush=True)
        TemporaryFile=os.path.split(TargetPath)[0]+"_translate.bak"
        with open(TemporaryFile,"w",encoding="utf-8") as File:
            File.write(FilesContent)
        print("done",flush=True)
        # 执行LUpdate并输出日志
        print("LUpdate执行日志: ")
        LUpdatePath="\"D:\\Visual Studio\\Microsoft Visual Studio\\Shared\\Python37_64\\Lib"\
                    "\\site-packages\\qt5_applications\\Qt\\bin\\lupdate.exe\""
        ShellResult=subprocess.Popen(r"{exec} {temp} -ts {ts}".format(
            exec=LUpdatePath,temp='\"'+TemporaryFile+'\"',ts='\"'+TargetPath+'\"'),
            stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        stdout,stderr=ShellResult.communicate()
        print(stderr.decode("gbk"),end="")
        print(stdout.decode("gbk"),end="")
        # 删除临时C++文件
        print("正在删除临时文件\"_translate.bak\"...",end="",flush=True)
        os.remove(TemporaryFile)
        print("done",flush=True)
        # 修改ts文件使之与源文件相对应
        print("正在读取ts文件\"{}\"...".format(TargetPath),end="",flush=True)
        with open(TargetPath,"r",encoding="utf-8") as File:
            TsFileContent=File.readlines()
        print("done",flush=True)
        BeginIndex=-1
        FileIndex=-1
        SourceName=""
        CommentName=""
        ReLocation=re.compile(r'\s*<location filename="(.*?)" line="(\d*?)"/>')
        ReSource=re.compile(r'\s*<source>(.*?)</source>')
        ReComment=re.compile(r'\s*<comment>(.*?)<byte value="x7"/>(\d*?)</comment>')
        print("正在处理得到的XML文档...",end="",flush=True)
        for XmlLineIndex,XmlLine in enumerate(TsFileContent):
            if re.match(r"\s*<message>",XmlLine) is not None:
                BeginIndex=XmlLineIndex
                continue
            if ReSource.match(XmlLine) is not None:
                SourceName=ReSource.findall(XmlLine)[0]
                continue
            if ReComment.match(XmlLine) is not None:
                CommentName,FileIndex=ReComment.findall(XmlLine)[0]
                CommentName=CommentName.replace("&amp;","&").replace("&lt;","<")
                FileIndex=int(FileIndex)
                continue
            if re.match(r"\s*</message>",XmlLine) is not None:
                # 获取该字符串原来所在的位置列表
                Filepath=FilepathList[FileIndex]
                LocationList=[]
                TrFuncPattern=r'_translate\("{src}",\s*?"{cmt}"\)'.format(
                    src=escapeString(SourceName),cmt=escapeString(CommentName))
                with open(Filepath,"r",encoding="utf-8") as File:
                    FileLineList=File.readlines()
                for FileLineIndex,FileLine in enumerate(FileLineList):
                    if re.search(TrFuncPattern,FileLine):
                        LocationList.append(FileLineIndex+1)
                # 对ts文件的内容进行修正
                LocationCounter=0
                RealFileName=r'filename="{}"'.format(
                    getRelativePath(os.path.abspath(os.getcwd()),os.path.abspath(Filepath)))
                for SubXmlLineIndex in range(BeginIndex+1,XmlLineIndex):
                    XmlLineContent=TsFileContent[SubXmlLineIndex]
                    if ReLocation.match(XmlLineContent) is not None:
                        TsFileContent[SubXmlLineIndex]=re.sub(
                            r'filename="(.*?)"',RealFileName,XmlLineContent)
                        TsFileContent[SubXmlLineIndex]=re.sub(
                            r'line="(\d*?)"',r'line="{}"'.format(
                                LocationList[LocationCounter]),TsFileContent[SubXmlLineIndex])
                        LocationCounter+=1
                        continue
                    if ReComment.match(XmlLineContent) is not None:
                        TsFileContent[SubXmlLineIndex]=re.sub(
                            r'<byte value="x7"/>(\d*?)</comment>',r'</comment>',XmlLineContent)
                        continue
                continue
        print("done",flush=True)
        print("正在写入ts文件\"{}\"...".format(TargetPath),end="",flush=True)
        with open(TargetPath,"w",encoding="utf-8") as File:
            File.write("".join(TsFileContent))
        print("done",flush=True)
    except:
        traceback.print_exc()
        print("正在删除临时文件\"_translate.bak\"...",end="",flush=True)
        if "TemporaryFile" in locals() and os.path.exists(TemporaryFile):
            os.remove(TemporaryFile)
        print("done",flush=True)
        sys.exit()
if __name__=="__main__":
    try:
        print("请输入Python文件路径列表(使用\"Exit\"表示列表的结束): ")
        FilepathList=[]
        while True:
            Filepath=input()
            if Filepath.lower()=="exit": break
            FilepathList.append(Filepath)
        if len(FilepathList)==0:
            raise ValueError("The file list is empty")
        TargetPath=input("请输入目标文件路径(必须是ts文件): \n")
        if os.path.splitext(TargetPath)[1].lower()!=".ts":
            raise ValueError("The target file isn't a ts file")
        extractor(FilepathList, TargetPath)
    except:
        traceback.print_exc()
        sys.exit()
