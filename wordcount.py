# -*- coding: utf-8 -*-
"""
Created on 2018/4/20 10:27
author: Rongfeng.Qiu
file:wordcount.py
"""
import os

#单文件单关键词
def wordCount(str,filepath):
    # pathfile = r".\System.log.1"
    with open(filepath,"r") as f:
        file = f.read()
        warm_num = file.count(str)
        return warm_num
##单文件多关键词
def listCount(count_list,filepath,count_map):
    for line in count_list:
        num = wordCount(line,filepath)
        count_map[line] += num
    return count_map
#多文件多关键词
def fileListCount(start,end,count_list,filepath):
    count_map = {}
    for v in count_list:
        count_map[v] = 0
    for i in range(start,end + 1):
        path = filepath.replace('*',str(i))
        if(not os.path.exists(path)):
            continue
        print("统计文件" + path)
        try:
            listCount(count_list, path, count_map)
        except:
            print("统计文件出错")
            continue
    return count_map