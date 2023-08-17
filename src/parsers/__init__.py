'''Module providing parsers for different type of images.'''

from .generic_parser import GenericParser
from .nubank_parser import NubankParser


def parser_factory(text: str) -> GenericParser:
    '''Finds the correct parser for the Document and returns its object or None'''

    for subclass in GenericParser.__subclasses__():
        result = subclass.parse_document(text)
        if result:
            return subclass()
    return None
