# -*- coding: utf-8 -*-
"""
Created on 2018/4/20 10:27
author: Rongfeng.Qiu
file:output_excel.py
"""
import xlwt
def output(content,workbook,sheetName,initList):
    if type(content) == list:
        booksheet = workbook.add_sheet(sheetName, cell_overwrite_ok=True)
        ##初始行
        for i in range(len(initList)):
            booksheet.write(0, i, initList[i ])

        for i, row in enumerate(content):
            for j, col in enumerate(row):
                booksheet.write(i + 1, j, col)
        return workbook
    elif type(content) == dict:
        booksheet = workbook.add_sheet(sheetName, cell_overwrite_ok=True)
        ##初始行
        for i in range( len(initList) ):
            booksheet.write(0, i, initList[i])

        i = 1
        for k,v in content.items():
            booksheet.write(i, 0, k)
            booksheet.write(i, 1, v)
            i += 1
        return workbook

def output_keyvalue(content,workbook,sheetName,initList):
    booksheet = workbook.add_sheet(sheetName, cell_overwrite_ok=True)
    ##初始行
    for i in range(len(initList)):
        booksheet.write(0, i, initList[i])

    i = 1
    for key,value in content.items():
        for k, v in value.items():
            booksheet.write(i, 0, k)
            booksheet.write(i, 1, v)
            i += 1
    return workbook