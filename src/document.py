from image import Image
from parsers import GenericPixParser


class Document:
    text: str = None
    image: Image = None
    parser: GenericPixParser = None
    data = {}

    def parse(self):
        if not self.parser:
            raise ValueError('Parser not found')
        elif not self.text:
            raise ValueError('Text not found')
        elif isinstance(self.parser, GenericPixParser):
            raise ValueError('Invalid parser')
        else:
            return self.parser.parse_text(self.text)

    