"""Module providing parsers for different type of images"""
from typing import Any, Type

from .generic_pix_parser import GenericPixParser
from .nubank_pix_parser import NubankPixParser


def parser_factory(text: str) -> Type[GenericPixParser] | Any:
    """Finds the correct parser for the Document text and returns its Class or None"""

    for subclass in GenericPixParser.get_subclasses():
        result = subclass.classify_text(text)
        if result:
            return subclass
    return GenericPixParser
