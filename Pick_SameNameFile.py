# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/4/4 21:44 
# ide： PyCharm
# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/3/31 16:23
# ide： PyCharm
import os
import random
import shutil

def moveFile(txt_Dir, img_Dir):
        img_pathDir = os.listdir(txt_Dir)                    # 提取txt的原始路径
        filenumber = len(img_pathDir)
        sample1 = random.sample(img_pathDir, filenumber)      # 选取同数量的txt
        print(sample1)
        for i in range(0, len(sample1)):
            sample1[i] = sample1[i][:-4]                           # 去掉txt的拓展名，移动标注时需要这个列表
        for name in sample1:
            src_mask_name1 = img_Dir + name
            dst_mask_name1 = img_2_Dir + name
            shutil.move(src_mask_name1 + '.png', dst_mask_name1 + '.png')   # 加上标注文件的拓展名，移动标注文件
        return

if __name__ == '__main__':
    # 从img移动到img2
    txt_Dir = 'C:\\Users\\EP001\\Desktop\\1\\'
    img_Dir = 'C:\\Users\\EP001\\Desktop\\data_zm\\'
    img_2_Dir= 'C:\\Users\\EP001\\Desktop\\data\\'
    moveFile(txt_Dir, img_Dir)

