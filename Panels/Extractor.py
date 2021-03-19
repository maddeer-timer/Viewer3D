#!/usr/bin/env python
# coding=utf-8
import os
import sys
import re
import subprocess
import traceback
from Panels.ExtractorBaseCpp import CppBaseCode
def extractor(FilepathList,TargetPath):
    """
    实用工具Extractor\n
    用于将Python文件打包进一个C++文件并调用LUpdate转化成ts文件\n
    做出该文件的原因是因为PyQT5的PyLUpdate无法正常使用\n
    """
    for Filepath in FilepathList:
        try:
            # 读取Python文件
            if os.path.splitext(Filepath)[1]!=".py":
                raise ValueError("\"{}\" isn't a Python file".format(Filepath))
            FilesContent=""
            with open(Filepath,"r",encoding="utf-8") as File:
                ThisContent=File.read()
                TrFuncList=re.findall(r'_translate\(\".*?\",\s*?\".*?\"\)',ThisContent)
                FilesContent+="\n".join([TrFunc.replace("\n","").replace("_translate","\tObject::tr")
                                         for TrFunc in TrFuncList])
            # 合并入C++文件
            TemporaryFile=os.path.splitext(TargetPath)[0]+".cpp"
            with open(TemporaryFile,"w",encoding="utf-8") as File:
                File.write(CppBaseCode["CppBaseHead"]+FilesContent+CppBaseCode["CppBaseEnd"])
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
        except:
            traceback.print_exc()
            if "TemporaryFile" in locals() and os.path.exists(TemporaryFile):
                os.remove(TemporaryFile)
            break
if __name__=="__main__":
    try:
        print("请输入Python文件路径列表(使用\"Exit\"表示列表的结束): ")
        FilepathList=[]
        while True:
            Filepath=input()
            if Filepath=="Exit": break
            FilepathList.append(Filepath)
        if len(FilepathList)==0:
            raise ValueError("The file list is empty")
        TargetPath=input("请输入目标文件路径(必须是ts文件): \n")
        if os.path.splitext(TargetPath)[1]!=".ts":
            raise ValueError("The target file isn't a ts file")
        extractor(FilepathList, TargetPath)
    except:
        traceback.print_exc()
        sys.exit()
