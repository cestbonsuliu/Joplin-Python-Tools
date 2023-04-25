# Joplin-Python-Tools

[Joplin](https://joplinapp.org/) 是我的主力笔记软件，比较符合我的需求。但是 Joplin 的功能并不完善，所以需要自己编写代码来增加功能改善体验，可以编写插件，但由于前端能力一般，所以尝试使用 Python 来编写代码。

使用 Python 操控 Joplin 需要借助 Joplin API，这是一个基于 RESTful 风格的 API，可以让我们通过 HTTP 请求来调用 Joplin 的各种功能。

已经有不少库封装了使用 Python 处理 Joplin API ，所以不用自己从头造轮子，常用的库如下：

- [Python_Joplin](https://github.com/S73ph4n/python_joplin)
- [joppy](https://github.com/marph91/joppy)：比较常用

在这里向这些库的作者表示感谢！



# 使用 Joppy



## 基本操作



### 获取所有笔记

```
from joppy.api import Api

# Create a new Api instance.
api = Api(token=YOUR_TOKEN)

# Get all notes. Note that this method calls get_notes() multiple times to assemble the unpaginated result.
notes = api.get_all_notes()
```

### 获取某笔记本下所有笔记

```
from joppy.api import Api

api = Api(token=YOUR_TOKEN)

notes = api.get_notes(notebook_id=notebookId)
```

### 获取笔记正文


```
from joppy.api import Api

# Create a new Api instance.
api = Api(token=YOUR_TOKEN)

# Get note body
note_body = api.get_note(id_="note_id",field="body")
```

`fields` 参数指定获取的信息，可以设置多个信息例如"id,title,body"获取id、标题、正文

## 实践案例

### 批量更新笔记内容

批量更新指定 Joplin 笔记本中所有笔记的内容。

[ModifyNotes.py](Tools/ModifyNotes.py)

### 为笔记添加标签

[AddTag.py](Tools/AddTag.py)

### 将资源添加到笔记

[AddResource.py](Tools/AddResource.py)


### 移除孤立资源

[DeleteUnreferencedResources.py](Tools/DeleteUnreferencedResources.py)