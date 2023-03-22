import pandas as pd
from openpyxl import load_workbook

# 创建空DataFrame
merged_df = pd.DataFrame()

# 文件名列表
file_list = [
    "Glove_Pants/data_pants_process/opti_0306_1.xlsx",
    "Glove_Pants/data_pants_process/opti_0306_2.xlsx",
    "Glove_Pants/data_pants_process/opti_0306_3.xlsx",
    "Glove_Pants/data_pants_process/opti_0306_4.xlsx",
    "Glove_Pants/data_pants_process/opti_0306_6.xlsx",
    "Glove_Pants/data_pants_process/opti_0306_7.xlsx",
    "Glove_Pants/data_pants_process/opti_0306_8.xlsx",
]

# 读取文件
for file_name in file_list:
    # 读取数据
    wb = load_workbook(filename=file_name)
    sheet = wb.active
    rows = sheet.rows
    # 将数据添加到合并DataFrame中
    values_list = []
    for i, row in enumerate(rows):
        if i == 0:  # 跳过第1行
            continue
        values = [cell.value for cell in row]
        values_list.append(values)
    df = pd.DataFrame(values_list)
    merged_df = pd.concat([merged_df, df])


# 保存合并后的数据到csv文件
merged_df.to_excel("Glove_Pants/data_pants_process/merged_opti_0306.xlsx", index=False)
