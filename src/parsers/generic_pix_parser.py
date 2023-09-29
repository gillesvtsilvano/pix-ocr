import re


class GenericPixParser:
    """Generic Parser to be extended by other parsers"""

    # Generic Parser must not match any document
    _document_regex: str = r'(?=x)(?!x)'
    name: str = 'generic'
    fields: dict[str, str] = {
        'DATA': None,
        'HORA': None,
        'REMETENTE': None,
        'CPFCNPJ': None,
        'BANCO': None,
        'AGENCIA': None,
        'CONTA': None,
        'REFERENCIA': None,
        'VALOR R$': None,
        'BENEFICIARIO': None,
        'CPFCNPJ2': None,
        'BANCO2': None,
        'AGENCIA2': None,
        'CONTA2': None,
        'REFERENCIA2': None,
    }

    @classmethod
    def classify_text(cls, text: str) -> bool:
        """Classifies a document"""
        if not text:
            raise Exception('Invalid text')
        try:
            match = re.findall(cls.get_document_regex(), text)
        except Exception as exception:
            raise ValueError('Invalid document regex') from exception
        return bool(match)

    @classmethod
    def parse_text(cls, text: str) -> dict[str, str]:
        if not text:
            raise ValueError('Invalid text')
        return {}

    @classmethod
    def get_document_regex(cls):
        return cls._document_regex

    @classmethod
    def get_subclasses(cls) -> list:
        """Returns a lists of subclasses of GenericParser"""
        return cls.__subclasses__()

    @classmethod
    def get_parser_name(cls) -> str:
        return cls.name
