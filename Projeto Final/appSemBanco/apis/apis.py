import requests

def buscarEndereco(cep):
    url_api = f'http://www.viacep.com.br/ws/{cep}/json'
    req = requests.get(url_api)
    if req.status_code == 200:
        dicionario = req.json()
        if 'erro' in dicionario:
            return None
        return dicionario
    else:
        return None
    
def imagensCachorrosAleatorias():
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['message']
    else:
        return f"Erro ao acessar a API: {response.status_code}"
    
def cotacaoMoedas(origem):
    url_api = f'https://economia.awesomeapi.com.br/last/{origem}'
    req = requests.get(url_api)
    if req.status_code == 200:
        dicionario = req.json()
        return dicionario
    else:
        dicionario = req.json()
        if dicionario['message'] != None:
            return dicionario['message']
        return None
    