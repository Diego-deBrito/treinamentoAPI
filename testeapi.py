# Fazendo requisições
import requests

# Troca de informações
import json

# Pegando api do site
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL".format())
# transformando
cotacoes = cotacoes.json()
# Cotação do dolar
cotacoes_dolar = cotacoes["USDBRL"]["bid"]
# Cotação do euro
cotacoes_euro = cotacoes['EURBRL']['bid']
print(cotacoes)
print("\n")
print(cotacoes_dolar)
print("\n")
print(cotacoes_euro)