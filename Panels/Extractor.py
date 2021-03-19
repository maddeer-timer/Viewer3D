#!/usr/bin/env python
# coding=utf-8
import os
import sys
import re
import subprocess
import traceback
def getRelativePath(Workpath,Filepath):
    """
    用来获取相对路径的工具
    返回从Workpath到Filepath的相对路径
    """
    
def extractor(FilepathList,TargetPath):
    """
    实用工具Extractor\n
    用于将Python文件打包进一个C++文件并调用LUpdate转化成ts文件\n
    做出该文件的原因是因为PyQT5的PyLUpdate无法正常使用\n
    """
    FilesContent=""
    for FileIndex,Filepath in enumerate(FilepathList):
        try:
            # 读取Python文件
            if os.path.splitext(Filepath)[1].lower()!=".py":
                raise ValueError("\"{}\" isn't a Python file".format(Filepath))
            with open(Filepath,"r",encoding="utf-8") as File:
                ThisContent=File.read()
                TrFuncList=re.findall(r'_translate\(\".*?\",\s*?\".*?\"\)',ThisContent)
                CppTrFuncList=[re.sub(r'"\s*\)','\a{}")'.format(str(FileIndex)),
                                      TrFunc.replace("\n","").replace("_translate","Object::tr"))
                               for TrFunc in TrFuncList]
                FilesContent+="\n".join(CppTrFuncList)
        except:
            traceback.print_exc()
            break
    try:
        # 合并入C++文件
        TemporaryFile=os.path.split(TargetPath)[0]+"_translate.bak"
        with open(TemporaryFile,"w",encoding="utf-8") as File:
            File.write(FilesContent)
        # 执行LUpdate并输出日志
        print("LUpdate执行日志: ")
        LUpdatePath="\"D:\\Visual Studio\\Microsoft Visual Studio\\Shared\\Python37_64\\Lib"\
                    "\\site-packages\\qt5_applications\\Qt\\bin\\lupdate.exe\""
        ShellResult=subprocess.Popen(r"{exec} {temp} -ts {ts}".format(
            exec=LUpdatePath,temp=TemporaryFile,ts=TargetPath),
            stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        stdout,stderr=ShellResult.communicate()
        print(stderr.decode("gbk"),end="")
        print(stdout.decode("gbk"),end="")
        # 删除临时C++文件
        os.remove(TemporaryFile)
        # 修改ts文件使之与源文件相对应
        with open(TargetPath,"r",encoding="utf-8") as File:
            TsFileContent=File.readlines()
        BeginIndex=-1
        FileIndex=-1
        SourceName=""
        CommentName=""
        ReLocation=re.compile(r'\s*<location filename="(.*?)" line="(\d*?)"/>')
        ReSource=re.compile(r'\s*<source>(.*?)</source>')
        ReComment=re.compile(r'\s*<comment>(.*?)<byte value="x7"/>(\d*?)</comment>')
        for XmlLineIndex,XmlLine in enumerate(TsFileContent):
            if re.match(r"\s*<message>",XmlLine) is not None:
                BeginIndex=XmlLineIndex
                continue
            if ReSource.match(XmlLine) is not None:
                SourceName=ReSource.findall(XmlLine)[0]
                continue
            if ReComment.match(XmlLine) is not None:
                CommentName,FileIndex=ReComment.findall(XmlLine)[0]
                FileIndex=int(FileIndex)
                continue
            if re.match(r"\s*</message>",XmlLine) is not None:
                # 获取该字符串原来所在的位置列表
                Filepath=FilepathList[FileIndex]
                LocationList=[]
                with open(Filepath,"r",encoding="utf-8") as File:
                    FileLineList=File.readlines()
                for FileLineIndex,FileLine in FileLineList:
                    if re.search(r'_translate\(\"{src}\",\s*?\"{cmt}\"\)'.format(
                            src=SourceName,cmt=CommentName),FileLine):
                        LocationList.append(FileLineIndex+1)
                # 对ts文件的内容进行修正
                LocationCounter=0
                for SubXmlLineIndex in range(BeginIndex+1,XmlLineIndex):
                    XmlLineContent=TsFileContent[SubXmlLineIndex]
                    if ReLocation.match(XmlLineContent) is not None:
                        TsFileContent[SubXmlLineIndex]=re.sub(
                            r'filename="(.*?)"',r'filename="{}"'.format(getRelativePath(
                                os.path.abspath(os.getcwd()),os.path.abspath(Filepath))),
                            XmlLineContent)
                        TsFileContent[SubXmlLineIndex]=re.sub(
                            r'line="(\d*?)"',r'line="{}"'.format(
                                LocationList[LocationCounter]),XmlLineContent)
                        LocationCounter+=1
                        continue
                    if ReComment.match(XmlLineContent) is not None:
                        TsFileContent[SubXmlLineIndex]=re.sub(
                            r'',r'',XmlLineContent)
                        continue
                continue
    except:
        traceback.print_exc()
        if "TemporaryFile" in locals() and os.path.exists(TemporaryFile):
            os.remove(TemporaryFile)
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
