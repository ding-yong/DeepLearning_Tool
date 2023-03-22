# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2023/3/5 19:48 
# ide： PyCharm
import torch
from torchsummary import summary
input_shape=(32,1,12)
model = torch.load(r'D:\Python\Project_daily\glove\12-19\model_Transformer.pt')
summary(model, input_size=(input_shape))
