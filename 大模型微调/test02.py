# 统计转换后的json数据的最大长度
import json
with open("data/train_data.json", "r", encoding="utf-8") as json_file:
    transformed_data = json.load(json_file)

max_length = 0

for data in transformed_data:
    output_length = data["output"]
    if max_length < output_length:
        max_length = output_length

print(max_length)