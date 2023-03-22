import torch
import torchvision.models as models
import onnx

# 加载训练模型
model = torch.load('model_Transformer.pt')

# 创建虚拟输入数据
dummy_input = torch.randn(1,1,1,12)

# 将模型转换为onnx格式
onnx_model = torch.onnx.export(model, dummy_input, "model_Transformer.onnx", opset_version=10)