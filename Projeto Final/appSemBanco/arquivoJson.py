import json, os

def salvarDicionarioJson(dicionario, nome_arquivo='usuarios.json'):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dicionario, arquivo, indent=4)
        print(f"Dicionário salvo em {nome_arquivo} com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar o dicionário: {e}")

def carregaDicionarioJson(nome_arquivo='usuarios.json'):
    dicionario = {}  
    if os.path.exists(nome_arquivo): 
        try:
            with open(nome_arquivo, 'r') as arquivo:
                dicionario = json.load(arquivo) 
                dicionario = {int(chave): valor for chave, valor in dicionario.items()}
        except Exception as e:
            print(f"Ocorreu um erro ao carregar o dicionário: {e}")
    else:
        print(f"O arquivo {nome_arquivo} não existe. Um dicionário em branco foi criado.")
    
    return dicionario