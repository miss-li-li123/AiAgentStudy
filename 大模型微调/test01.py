import pandas as pd
import json

# 加载Excel文件
file_path = "data/test.xlsx"
df = pd.read_excel(file_path)

# 创建一个列表来保存转换后的数据
transformed_data = []

# 遍历DataFream的每一行
for index, row in df.iterrows():
    # 为每一行创建一个字典
    data_dict = {
        "instruction": row["问"],
        "input": "",
        "output": row["答"]
    }
    # 将字典添加到列表中
    transformed_data.append(data_dict)

# 将列表转换成JSON字符串
json_data = json.dumps(transformed_data, ensure_ascii=False,indent=4)


# 将JSON数据保存在文件中
json_file_path = "data/train_data.json"
with open(json_file_path,"w",encoding="utf-8") as json_file:
    json_file.write(json_data)
