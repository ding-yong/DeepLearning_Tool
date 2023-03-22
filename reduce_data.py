import numpy as np
import pandas as pd

for j in [1, 2, 3, 4, 6, 7, 8]:
    # 读取数据
    data_X = pd.read_csv(f"Glove_Pants/data_pants/0306Sensor{j}.csv", dtype=float)
    data_Y = pd.read_excel(f"Glove_Pants/data_pants/opti_0306_00{j}.xlsx", dtype=float)
    data_a = np.array(data_X)
    data_b = np.array(data_Y)

    # 计算数据A和数据B之间的帧数差异
    diff_frames = data_a.shape[0] - data_b.shape[0]

    # 创建空DataFrame
    merged_df_a = pd.DataFrame()
    merged_df_b = pd.DataFrame()

    # 将数据A中的帧数据按照数据B的帧数进行删减
    if diff_frames > 0:
        reduced_data_a = np.zeros((data_b.shape[0], data_a.shape[1]))
        for i in range(data_b.shape[0]):
            reduced_data_a[i, :] = data_a[i * (data_a.shape[0] // data_b.shape[0]), :]
        merged_df_a = pd.DataFrame(reduced_data_a)
        merged_df_b = pd.DataFrame(data_b)
    elif diff_frames < 0:
        reduced_data_b = np.zeros((data_a.shape[0], data_b.shape[1]))
        for i in range(data_a.shape[0]):
            reduced_data_b[i, :] = data_b[i * (data_b.shape[0] // data_a.shape[0]), :]
        merged_df_a = pd.DataFrame(data_a)
        merged_df_b = pd.DataFrame(reduced_data_b)
    else:
        merged_df_a = pd.DataFrame(data_a)
        merged_df_b = pd.DataFrame(data_b)

    # 现在，reduced_data_a和data_b的帧数相同,进行保存

    # 保存合并后的数据到csv文件
    merged_df_a.to_csv(f"Glove_Pants/data_pants_process/0306Sensor{j}.csv", index=False)
    # 保存合并后的数据到excel文件
    merged_df_b.to_excel(
        f"Glove_Pants/data_pants_process/opti_0306_{j}.xlsx", index=False
    )
