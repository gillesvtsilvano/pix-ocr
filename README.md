# pix-ocr
Tool for processing PIX payment images amd formating for IBM i2 using pytesseract.

# Colunas esperadas pelo I2

Será gerado um arquivo Excel (.xls) na pasta `./resultados` nomeado com a data e hora da solicitação da conversão contendo os dados encontrados nas imagens, estruturados nas seguintes colunas:

```python
['DATA', 'HORA', 'REMETENTE', 'CPF/CNPJ', 'BANCO', 'AGENCIA', 'CONTA', 'REFERENCIA', 'VALOR R$', 'BENEFICIARIO', 'CPF/CNPJ2', 'BANCO2', 'AGENCIA2', 'CONTA2', 'REFERENCIA2', 'HASH']
```

# Limitações conhecidas

Limite de 1.000.000 de linhas no arqruivo de saída.