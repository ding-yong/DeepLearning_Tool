import pandas as pd

# 创建空DataFrame
merged_df = pd.DataFrame()

# 文件名列表
file_list = [
    "Glove_Pants/data_pants_process/0306Sensor1.csv",
    "Glove_Pants/data_pants_process/0306Sensor2.csv",
    "Glove_Pants/data_pants_process/0306Sensor3.csv",
    "Glove_Pants/data_pants_process/0306Sensor4.csv",
    "Glove_Pants/data_pants_process/0306Sensor6.csv",
    "Glove_Pants/data_pants_process/0306Sensor7.csv",
    "Glove_Pants/data_pants_process/0306Sensor8.csv",
]

# 读取文件
for file_name in file_list:
    # 读取数据，跳过前1行
    df = pd.read_csv(file_name, header=None, skiprows=1, encoding="utf-8")
    # 将数据添加到合并DataFrame中
    merged_df = pd.concat([merged_df, df])

# 保存合并后的数据到csv文件
merged_df.to_csv("Glove_Pants/data_pants_process/merged_0306Sensor.csv", index=False)
