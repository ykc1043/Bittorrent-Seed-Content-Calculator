import os
import bencoder
import humanfriendly

def get_torrent_file_size(file_name):
    # 读取种子文件
    with open(file_name, 'rb') as f:
        data = f.read()

    # 使用 bencoder 库解码种子文件
    decoded = bencoder.decode(data)

    # 获取种子文件内所有文件的大小
    total_size = 0
    if b'files' in decoded[b'info']:
        # 种子文件包含多个文件
        for file_info in decoded[b'info'][b'files']:
            total_size += file_info[b'length']
    else:
        # 种子文件只包含单个文件
        total_size = decoded[b'info'][b'length']

    return total_size

# 获取当前目录下所有文件名
file_names = os.listdir()

# 解析每个种子文件，并累加所有文件的大小
total_size = 0
for file_name in file_names:
    if file_name.endswith('.torrent'):
        total_size += get_torrent_file_size(file_name)

# 将文件大小转换为人类可读的格式
total_size_str = humanfriendly.format_size(total_size)
print(f'Total size of all files in torrents: {total_size_str}')
