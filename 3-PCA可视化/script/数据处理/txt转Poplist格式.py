import pandas as pd

# 配置输入和输出文件路径，方便修改
input_file = '/mnt/c/Users/Administrator/Desktop/1.txt'
output_file = '/mnt/c/Users/Administrator/Desktop/poplist.txt'

# 读取TXT文件，假设是制表符分隔（如为空格分隔，可改为 sep='\s+'）
df = pd.read_csv(input_file, sep='\t', header=None, dtype=str)

# 获取唯一的分组
groups = df[1].unique()

# 生成输出文件
with open(output_file, 'w', encoding='utf-8') as f:
    for group in groups:
        f.write(f"===={group}====\n")
        members = df[df[1] == group][0].tolist()  # 获取该分组的所有成员
        f.writelines([member + '\n' for member in members])  # 确保每个成员换行

print("输出文件已生成。")
