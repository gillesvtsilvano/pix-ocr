from . import GenericParser


class NubankParser(GenericParser):
    name: str = 'nubank'
    __document_regex = r'(^nu)|(Nu Pagamentos S.A.)|(18.236.120/0001-58)|(0800 867 0463){{e<1}}'
