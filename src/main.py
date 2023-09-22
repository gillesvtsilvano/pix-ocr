import os
import logging
from document import Document
from image import Image
from parsers import parser_factory
from ocr import OCR


# TODO: move to settings file
IMAGES_DIR = os.path.join('images')
OUTPUT_DIR = os.path.join('output')

logging.basicConfig(
    # filename='pix-orc.log',
    level=logging.DEBUG,
    format="%(asctime)s | %(levelname)s: %(message)s",
)

def main():
    images = []
    for filename in os.listdir(IMAGES_DIR):
        filepath = os.path.join(os.getcwd(), IMAGES_DIR, filename)
        if os.path.isfile(filepath):
            images.append(Image(filepath))
        else:
            logging.warning('Could not create image because %s is not a standard file', filepath)

    documents = []

    for img in images:
        try:
            doc = Document()
            doc.image = img
            doc.text = OCR.image_to_text(img.image)
            doc.parser = parser_factory(doc.text)
            if not doc.parser:
                raise Exception('Parser None for file %s', doc.image.filename)
            else:
                print(doc.image.filepath, doc.parser.name)
        except Exception as exception:
            logging.warning('Could not process document of file %s: %s', doc.image.filename, exception)
        documents.append(doc)
    # export_xls(output='file.xlsx', documents)
        
if __name__ == '__main__':
    main()
