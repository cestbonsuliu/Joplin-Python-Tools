from joppy.api import Api
from joppy import tools

def add_resource(api_token, notebook_title, note_title, resource_path=None):

    api = Api(token=api_token)

    notebook_id = api.add_notebook(title=notebook_title)


    if resource_path is not None:
        # Option 1: 添加一个带有图像数据URL的笔记,只适用于图像
        image_data = tools.encode_base64(resource_path)
        note_id = api.add_note(
            title=note_title,
            image_data_url=f"data:image/png;base64,{image_data}",
        )
    else:
        # Option 2: 分别创建笔记和资源,然后再把它们连接起来,适用于任意的附件
        note_id = api.add_note(title=note_title)
        resource_id = api.add_resource(filename=resource_path, title="My first resource")
        api.add_resource_to_note(resource_id=resource_id, note_id=note_id)

    return notebook_id, note_id
