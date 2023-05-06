from joppy.api import Api
import GetFolderInfo
import os

def build_note_pdf_map(api, notes):
    """构建笔记与 PDF 之间的映射关系"""
    note_pdf_map = []
    for note in notes:
        end_PDF_folder = GetFolderInfo.get_folder_info(api, note)

        normal_title = note.title.lower().replace(" ", "_")
        end_PDF = os.path.join(end_PDF_folder, f"{normal_title}.pdf")

        note_pdf_map.append({
            "note_title": note.title,
            "note_pdf_folder": end_PDF,
        })

    return note_pdf_map