#!/usr/bin/env python
# coding=utf-8
import sys
import os
import traceback
try:
    main_dir=os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0,main_dir)
    os.chdir(main_dir)
except:
    traceback.print_exc()
def main():
    import Control
    Control.main()
if __name__=="__main__":
    main()