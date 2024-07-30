def split_file_by_lines(input_file, output_prefix, lines_per_file):
    """
    按行分割文件。

    :param input_file: 要分割的原始文件路径
    :param output_prefix: 输出文件的文件名前缀
    :param lines_per_file: 每个输出文件应包含的行数
    """
    current_part = 1
    with open(input_file, 'r', encoding='utf-8') as infile:
        lines = []
        for line in infile:
            lines.append(line)
            if len(lines) == lines_per_file:
                with open(f"{output_prefix}_{current_part}.csv", 'w', encoding='utf-8') as outfile:
                    outfile.writelines(lines)
                lines = []
                current_part += 1

                # 处理剩余的行（如果有的话）
        if lines:
            with open(f"{output_prefix}_{current_part}.csv", 'w', encoding='utf-8') as outfile:
                outfile.writelines(lines)

            # 使用示例


input_file_path = 'large_file.txt'
output_file_prefix = 'part_'
lines_per_file = 1000  # 每个输出文件1000行
split_file_by_lines("aion.csv", "aion", 20000)