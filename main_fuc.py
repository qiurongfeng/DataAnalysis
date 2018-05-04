# -*- coding: utf-8 -*-
"""
Created on 2018/4/20 10:27
author: Rongfeng.Qiu
file:main_fuc.py
"""
from DataAnalysis import key_valuecount,during_timecount,upEndTime,output_pic,output_excel,wordcount
import os
import xlwt

#输入文件格式，文件放在当前目录下
filepath = r"data\System.log.*"
#文件初始编号
start = 0
#文件结束编号
end = 25
#填入需要统计的出现词列表或者单个字符串
count_list1 = [
    "WARNING",
    "saveImage",
    "Image transfer done. FrameNumber:0 ImageState:Blank",
    "Start shot",
    "End Shot",
    "ImagingEngineSvtImpl::getImage() fail"
]
count_list2 = [
    "modeInt is:",
    "Mode is:",
    "pulseFlagInt is:",
    "ppsInt is:",
    "lowDoseFlagInt is:",
    "magModeInt is:",
    "kv is:",
    "ma is:",
    "maFloat to IE is"
]
count_list3 = [
    "Image transfer done. FrameNumber:0 ImageState:Blank"
]
#起始字符串
str1 = "************************************************************"
#结束字符串
str2 = "System exit in logger"
##
str3 = "Start shot"
##
str4 = "End Shot"

#############################################################
workbook = xlwt.Workbook(encoding='utf-8')
#############################################################

########统计时间差########
#输入工作表名称
sheetname1 = "sheet 1"
#输入初始行
initList = ["开机时间","关机时间","时间差（单位秒）"]
listTime = upEndTime.count_time(str1,str2,start,end,filepath)
workbook = output_excel.output(listTime,workbook,sheetname1,initList)
#########################


########统计shot时间差########
#输入工作表名称
sheetname2 = "sheet 2"
#输入初始行
initList = ["start shot时间","end shot时间","时间差（单位秒）"]
shotList = upEndTime.count_time(str3,str4,start,end,filepath)
workbook = output_excel.output(shotList,workbook,sheetname2,initList)
#########################


########统计出现次数########
#输入工作表名称
sheetname3 = "sheet 3"
#输入初始行
initList = ["出现关键字","出现次数"]
count_map1 = wordcount.fileListCount(start,end,count_list1,filepath)
workbook = output_excel.output(count_map1,workbook,sheetname3,initList)
#########################

########统计出现次数########
#输入工作表名称
sheetname4 = "sheet 4"
#输入初始行
initList = ["出现关键字","出现次数"]
count_map2 = key_valuecount.fileKeyCount(start,end,count_list2,filepath)
output_pic.output(count_map2)
workbook = output_excel.output_keyvalue(count_map2,workbook,sheetname4,initList)

#########################

########统计出现次数########
#输入工作表名称
sheetname5 = "sheet 5"
#输入初始行
initList = ["出现关键字","出现次数"]
count_map3 = during_timecount.count_duringtime(str3,str4,start,end,count_list3,filepath)
workbook = output_excel.output(count_map3,workbook,sheetname5,initList)
#########################



# 输入Excel文件名
excelName = 'res_15.xls'

try:
    workbook.save("output/" + excelName)
    print("操作成功,文件" + excelName + "已生成")
except OSError as reason:
    print("保存失败：" + str(reason))




