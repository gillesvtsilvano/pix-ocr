import re
from . import GenericPixParser


class NubankPixParser(GenericPixParser):
    name: str = 'nubank'
    _document_regex: str = r'((^NU)|(Nu Pagamentos S.A.)|(18.236.120/0001-58)|(0800 867 0463))'
    # _pattern = r'NU\nComprovante de\ntransferência\n(?P<DATA>.*) - (?P<HORA>.*)\nValor R\$ (?P<VALOR>.*)\nTipo de transferência Pix\nLeg] Destino\nNome (?P<BENEFICIARIO>.*)\n(CPF|CPNJ) (?P<CPFCNPJ>.*)\nInstituição (?P<BANCO>.*)\nTipo de conta (?P<TIPOCONTA>.*)\nLe Origem\n\n(?P<REMETENTE>[\W\w]*)\nInstituiç (?P<BANCO2>.*) - ([\W\w]*)\nAgência (?P<AGENCIA>.*)\nConta (?P<CONTA>.*)\n'
    _pattern = r'nu\\n+.*\\n+.*\\n+(?P<DATA>[0-9]{1,2} [JAN|FEV|MAR|ABR|MAI|JUN|JUL|AGO|SET|OUT|NOV|DEZ]+ 20[1,2][0-9]) - (?P<HORA>.{1,2}:.{1,2}:.{1,2})\\n+'

    @classmethod
    def parse_text(cls, text: str) -> dict[str, str]:
        result = re.match(cls._pattern, text, re.IGNORECASE | re.MULTILINE)
        for key, value in result.groupdict().items():
            cls.fields[key] = value
        return cls.fields

