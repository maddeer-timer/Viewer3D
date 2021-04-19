#!/usr/bin/env python
# coding=utf-8
import os
import sys
import re
import traceback
def TSSweeper(Filepath):
    """
    实用工具TSSweeper\n
    功能是把TS文件还原为为翻译前的状态\n
    因为Linguist没有还原功能\n
    """
    try:
        # 读取TS文件
        print("正在读取ts文件...",end="",flush=True)
        if len(Filepath)==0 or os.path.splitext(Filepath)[1].lower()!=".ts":
            raise ValueError("\"{}\"不是ts文件".format(Filepath))
        ThisContent=""
        with open(Filepath,"r",encoding="utf-8") as File:
            ThisContent=File.read()
        print("done",flush=True)
        # 处理文件内容
        print("正在查找并替换文件内容...",end="",flush=True)
        TranslatePattern=re.compile(r'<translation\s*(type="(?P<type>.*?)")?>'
                                    r'(?P<content>.*?)</translation>',flags=re.DOTALL)
        ReplaceString=r'<translation type="unfinished"></translation>'
        ReplaceStringLength=len(ReplaceString)
        MatchObjectCounter={}
        MatchObject=TranslatePattern.search(ThisContent)
        while MatchObject is not None:
            TranslationType=MatchObject.group("type")
            if TranslationType is None: TranslationType="NoneType"
            Addend=len(MatchObject.group("content"))!=0
            if TranslationType not in MatchObjectCounter:
                MatchObjectCounter[TranslationType]=[0,0]
            MatchObjectCounter[TranslationType][Addend]+=1
            ThisContent=ThisContent.replace(MatchObject.group(),ReplaceString,1)
            MatchObject=TranslatePattern.search(
                ThisContent,MatchObject.start()+ReplaceStringLength)
        print("done",flush=True)
        print("查找\"{}\"...".format(Filepath),flush=True)
        TranslationTotal=0
        for Type,(Default,Translation) in MatchObjectCounter.items():
            Total=Default+Translation
            print("\t发现类型\"{Type}\"的标签共{Total}个: 其中{Default}个为空, "
                  "{Translation}个已翻译".format(Type=Type,Total=
            Total,Default=Default,Translation=Translation),flush=True)
            Translation+=Total
        # 改名原文件写入新文件
        print("正在写入\"{}\"...".format(Filepath),end="",flush=True)
        SplitextList=os.path.splitext(Filepath)
        BackupFilepath=SplitextList[0]+"_Bak"+SplitextList[1]
        os.rename(Filepath,BackupFilepath)
        with open(Filepath,"w",encoding="utf-8") as File:
            File.write(ThisContent)
        print("done",flush=True)
    except:
        print()
        traceback.print_exc()
        if "BackupFilepath" in locals() and os.path.splitext(BackupFilepath)[0][:-4]==\
                os.path.splitext(Filepath)[0] and os.path.exists(BackupFilepath):
            print("正在恢复文件\"{}\"...".format(Filepath),end="",flush=True)
            os.remove(Filepath)
            os.rename(BackupFilepath,Filepath)
            print("done",flush=True)
        sys.exit()
if __name__=="__main__":
    try:
        Filepath=input("请输入目标文件路径(必须是ts文件): \n")
        TSSweeper(Filepath)
    except:
        traceback.print_exc()
        sys.exit()