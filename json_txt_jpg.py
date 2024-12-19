import json
import os

# 加载 JSON 文件
json_file = 'D:/test3.json'  # 替换为你的 JSON 文件路径
txt_file = 'D:/test1.txt'  # 输出 TXT 文件路径

# 读取 JSON 文件
with open(json_file, 'r') as f:
    image_paths = json.load(f)

# 提取文件名并写入 TXT 文件
with open(txt_file, 'w') as f:
    for image_path in image_paths:
        # 从路径中提取文件名
        file_name = os.path.basename(image_path)
        f.write(file_name + '\n')

print(f"文件名已成功提取到 {txt_file}")
