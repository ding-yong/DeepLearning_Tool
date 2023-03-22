# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2022/5/22 18:40 
# ide： PyCharm
import os
from PIL import Image

dirname_read="C:\\Users\\EP001\\Desktop\\VOC2007\\JPEGImages\\"
dirname_write="C:\\Users\\EP001\\Desktop\\1\\"
names=os.listdir(dirname_read)
count=0
for name in names:
    img=Image.open(dirname_read+name)
    img = img.convert("RGB")
    name=name.split(".")
    if name[-1] == "png":
        name[-1] = "jpg"
        name = str.join(".", name)
        to_save_path = dirname_write + name
        img.save(to_save_path)
        count+=1
        print(to_save_path, "------conut：",count)
    else:
        continue
