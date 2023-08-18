from . import GenericParser


class NubankParser(GenericParser):
    name: str = 'nubank'
    document_regex: str = r'(^nu)|(Nu Pagamentos S.A.)|(18.236.120/0001-58)|(0800 867 0463){{e<1}}'

    def __init__(self):
        self.field_parsers['DATA'] = self.data_parser
        self.field_parsers['HORA'] = self.hora_parser
        self.field_parsers['REMETENTE'] = self.remetente_parser

    def data_parser(cls, text, field='DATA'):
        pass