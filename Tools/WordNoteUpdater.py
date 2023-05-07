import os
from joppy.api import Api
import DumpAndLoad

def get_table_md():
    # 获取API token
    token = os.environ.get('API_TOKEN')

    # 从 API_TOKEN 环境变量中读取 token

    if not token:
        raise ValueError('No API_TOKEN set for authentication!')

    api = Api(token=token)

    # 单词笔记标题和ID映射
    title_id_map = DumpAndLoad.load_from_file("D:/beidanci/data/title_id_map.txt")

    # 单词记忆忘记次数
    word_remembered_forgotten = DumpAndLoad.load_from_file("D:/beidanci/data/words.json")

    # 将单词记忆忘记次数字典按照forgotten排序
    sorted_result = sorted(word_remembered_forgotten.items(), key=lambda x: x[1]['forgotten'], reverse=True)

    # 挑选忘记次数大于0的
    result = [w for w in sorted_result if w[1]['forgotten'] > 0]

    # 构建markdown表头
    table_md = "|word|remembered|forgotten|\n|-|-|-|\n"

    for word, values in result:
        for word_title in title_id_map:
            if word == word_title["note_title"]:
                remembered = values['remembered']
                forgotten = values['forgotten']
                word_id = word_title["note_id"]
                row = f"|[{word}](:/{word_id})|{remembered}|{forgotten}|\n"
                # 将每行markdown表格拼接到总表上
                table_md += row

    return table_md


def update_note():
    # 获取API token
    token = os.environ.get('API_TOKEN')

    # 从 API_TOKEN 环境变量中读取 token

    if not token:
        raise ValueError('No API_TOKEN set for authentication!')

    api = Api(token=token)

    table_md = get_table_md()

    api.modify_note(id_="47025d660e1b4cb198c41e77a6942f2e", body=table_md)
