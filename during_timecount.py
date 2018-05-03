# -*- coding: utf-8 -*-
"""
Created on 2018/4/24 16:36
author: Rongfeng.Qiu
file:during_timecount.py
"""
import os
import datetime
def duringtime(str1,str2,countlist,filepath,count_map):
    listTemp = []
    down = 1
    flag = 0
    with open(filepath, "r") as f:
        while down:
            fileLine = f.readline()
            if fileLine == '':
                down = 0
            # fileLine = fileLine.strip().split(",")
            for str in countlist:
                if (str in fileLine) and flag:
                    count_map[str] += 1
            if(str1 in fileLine):
                    flag = 1
            if(str2 in fileLine):
                if(flag == 0):
                    continue
                else:
                    flag = 0
    return count_map

def count_duringtime(str1,str2,start,end,count_list,filepath):
    count_map = {}
    for v in count_list:
        count_map[v] = 0
    for i in range(start,end + 1):
        path = filepath.replace('*',str(i))
        if(not os.path.exists(path)):
            continue
        print("计算文件" + path)
        try:
            duringtime(str1,str2,count_list,path,count_map)
        except(OSError , EOFError) as res:
            print("计算文件出错" +res)
            continue
    return count_map
