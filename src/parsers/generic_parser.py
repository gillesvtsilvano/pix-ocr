import regex
from document import Document


class GenericParser:
    '''Generic Parser to be extended by other parsers'''

    #Generic Parser must not match any document
    document_regex__: str = r'(?=x)(?!x)'
    name: str = 'generic'
    field_parsers: dict[str, str] = {
        'DATA': None,
        'HORA': None,
        'REMETENTE': None,
        'CPF/CNPJ': None,
        'BANCO': None,
        'AGENCIA': None,
        'CONTA': None,
        'REFERENCIA': None,
        'VALOR R$': None,
        'BENEFICIARIO': None,
        'CPF/CNPJ2': None,
        'BANCO2': None,
        'AGENCIA2': None,
        'CONTA2': None,
        'REFERENCIA2': None,
    }

    @classmethod
    def classify_document(cls, document: Document) -> bool:
        '''Classify a document'''
        match = False
        if not document:
            raise Exception('Invalid Document.')
        if not document.text:
            raise Exception('Document')
        
        try:
            match = regex.findall(cls.document_regex, document.text)
        except Exception as exception:
            raise ValueError('document_regex is not a valid regular expression') from exception
        return bool(match)
    
    @classmethod
    def parse_document(cls, document_text) -> dict:
        return None
    
    @classmethod
    def get_subclasses(cls) -> list:
        '''Returns a lists of subclasses of GenericParser'''
        return cls.__subclasses__()