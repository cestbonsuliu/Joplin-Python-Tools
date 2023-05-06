import os
from pathlib import Path
import tempfile

from joppy.api import Api
import pypandoc


def create_custom_css_file(path):
    with open(path, "w") as outfile:
        outfile.write(
            """
img {
  /* prevent image going out of page */
  max-width: 100%;
  /* center image */
  display: block;
  margin-left: auto;
  margin-right: auto;
}
figure > figcaption{
    text-align: center;
}
"""
        )


def convert_notes(joplin_api, note_titles, output_format="pdf", output_folder="note_export"):

    api = joplin_api

    candidates = note_titles

    # Create a temporary directory for the resources.
    with tempfile.TemporaryDirectory() as tmpdirname:
        # Convert all notes to the specified format.
        os.makedirs(output_folder, exist_ok=True)
        for candidate in candidates:
            note = api.get_note(id_=candidate.id, fields="body")
            note_body = note.body

            # Download and add all image resources
            resources = api.get_all_resources(note_id=candidate.id, fields="id,mime")
            for resource in resources:
                if not resource.mime.startswith("image"):
                    continue
                resource_binary = api.get_resource_file(resource.id)
                resource_path = str(Path(tmpdirname) / resource.id)
                with open(resource_path, "wb") as outfile:
                    outfile.write(resource_binary)
                # Replace joplin's local link with the path to the just
                # downloaded resource. Use the "file:///" protocol:
                # https://stackoverflow.com/a/18246357/7410886
                note_body = note_body.replace(
                    f":/{resource.id}", f"file:///{resource_path}"
                )

            title_normalized = (
                candidate.title.lower().replace(" ", "_")
            )
            output_path = (
                f"{output_folder}/{title_normalized}.{output_format}"
            )

            valid_output_formats = pypandoc.get_pandoc_formats()[1]
            if output_format not in valid_output_formats:
                raise ValueError(
                    f"Invalid format: {output_format}. "
                    f"Valid formats: {valid_output_formats}."
                )
            # special arguments for some output formats
            custom_css_file = str(Path(tmpdirname) / "custom.css")
            create_custom_css_file(custom_css_file)
            format_kwargs = {
                # https://github.com/NicklasTegner/pypandoc/issues/186#issuecomment-673282133
                "pdf": {
                    "to": "html",
                    "extra_args": [
                        "--pdf-engine",
                        "weasyprint",
                        "--metadata",
                        f"title={candidate.title}",
                        "--css",
                        f"file:///{custom_css_file}",
                    ],
                }
            }

            # 将字符串强制转换为utf-8编码
            note_body_utf8 = note_body.encode('utf-8', 'ignore')

            pypandoc.convert_text(
                note_body_utf8,
                format="md",
                outputfile=output_path,
                **format_kwargs.get(output_format, {"to": output_format}),
            )
