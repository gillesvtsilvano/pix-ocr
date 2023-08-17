import regex


class DocumentMapping:
    key: str = None
    value: str = None
    regex: str = None

    def __init__(self, key: str, value: str, regex: str) -> None:
        '''Stores mappings of the Document'''
        self.key = key
        self.value = value
        # Check if regex is valid
        if regex.fullmatch(regex):
            self.regex = regex 
        else:
            raise Exception('regex is not a valid regular expression')


class Document:
    '''Generic Document'''

    mappings: [DocumentMapping] = []

    def classify(self, text: str) -> bool:
        match = regex.findall(self.document_regex, text)
        return bool(match)

    def extract(self):
        pass
