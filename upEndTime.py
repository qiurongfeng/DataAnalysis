# -*- coding: utf-8 -*-
"""
Created on 2018/4/20 10:27
author: Rongfeng.Qiu
file:upEndTime.py
"""
import os
import datetime
def single_time(str1,str2,filepath,listTime):
    listTemp = []
    down = 1
    with open(filepath, "r") as f:
        while down:
            fileLine = f.readline()
            if fileLine == '':
                down = 0
            fileLine = fileLine.strip().split(",")
            if(str1 in fileLine):
                time  = fileLine[1] + " " + fileLine[2]
                if  listTemp:
                    listTemp.pop()
                    listTemp.append(time)
                else:
                    listTemp.append(time)
            if(str2 in fileLine):
                if(listTemp == []):
                    continue
                else:

                    one_list = []
                    endTime = fileLine[1] + " " + fileLine[2]
                    startTime = listTemp.pop()
                    un_endTime =  datetime.datetime.strptime(endTime,'%Y-%m-%d %H:%M:%S.%f').timestamp()
                    un_startTime = datetime.datetime.strptime(startTime,'%Y-%m-%d %H:%M:%S.%f').timestamp()
                    one_list.append(startTime)
                    one_list.append(endTime)
                    one_list.append(float(un_endTime) - float(un_startTime))
                    listTime.append(one_list)
    return listTime

def count_time(str1,str2,start,end,filepath):
    listTime = []
    for i in range(start,end + 1):
        path = filepath.replace('*',str(i))
        if(not os.path.exists(path)):
            continue
        print("计算文件" + path)
        try:
            single_time(str1,str2,path,listTime)
        except(OSError , EOFError) as res:
            print("计算文件出错" +res)
            continue
    return listTime
