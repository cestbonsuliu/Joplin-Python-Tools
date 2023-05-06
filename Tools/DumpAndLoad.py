import json
import os

def dump_to_file(map, file_path):
    """
    将映射关系写入文件
    :param map: 映射关系
    :param file_path: 文件路径
    """
    # 验证文件路径是否存在
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    # 将数据写入文件
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(map, f, ensure_ascii=False)
    except IOError as e:
        print(f"写入文件失败：{e}")


def load_from_file(file_path):
    """
    从文件中读取映射关系
    :param file_path: 文件路径
    :return: 映射关系
    """
    # 验证文件路径是否存在并有权限访问
    if not os.path.exists(file_path) or not os.access(file_path, os.R_OK):
        print(f"文件不存在或无权访问：{file_path}")
        return None

    # 打开文件，读取数据
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.decoder.JSONDecodeError as e:
        print(f"解析 JSON 数据失败：{e}")
        return None
    except Exception as e:
        print(f"读取文件失败：{e}")
        return None

    return data
