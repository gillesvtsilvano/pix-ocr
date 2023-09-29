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


def get_images(images_path: str = IMAGES_DIR):
    images = []
    for filename in os.listdir(images_path):
        filepath = os.path.join(os.getcwd(), images_path, filename)
        if os.path.isfile(filepath):
            images.append(Image(filepath))
        else:
            logging.warning('Skipping %s because it is not a standard file', filepath)
    return images


def main():
    try:
        images = get_images()
        documents = []
        for img in images:
            doc = Document()
            doc.image = img
            doc.text = OCR.image_to_text(doc.image)
            doc.parser = parser_factory(doc.text)
            if not doc.parser:
                raise Exception(f'Parser not found for file {doc.image.filename}')
            print(doc.image.filename, 'Resultado: ', doc.parser.parse_text(doc.text))
            documents.append(doc)
    except Exception as exception:
        logging.warning('Could not parse image: %s', exception)

    # export_xls(output='file.xlsx', documents)


if __name__ == '__main__':
    main()
