import sys
from pathlib import Path

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
XLS_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPT_DOCUMENTS = []
PPTX_DOCUMENTS = []
PDF_DOCUMENTS = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
ZIP_ARCHIVES = []
GZ_ARCHIVES = []
TAR_ARCHIVES = []
ISO_IMAGE = []
IMG_IMAGE = []
MY_OTHER = []


REGISTER_EXTENSION = {
    'JPEG': JPEG_IMAGES,
    'JPG': JPG_IMAGES,
    'PNG': PNG_IMAGES,
    'SVG': SVG_IMAGES,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'XLS': XLS_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPT': PPT_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'ZIP': ZIP_ARCHIVES,
    'GZ': GZ_ARCHIVES,
    'TAR': TAR_ARCHIVES,
    'ISO': ISO_IMAGE,
    'IMG': IMG_IMAGE,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(name: str) -> str:
    return Path(name).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'MY_OTHER', 'image'):
                FOLDERS.append(item)
                scan(item)
            continue

        extension = get_extension(item.name)
        full_name = folder / item.name
        if not extension:
            MY_OTHER.append(full_name)
        else:
            try:
                extension_registration = REGISTER_EXTENSION[extension]
                extension_registration.append(full_name)
                EXTENSIONS.add(extension)
            except KeyError:
                UNKNOWN.add(extension)
                MY_OTHER.append(full_name)


if __name__ == '__main__':
    folder_process = sys.argv[1]
    scan(Path(folder_process))
# KNOWN IMAGE FORMATS OUTPUT:
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images png: {PNG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
# KNOWN VIDEO FORMATS OUTPUT:
    print(f'Video avi: {AVI_VIDEO}')
    print(f'Video mp4: {MP4_VIDEO}')
    print(f'Video mov: {MOV_VIDEO}')
    print(f'Video mkv: {MKV_VIDEO}')
# KNOWN DOCUMENT FORMATS OUTPUT:
    print(f'Document doc: {DOC_DOCUMENTS}')
    print(f'Document docx: {DOCX_DOCUMENTS}')
    print(f'Document txt: {TXT_DOCUMENTS}')
    print(f'Document xls: {XLS_DOCUMENTS}')
    print(f'Document xlsx: {XLSX_DOCUMENTS}')
    print(f'Document ppt: {PPT_DOCUMENTS}')
    print(f'Document pptx: {PPTX_DOCUMENTS}')
    print(f'Document pdf: {PDF_DOCUMENTS}')
# KNOWN AUDIO FORMATS OUTPUT:
    print(f'Audio mp3: {MP3_AUDIO}')
    print(f'Audio ogg: {OGG_AUDIO}')
    print(f'Audio wav: {WAV_AUDIO}')
    print(f'Audio AMR: {AMR_AUDIO}')
# KNOWN ARCHIVES FORMAT OUTPUT:
    print(f'Archive zip: {ZIP_ARCHIVES}')
    print(f'Archive gz: {GZ_ARCHIVES}')
    print(f'Archive tar: {TAR_ARCHIVES}')
# KNOWN IMAGE FORMATS OUTPUT:
    print(f'Image ISO: {ISO_IMAGE}')
    print(f'Image img: {IMG_IMAGE}')
# OUTPUT ALL KNOWN EXTENSIONS:
    print(f'EXTENSIONS: {EXTENSIONS}')
# OUTPUT ALL FOUNDED BUT UNKNOWN EXTENSTIONS:
    print(f'UNKNOWN: {UNKNOWN}')
