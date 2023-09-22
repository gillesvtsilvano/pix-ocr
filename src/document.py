from image import Image
from parsers import GenericParser


class Document:
    text: str
    image: Image
    parser: GenericParser
    