# -*- coding: utf-8 -*-
# author： DingYong
# contact： dingyong10106071@gmail.com
# datetime： 2023/3/3 15:05
# ide： PyCharm

import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv1D, MaxPooling1D
from sklearn.model_selection import train_test_split

# 从文件中读取原始数据
datax = np.loadtxt('Y_all.txt')
datay = np.loadtxt('X_all.txt')
# 将数据按照12通道和21通道分为X和Y
X = datax[:, 0:12]
Y = datay[:, 0:21]

# 将数据划分为训练集和测试集

X_train_val, X_test, Y_train_val, Y_test = train_test_split(X, Y, test_size=0.4, random_state=42)
X_train, X_val, Y_train, Y_val = train_test_split(X_train_val, Y_train_val, test_size=0.4, random_state=42)
# 将数据标准化到0-1范围
X_train = 200*(X_train - np.min(X_train)) / (np.max(X_train) - np.min(X_train))
#Y_train = (Y_train - np.min(Y_train)) / (np.max(Y_train) - np.min(Y_train))
X_test = 200*(X_test - np.min(X_test)) / (np.max(X_test) - np.min(X_test))
#Y_test = (Y_test - np.min(Y_test)) / (np.max(Y_test) - np.min(Y_test))

# 将训练数据 X_train 转换为三维格式
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
# 将测试数据 X_test 转换为三维格式
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
# 将验证数据 X_val 转换为三维格式
X_val = X_val.reshape((X_val.shape[0], X_val.shape[1], 1))

# 输入数据包含12个通道
input_dim = 12
# 输出数据包含21个通道
output_dim = 21
# 定义模型
model = Sequential()
model.add(Conv1D(32, 3, activation='relu', input_shape=(12, 1)))
model.add(Conv1D(64, 3, activation='relu'))
model.add(MaxPooling1D(2))
model.add(Dropout(0.25))
model.add(Conv1D(128, 3, activation='relu'))
model.add(MaxPooling1D(2))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(21))

# 编译模型
model.compile(loss='mean_squared_error',
              optimizer='adam',
              metrics=['mae'])

# 训练模型
history = model.fit(X_train, Y_train,
                    batch_size=256,
                    epochs=500,
                    verbose=1,
                    validation_data=(X_val, Y_val))

model.save('model.h5')
# 使用模型进行预测
Y_pred = model.predict(X_test)
#想要展示的通道
i=6
y_test_channel = Y_test[0:500, i]
y_pred_channel = Y_pred[0:500, i]  # 提取预测值的第一个通道
j=0
n=0
for j in range(500):
    n = n+ abs(y_pred_channel[j]-y_test_channel[j])
n=n/500
print(n)
plt.plot(y_test_channel, label='true')
plt.plot(y_pred_channel, label='pred')
plt.legend()
plt.show()