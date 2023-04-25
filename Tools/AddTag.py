from joppy.api import Api


def add_note_with_tag(token, notebook_title, note_title, note_body, tag_title):

    api = Api(token=token)

    notebook_id = api.add_notebook(title=notebook_title)

    note_id = api.add_note(title=note_title, body=note_body, parent_id=notebook_id)

    tags = api.get_all_tags()
    for tag in tags:
        if tag['title'] == tag_title:
            tag_id = tag['id']
            break
    else:
        tag_id = api.add_tag(title=tag_title)

    api.add_tag_to_note(tag_id=tag_id, note_id=note_id)
