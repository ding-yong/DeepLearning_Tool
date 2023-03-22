# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/5/20 16:25 
# ide： PyCharm
# coding=utf-8
import os
import os.path
import xml.dom.minidom

path=r'C:\Users\EP001\Desktop\Annotations'
files=os.listdir(path)

for xmlFile in files:
    if not os.path.isdir(xmlFile):

        dom=xml.dom.minidom.parse(os.path.join(path,xmlFile))
        root=dom.documentElement

        name=root.getElementsByTagName('name')
        #修改属性值
        print(name)
        for j in range(len(name)):
            name[j].firstChild.data=0
            print(name[j].firstChild.data)

        #保存修改到xml文件中
        with open(os.path.join(path,xmlFile),'w') as wn:
            dom.writexml(wn)
            print("修改完成！")