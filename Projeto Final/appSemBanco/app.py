from flask import Flask, render_template, request, redirect, url_for
from exercicios.exercicios import *
from apis.apis import *
from datetime import datetime
from arquivoJson import *
import locale

# Configurar o locale para o formato brasileiro
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
id = 0

#cria um objeto da classe flask, importando todas as informações
app = Flask(__name__)

@app.route('/')
def home():
    # return "Home"
    return render_template('home.html')

@app.route('/api', methods=['GET', 'POST'])
def api():
    context = {}
    if request.method == 'POST':
        if 'consulta_cep' in request.form:
            context['api_cep'] = buscarEndereco(request.form['cep'])
        elif 'consulta_cachorro' in request.form:
            context['api_cachorro'] = imagensCachorrosAleatorias()
        elif 'consulta_moeda' in request.form:
            retorno = {}
            if len(request.form['moedas']) > 0:
                resposta = cotacaoMoedas(request.form['moedas'])
                if isinstance(resposta, dict):
                    moeda = request.form['moedas'].replace("-","")
                    moeda_dados = resposta[moeda]
                    retorno['nome'] = moeda_dados['name']
                    retorno['compra'] = f"R$ {locale.format_string('%.2f', float(moeda_dados['bid']), grouping=True)}" #grouping add separador de milhar
                    retorno['venda'] = f"R$ {locale.format_string('%.2f', float(moeda_dados['ask']), grouping=True)}"
                    retorno['data'] = datetime.strptime(moeda_dados['create_date'], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
                    #strptime converte uma string para um objeto datetime
                    #strftime converte um objeto datetime para uma string formatada
                else:
                    retorno['mensagem'] = resposta
            context['api_moedas'] = retorno
    return render_template('api.html', context = context)

@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html', users=users)

@app.route('/gerenciar_usuario', methods=['GET', 'POST'])
def gerenciar_usuario():
    user_id = request.args.get('user_id', type=int)  # Obtém o user_id da query string
    user = users.get(user_id) if user_id else None  # Recupera o usuário para edição, se existir
    if request.method == 'POST':
        action = request.form.get('action')  # Identifica a ação do formulário
        if action == 'buscar_cep':  # Ação de buscar CEP
            if user is None:  # Cria um novo dicionário para o novo usuário
                user = recuperaInfo(request)
            retorno = buscarEndereco(request.form['cep'])
            if retorno:
                user.update({
                    "endereco": retorno['logradouro'],
                    "bairro": retorno['bairro'],
                    "complemento": retorno['complemento'],
                    "estado": retorno['estado'],
                    "cidade": retorno['localidade'],
                    "cep": retorno['cep']
                })
            return render_template('gerenciar_usuario.html', user=user, user_id=user_id)

        # Ação padrão: Salvar ou editar o usuário
        if user:  # Editar usuário existente
            users[user_id] = recuperaInfo(request)
            salvarDicionarioJson(users)
        else:  # Adicionar novo usuário
            global id
            id += 1
            new_id = id
            users[new_id] = recuperaInfo(request)
            salvarDicionarioJson(users)
        return redirect(url_for('usuarios'))

    return render_template('gerenciar_usuario.html', user=user, user_id=user_id)
       
@app.route('/excluir_usuario/<int:user_id>')
def excluir_usuario(user_id):
    users.pop(user_id, None)
    salvarDicionarioJson(users)
    return redirect(url_for('usuarios'))

def recuperaInfo(request):
        dados = {}
        if request != None:
            dados = {
                'nome': request.form['nome'],
                'sobrenome': request.form['sobrenome'],
                'email': request.form['email'],
                'data_nascimento': request.form['data_nascimento'],
                'cep': request.form['cep'],
                'endereco': request.form['endereco'],
                'numero': request.form['numero'],
                'complemento': request.form['complemento'],
                'bairro': request.form['bairro'],
                'cidade': request.form['cidade'],
                'estado': request.form['estado']
            }
        return dados

@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
    # return "Calculadora"
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operacao = request.form["operacao"]
        result = calcular(num1,num2,operacao)
    return render_template('calculadora.html', result=result)

@app.route('/ferramentas', methods=['GET', 'POST'])
def ferramentas():
    # return "Ferramentas"
    context = {}
    if request.method == "POST":
        if "convert_temp" in request.form:
            temperatura = float(request.form['temp'])
            escala = request.form['escala']
            retorno = converteTemperatura(escala, temperatura)
            context['temp_result'] = retorno
        elif "calc_imc" in request.form:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            context['imc_result'] = imc(peso, altura)
        elif "verificar_par_impar" in request.form:
            num = int(request.form['num'])
            context['par_impar_result'] = parImpar(num)
        elif "gerar_tabuada" in request.form:
            num = int(request.form['num'])
            context['tabuada_result'] = tabuada(num)
        elif "converter_moeda" in request.form:
            valor = float(request.form['valor'])
            de = request.form['de']
            para = request.form['para']
            context['moeda_result'] = converteMoeda(valor, de, para)
        elif "calc_combustivel" in request.form:
            etanol = float(request.form['etanol'])
            gasolina = float(request.form['gasolina'])
            context['combustivel_result'] = comparaCombustivel(etanol, gasolina)
        elif "calc_potencia" in request.form:
            base = float(request.form['base'])
            expoente = float(request.form['expoente'])
            context['potencia_result'] = calculaPotencia(base, expoente)
    return render_template('ferramentas.html', context=context)

users = carregaDicionarioJson()

#garante que o código só seja executado se o script for rodado diretamente, e não importado como um módulo.
if __name__ == '__main__':
    app.run(debug=True) #ativa do debug
    
#venv\Scripts\Activate
#pip freeze > requirements.txt # cria o arquivo requirements
#pip install -r requirements.txt # instala no computador
