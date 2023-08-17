import regex


class GenericParser:
    '''Generic Parser to be extended by other parsers'''

    name: str = 'generic'
    document_regex__: str = r'(?=x)(?!x)'   # impossible match

    @classmethod
    def parse_document(cls, text: str) -> bool:
        '''Parses a document'''
        match = False
        try:
            match = regex.findall(cls.document_regex, text)
        except Exception as exception:
            raise ValueError('document_regex is not a valid regular expression') from exception
        return bool(match)
    
    @classmethod
    def get_subclasses(cls) -> list:
        '''Returns a lists of subclasses of GenericParser'''
        return cls.__subclasses__()