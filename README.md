# PIX-OCR

Tool for processing PIX payment images amd formating for IBM i2 using pytesseract.

## Requirements

### Windows
- Install Microsoft C++ Build Tools from this [link](https://aka.ms/vs/17/release/vs_BuildTools.exe)

### Linux
- Install libGL.so.1
```$ apt install libgl1```

### Common


- pip install -r requirements.txt
- python src/main.py

## Output

Será gerado um arquivo Excel (.xls) na pasta `./resultados` nomeado com a data e hora da solicitação da conversão contendo os dados encontrados nas imagens, estruturados nas seguintes colunas:

## Expected columns for I2 specs

```python
['DATA', 'HORA', 'REMETENTE', 'CPF/CNPJ', 'BANCO', 'AGENCIA', 'CONTA', 'REFERENCIA', 'VALOR R$', 'BENEFICIARIO', 'CPF/CNPJ2', 'BANCO2', 'AGENCIA2', 'CONTA2', 'REFERENCIA2', 'HASH']
```

## Know limitations

Excel limit 1.000.000 lines per file.
