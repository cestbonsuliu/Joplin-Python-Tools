import re

from joppy.api import Api

def delete_unreferenced_resources(api: Api) -> None:

    referenced_resources = set()
    for note in api.get_all_notes(fields="id,body"):
        matches = re.findall(r"\[.*\]\(:.*\/([A-Za-z0-9]{32})\)", note.body)
        referenced_resources.update(matches)

    assert len(referenced_resources) > 0, "sanity check"

    for resource in api.get_all_resources():
        if resource.id not in referenced_resources:
            print("Deleting resource:", resource)
            api.delete_resource(resource.id)
