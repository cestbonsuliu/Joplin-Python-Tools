from joppy.api import Api
import re

def modify_notes(api_token, notebook_id, pattern):
    # 创建 API 实例
    api = Api(token=api_token)

    # 获取指定笔记本中的所有笔记
    notes = api.get_notes(notebook_id=notebook_id, fields="id,title,body")

    for note in notes.items:
        # 获取笔记内容并进行替换
        note_body = note.body
        new_s = re.sub(pattern, r'\1', note_body)

        # 更新笔记内容
        api.modify_note(id_=note.id, body=new_s)

    print("所有笔记更新完成！")

if __name__ == "__main__":

    # 调用示例
    api_token = 'token'
    notebook_id = "id"
    pattern = '\[(.*?)\]\(http://c\.biancheng\.net/.*?\)'

    modify_notes(api_token, notebook_id, pattern)
