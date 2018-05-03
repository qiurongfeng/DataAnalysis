# -*- coding: utf-8 -*-
"""
Created on 2018/4/26 15:49
author: Rongfeng.Qiu
file:output_pic.py
"""
import numpy as np
import matplotlib.pyplot as plt
def output(content):
    for title,value in content.items() :
        # 设置字体样式
        plt.figure()
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = [u'SimHei']
        plt.title(title)
        labels = []
        fracs = []
        for k,v in value.items():
            if title!=k:
                labels.append(k.replace(title,""))
                fracs.append(v)
        plt.pie(x = fracs,labels=labels)
        save_path =( "pic/" + title.split(":")[0] +".png")
        print(save_path)
        plt.savefig(save_path)
        plt.close(0)
