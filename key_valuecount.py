# -*- coding: utf-8 -*-
"""
Created on 2018/4/24 13:40
author: Rongfeng.Qiu
file:key_valuecount.py
"""
import os
import operator

#单文件单关键词
def keyCount(keyList,filepath,count_map):
    # pathfile = r".\System.log.1"
    down = 1
    with open(filepath,"r") as f:
        while down:
            fileLine = f.readline()
            if fileLine == '':
                down = 0
            fileList = fileLine.split(",")
            for index,key in enumerate(keyList):
                for line in fileList:
                    if key in line:
                        count_map[key] += 1
                        count_map[line] = count_map[line] + 1 if (line in count_map) else  1
    return count_map
#多文件多关键词
def fileKeyCount(start,end,count_list,filepath):
    list_map = {}
    count_map = {}
    for v in count_list:
        count_map[v] = 0
    for i in range(start,end + 1):
        path = filepath.replace('*',str(i))
        if(not os.path.exists(path)):
            continue
        print("统计文件key-value" + path)
        try:
            keyCount(count_list, path, count_map)
        except:
            print("统计文件key-value出错")
            continue
    # sorted(count_map.keys())
    #将键值对进行归类格式为{   key1:{}, key2:{} }
    for key in count_list:
        tempDict = {}
        for k,v in count_map.items():
            if key in k:
                tempDict[k] = v
        sorted_x = sorted(tempDict.items(), key=(operator.itemgetter(0)))
        list_map[key] = dict(sorted_x)

    return list_map