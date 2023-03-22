# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/4/12 21:06 
# ide： PyCharm
#coding=utf-8
'cv2'
import cv2
import os
import glob

path = 'E:\\data\\mask\\train\\*.png'
for i in glob.glob(path):
    im1 = cv2.imread(i)
    im2 = cv2.resize(im1, (572, 572))
    cv2.imwrite(os.path.join('E:\\data\\mask\\train\\mask', os.path.basename(i)), im2)