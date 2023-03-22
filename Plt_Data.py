# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/4/12 19:20 
# ide： PyCharm
import matplotlib.pyplot as plt
import numpy as np

values = open('C:\\Users\\EP001\\Desktop\\loss1.txt','r',encoding='utf8')
squares=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
plt.plot(values, squares, linewidth=4)
plt.title("Square Number", fontsize=20)
plt.xlabel("Value", fontsize=24)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both',
                labelsize=10)
plt.axis([0, 6, 0, 30])
plt.show()
