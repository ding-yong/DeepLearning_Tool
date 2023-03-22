# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/3/30 15:36 
# ide： PyCharm
import os
path_last = 'C:\\Users\\EP001\\Documents\\WeChat Files\\wxid_3op8mf9jgvx121\\FileStorage\\File\\2022-05\\数据（png形式的金标准）\\data_zm\\'
for n in range(1,23):
    path=path_last +str(n)+'\\'
    print(path)
    for file in os.listdir(path):
        print(file, 'ok')
        if os.path.isfile(os.path.join(path,file))==True:
            newname = str(n) + file
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            print(file,'ok')