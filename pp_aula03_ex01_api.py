# Autor: Lucas Inácio
# API - CNPJ

# Importar biblioteca
import requests

cnpj = "05061448000139"
url = f"https://api.opencnpj.org/{cnpj}"
res = requests.get(url)

dados = res.json()

print(f'CNPJ: {dados["cnpj"]}')
print("Razão Social: ", dados['razao_social'])
print(f'Nome Fantasia: {dados["nome_fantasia"]}')
print(f'Situação Cadastral: {dados["situacao_cadastral"]}')