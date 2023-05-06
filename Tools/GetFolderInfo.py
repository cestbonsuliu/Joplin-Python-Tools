from joppy.api import Api
import os

FOLDER_ROOT = "D:/Joplin_PDF"

def get_folder_info(api, note):
    """获取笔记对应目录的信息"""
    notebook = api.get_notebook(id_=note.parent_id)

    titles = ""
    while notebook.parent_id:
        titles += notebook.title + "/"
        notebook = api.get_notebook(id_=notebook.parent_id)
    titles += notebook.title

    title_list = titles.split('/')
    title_list.reverse()

    title_folder = '/'.join(title_list)
    end_folder = os.path.join(FOLDER_ROOT, title_folder)

    return end_folder