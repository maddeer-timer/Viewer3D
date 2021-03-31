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
        if len(Filepath)==0 or os.path.splitext(Filepath)[1].lower()!=".ts":
            raise ValueError("\"{}\"不是ts文件".format(Filepath))
        ThisContent=""
        with open(Filepath,"r",encoding="utf-8") as File:
            ThisContent=File.read()
        # 处理文件内容
        TranslatePattern=re.compile(r'<translation>.*?</translation>',flags=re.DOTALL)
        ReplaceString=r'<translation type="unfinished"></translation>'
        ReplaceStringLength=len(ReplaceString)
        MatchObject=TranslatePattern.search(ThisContent)
        while MatchObject is not None:
            ThisContent=ThisContent.replace(MatchObject.group(),ReplaceString)
            MatchObject=TranslatePattern.search(
                ThisContent,MatchObject.start()+ReplaceStringLength)
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
        sys.exit()
if __name__=="__main__":
    try:
        Filepath=input("请输入目标文件路径(必须是ts文件): \n")
        TSSweeper(Filepath)
    except:
        traceback.print_exc()
        sys.exit()