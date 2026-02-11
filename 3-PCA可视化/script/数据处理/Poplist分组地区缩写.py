# Adjust the function to only abbreviate the part of the group name before the first underscore

def abbreviate_regions_in_file_v3(input_file_path, output_file_path):
    """
    此函数读取一个文件，将其中的地区名（第一个下划线之前的部分）缩写，并保存到另一个文件中。

    :param input_file_path: 输入文件的路径
    :param output_file_path: 输出文件的路径
    """
    # 定义地区名缩写的对应关系
    abbreviations = {
        'EastAsia': 'EA',
        'Africa': 'AF',
        'America': 'AM',
        'SouthAsia': 'SA',
        'Europe': 'EUR',
        'CentralAsia': 'CA',
        'WestAsia': 'WA',
        'NorthAsia': 'NA',
        'SoutheastAsia': 'SEA'
    }

    # 读取输入文件的内容
    with open(input_file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # 初始化列表，用于存储处理后的每一行
    output_lines = []

    # 遍历输入文本中的每一行
    for line in file_content.split('\n'):
        # 检查该行是否包含分组名，分组名是用等号包围的
        if line.startswith('====') and '_' in line:
            # 找到第一个下划线的位置
            underscore_index = line.find('_')
            # 获取下划线之前的部分（地区名）
            region_name = line[4:underscore_index]
            # 如果这部分是我们要缩写的地区名，进行缩写
            if region_name in abbreviations:
                # 将地区名替换为缩写
                abbreviated_region = abbreviations[region_name]
                # 重构该行，只替换第一个下划线之前的部分
                line = '====' + abbreviated_region + line[underscore_index:]
        # 将处理后的行添加到列表中
        output_lines.append(line)

    # 将处理后的行合并为字符串，用换行符连接
    output_text = '\n'.join(output_lines)

    # 将缩写后的文本写入到输出文件
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(output_text)

# 定义输入和输出文件的路径
input_file_path = 'C:/Users/LuzHu/Desktop/加长版poplist_77pop.txt'
output_file_path = 'C:/Users/LuzHu/Desktop/缩写版poplist_77pop.txt'

# 调用函数
abbreviate_regions_in_file_v3(input_file_path, output_file_path)

# 返回输出文件的路径
output_file_path
