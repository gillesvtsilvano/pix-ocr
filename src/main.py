import os
from document import Document
from parsers import parser_factory
from ocr import OCR
from utils import load_images


# TODO: move to settings file
IMAGES_DIR = os.path.join('..', '../images')
OUTPUT_DIR = os.path.join('..', '../output')

def main():
    images = load_images(IMAGES_DIR)

    documents = []

    for img in images:
        text = OCR.image_to_text(img)
        parser = parser_factory(text)
        doc = Document(parser.parse_document(text), path=img.filename)
        documents.append(doc)
    
    # export_xls(output='file.xlsx', documents)
        
if __name__ == '__main__':
    main()
