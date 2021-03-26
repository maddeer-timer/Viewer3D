#!/usr/bin/env python
# coding=utf-8
import os
import sys
import re
import subprocess
import traceback
def extractor(FilepathList,TargetPath):
    """
    实用工具Extractor\n
    用于将Python文件打包进一个C++文件并调用LUpdate转化成ts文件\n
    做出该文件的原因是因为我的PyQT5的PyLUpdate无法正常使用\n
    """
    print("正在复制并改写Python文件...",end="",flush=True)
    FileIOFlagTuple=(False,-1)
    for FileIndex,Filepath in enumerate(FilepathList):
        try:
            # 读取Python文件
            if len(Filepath)==0 or os.path.splitext(Filepath)[1].lower()!=".py":
                raise ValueError("\"{}\"不是Python文件".format(Filepath))
            ThisContent=""
            with open(Filepath,"r",encoding="utf-8") as File:
                ThisContent=File.read()
            # 处理文件内容
            TranslatePattern=re.compile(
                r'_translate\("(.*?)",\s*((r?(["\']{1,3}).*?\4\s*,\s*)*?r?(["\']{1,3}).*?\5\s*)\)',
                flags=re.DOTALL)
            MatchObject=TranslatePattern.search(ThisContent)
            while MatchObject is not None:
                ReplaceString=MatchObject.expand(r'\g<1>::tr(\g<2>)')
                ReplaceContent=MatchObject.group(2)
                VariableStringList=eval('['+ReplaceContent+']')
                for StringIndex,VariableString in enumerate(VariableStringList):
                    RealValue='"'+repr(VariableString)[1:-1].replace(r"\'",r"'")\
                        .replace(r"'",r"\'").replace(r'\"',r'"').replace(r'"',r'\"')+'"'
                    VariableStringList[StringIndex]=RealValue
                ReplaceString=ReplaceString.replace(ReplaceContent,",".join(VariableStringList))
                ThisContent=ThisContent.replace(MatchObject.group(),ReplaceString)
                MatchObject=TranslatePattern.search(
                    ThisContent,MatchObject.start()+len(ReplaceString))
            # 改名原文件写入新文件
            SplitextList=os.path.splitext(Filepath)
            BackupFilepath=SplitextList[0]+"_Bak"+SplitextList[1]
            os.rename(Filepath,BackupFilepath)
            with open(Filepath,"w",encoding="utf-8") as File:
                File.write(ThisContent)
        except:
            print()
            traceback.print_exc()
            if "BackupFilepath" in locals() and os.path.splitext(BackupFilepath)[0][:-4]==\
                    os.path.splitext(Filepath)[0] and os.path.exists(BackupFilepath):
                print("正在恢复文件\"{}\"...".format(Filepath),end="",flush=True)
                os.remove(Filepath)
                os.rename(BackupFilepath,Filepath)
                print("done",flush=True)
            FileIOFlagTuple=[True,FileIndex]
            break
    if FileIOFlagTuple[0]:
        for Filepath in FilepathList[:FileIOFlagTuple[1]]:
            SplitextList=os.path.splitext(Filepath)
            BackupFilepath=SplitextList[0]+"_Bak"+SplitextList[1]
            if os.path.exists(BackupFilepath):
                print("正在恢复文件\"{}\"...".format(Filepath),end="",flush=True)
                os.remove(Filepath)
                os.rename(BackupFilepath,Filepath)
                print("done",flush=True)
        sys.exit()
    print("done",flush=True)
    try:
        # 执行LUpdate并输出日志
        print("LUpdate执行日志: ")
        LUpdatePath="\"D:\\Visual Studio\\Microsoft Visual Studio\\Shared\\Python37_64\\Lib"\
                    "\\site-packages\\qt5_applications\\Qt\\bin\\lupdate.exe\""
        FilepathListString=" ".join(['"'+Filepath+'"' for Filepath in FilepathList])
        ShellResult=subprocess.Popen(r"{exec} {temp} -ts {ts}".format(
            exec=LUpdatePath,temp=FilepathListString,ts='"'+TargetPath+'"'),
            stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        stdout,stderr=ShellResult.communicate()
        print(stderr.decode("gbk"),end="")
        print(stdout.decode("gbk"),end="")
        # 恢复Python文件
        for Filepath in FilepathList:
            SplitextList=os.path.splitext(Filepath)
            BackupFilepath=SplitextList[0]+"_Bak"+SplitextList[1]
            if os.path.exists(BackupFilepath):
                print("正在恢复文件\"{}\"...".format(Filepath),end="",flush=True)
                os.remove(Filepath)
                os.rename(BackupFilepath,Filepath)
                print("done",flush=True)
    except:
        print()
        traceback.print_exc()
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
        if len(TargetPath)==0 or os.path.splitext(TargetPath)[1].lower()!=".ts":
            raise ValueError("目标文件不是ts文件")
        extractor(FilepathList,TargetPath)
    except:
        traceback.print_exc()
        sys.exit()
