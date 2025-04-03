def calcular(numero1, numero2, operacao):
    try:
        if operacao == "soma":
            return f"{numero1} + {numero2} = {numero1 + numero2}"
        elif operacao == "subtracao":
            return f"{numero1} - {numero2} = {numero1 - numero2}"
        elif operacao == "multiplicacao":
            return f"{numero1} * {numero2} = {numero1 * numero2}"
        elif operacao == "divisao":
            return f"{numero1} / {numero2} = {numero1 / numero2}"
        elif operacao == "divisao_inteira":
            return f"{numero1} // {numero2} = {numero1 // numero2}"
        elif operacao == "potencia":
            return f"{numero1} ** {numero2} = {numero1 ** numero2}"
        elif operacao == "modulo":
            return f"{numero1} % {numero2} = {numero1 % numero2}"
        else:
            return f"Operação Inválida!"
    except:
        return f"Erro ao executar a operação!"
    
def imc(peso, altura):
    try:
        resultado = peso / (altura ** 2)
        if resultado < 16:
            return f"Seu IMC é: {resultado:.2f} - Magreza grave"
        elif resultado >= 16 and resultado <= 16.9:
            return f"Seu IMC é: {resultado:.2f} - Magreza moderada"
        elif resultado >= 17 and resultado <= 18.5:
            return f"Seu IMC é: {resultado:.2f} - Magreza leve"
        elif resultado >= 18.6 and resultado <= 24.9:
            return f"Seu IMC é: {resultado:.2f} - Peso ideal"
        elif resultado >= 25 and resultado <= 29.9:
            return f"Seu IMC é: {resultado:.2f} - Sobrepeso"
        elif resultado >= 30 and resultado <= 34.9:
            return f"Seu IMC é: {resultado:.2f} - Obesidade grau I"
        elif resultado >= 35 and resultado <= 39.9:
            return f"Seu IMC é: {resultado:.2f} - Obesidade grau II (severa)"
        else:
            return f"Seu IMC é: {resultado:.2f} - Obesidade grau III (mórbida)"
    except:
        return f"Erro ao calcular o IMC"

def converteTemperatura(escala, temperatura):
    try:
        if escala == "celsius":
            result = (temperatura * 9/5) + 32
            return f"{temperatura}°C = {result:.1f}°F"
        else:
            result = (temperatura - 32) * 5/9
            return f"{temperatura}°F = {result:.1f}°C"
    except:
        return f"Erro ao converter a temperatura!"

def parImpar(numero):
    try:
        if numero % 2 == 0:
            return f"O número {numero} é par"
        else:
            return f"O número {numero} é ímpar."
    except:
        return f"Erro ao verificar Par ou Ímpar!"

def tabuada(numero):
    try:
        result = []
        for i in range(1, 11):
            result.append(f"{numero} x {i} = {numero * i}")
        return result
    except:
        return f"Erro ao calcular a tabuada!"

def converteMoeda(valor, de, para):
    taxas = {
        'brl': {'usd': 0.17, 'eur': 0.16},
        'usd': {'brl': 5.96, 'eur': 0.95},
        'eur': {'brl': 6.26, 'usd': 1.05}
    }
   
    if de == para:
        resultado = valor
    elif para in taxas[de]:
        resultado = valor * taxas[de][para]
    elif de in taxas[para]:
        resultado = valor / taxas[para][de]
   
    return f"{valor} {de.upper()} = {resultado:.2f} {para.upper()}"

def comparaCombustivel(etanol, gasolina):
    try:
        if etanol <= (0.7 * gasolina):
            return f"Compensa abastecer com etanol."
        else:
            return f"Compensa abastecer com gasolina."
    except:
        return f"Erro ao verificar o combustível!"

def calculaPotencia(base, expoente):
    try:
        if base == 0:
            return f"A potência é 1"
        else:
            return f"A potência é {base ** expoente}"
    except:
        return f"Erro ao verificar o combustível!"