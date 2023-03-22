# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/4/12 18:34 
# ide： PyCharm

# -*- coding:utf-8 -*-

import sys
import matplotlib.pyplot as plt
file_path="C:\\Users\\EP001\\Desktop\\loss.txt"
file=open("C:\\Users\\EP001\\Desktop\\loss1.txt", "w")
with open('C:\\Users\\EP001\\Desktop\\loss.txt','r',encoding='utf8') as fin:

  for line in fin.readlines():
    #sample_ = line.split('loss (batch)=')
    #print(sample_)
    n = line.find('loss (batch)=')
    print(n)
    if line[n + 13:n + 18] != 'oint ':
        file.write(line[n+13:n+18])
        file.write('\n')
