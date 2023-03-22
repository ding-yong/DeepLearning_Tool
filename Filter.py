import pandas as pd
import numpy as np
from scipy.signal import butter, filtfilt, medfilt
from pykalman import KalmanFilter
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d
from scipy.interpolate import interp1d
from scipy.signal import resample
from scipy.signal import medfilt2d

# 读取csv文件并将数据转化为numpy数组
data = pd.read_csv("Glove_Pants/outputs/outputs_rnn.csv").values

"""
# 对每一列数据分别进行平滑滤波处理
kernel = 5
smooth_kernel = np.ones(kernel) / kernel
for i in range(data.shape[1]):
    data[:, i] = np.convolve(data[:, i], smooth_kernel, mode="same")

# 定义中值滤波器参数
window_size = 3
# 对每一列数据分别进行中值滤波处理
for i in range(data.shape[1]):
    data[:, i] = medfilt(data[:, i], window_size)

# 数据
n_samples = data.shape
n_channels = 4

# 定义卡尔曼滤波器
transition_matrix = np.eye(n_channels)
observation_matrix = np.eye(n_channels)
initial_state_mean = data[0]
initial_state_covariance = np.eye(n_channels)
kf = KalmanFilter(
    transition_matrices=transition_matrix,
    observation_matrices=observation_matrix,
    initial_state_mean=initial_state_mean,
    initial_state_covariance=initial_state_covariance,
)

# 执行卡尔曼滤波
data, _ = kf.filter(data)

# 对每一列进行亚采样和插值
num_resampled = int(data.shape[0] * 0.3)  # 输出点数为输入点数的50%
data_resampled = np.zeros((num_resampled, data.shape[1]))
for i in range(data.shape[1]):
    data_resampled[:, i] = resample(data[:, i], num_resampled)

# 插值
f_interp = interp1d(
    np.linspace(0, data.shape[0], num_resampled), data_resampled, kind="linear", axis=0
)
data = f_interp(np.linspace(0, data.shape[0], data.shape[0]))
"""
# 定义中值滤波器参数
window_size = (3, 1)
data = medfilt2d(data, window_size)

kernel_size = 3
smooth_kernel = np.ones((kernel_size, 1)) / kernel_size

# 对每一列数据分别进行平滑处理
for i in range(data.shape[1]):
    data[:, i] = np.convolve(data[:, i], smooth_kernel[:, 0], mode="full")
"""
# 高斯滤波
sigma = 1  # 标准差
angles_filtered = np.zeros_like(data)
for i in range(data.shape[1]):
    angles_filtered[:, i] = gaussian_filter1d(data[:, i], sigma=sigma)

# 创建插值函数
x = np.arange(data.shape[0])  # x坐标
f = interp1d(x, data, kind="linear", axis=0)

# 生成插值后的数据
x_new = np.linspace(0, x[-1], 100000)  # 新的x坐标
data = f(x_new)

def peak_preserving_filter(x, alpha=0.2, kernel_size=1):
    # 使用中值滤波器进行平滑
    y = medfilt(x, kernel_size=kernel_size)
    # 对中值滤波器的输出和原始信号进行加权平均
    z = (1 - alpha) * x + alpha * y
    return z


data = peak_preserving_filter(data, alpha=0.5, kernel_size=1)

# 对每一列数据分别进行平滑滤波处理
kernel = 5
smooth_kernel = np.ones(kernel) / kernel
for i in range(data.shape[1]):
    data[:, i] = np.convolve(data[:, i], smooth_kernel, mode="same")

# 对每一列数据分别进行平滑滤波处理
kernel = 5
smooth_kernel = np.ones(kernel) / kernel
for i in range(data.shape[1]):
    data[:, i] = np.convolve(data[:, i], smooth_kernel, mode="same")
"""

# 将处理后的数据保存到新的csv文件中
df = pd.DataFrame(data)
df.to_csv("Glove_Pants/outputs/outputs_rnn_filtered.csv", index=False, header=None)

# 读取csv文件
data1 = pd.read_csv(
    "D:\Python_Shanghai\\body_demo\HandDemo_Data\StreamingAssets\\0129_Bone_zyt006_process.csv"
)

# 删除第二行及之后的所有行
data1 = data1.drop(data1.index[0:])

# 将生成的数据添加到DataFrame中
print(data.shape)
data1["1"] = [row[0] for row in data]
data1["2"] = 0
data1["3"] = 0
data1["4"] = 0
data1["5"] = 0
data1["6"] = [row[1] for row in data]
data1["7"] = [row[2] for row in data]
data1["8"] = [row[3] for row in data]

# 将修改后的DataFrame写回csv文件
data1.to_csv(
    "D:\Python_Shanghai\\body_demo\HandDemo_Data\StreamingAssets\\0129_Bone_zyt006_process.csv",
    index=False,
)

plt.plot(data[:, 0], label="0")
plt.plot(data[:, 2], label="1")
plt.legend()
plt.show()
