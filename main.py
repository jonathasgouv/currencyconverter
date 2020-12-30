
import requests

api_address='http://data.fixer.io/api/latest?access_key=4ddc12855ee9d5a03f7576596db26e36&format=1'
url = api_address
json_data = requests.get(url).json()

USD = (json_data['rates']['USD'])
BRL = 1/(json_data['rates']['BRL'])

def conversorBRLtoEUR(qt):
    resultado = qt*BRL
    return resultado

def conversorBRLtoUSD(qt):
    resultado = (qt*BRL)*(USD)
    return resultado

def conversorEURtoBRL(qt):
    resultado = qt/BRL
    return resultado

def conversorUSDtoBRL(qt):
    resultado = (qt/BRL)/(USD)
    return resultado
while True:
    print("-"*60+"\n")
    print("(1) Converter de Real para Euro\n(2) Converter de Real para Dólar\n(3) Converter de Euro para Real\n(4) Converter de Dólar para Real\n")
    print("-"*60+"\n")

    opt = int(input("Digite o número da operação a ser realizada:\n"))

    if opt == 1:
        qtd = str(input("\nDigite o valor:\nR$ ")).replace(",",".")
        qtd = float(qtd)
        valor = conversorBRLtoEUR(qtd)
        print("O valor após conversão é de: £ {:0.2f}".format(valor).replace(".",","))
    elif opt == 2:
        qtd = str(input("\nDigite o valor:\nR$ ")).replace(",",".")
        qtd = float(qtd)
        valor = conversorBRLtoUSD(qtd)
        print("O valor após conversão é de: $ {:0.2f}".format(valor).replace(".",","))
    elif opt == 3:
        qtd = str(input("\nDigite o valor:\n£  ")).replace(",",".")
        qtd = float(qtd)
        valor = conversorEURtoBRL(qtd)
        print("O valor após conversão é de: R$ {:0.2f}".format(valor).replace(".",","))
    elif opt == 4:
        qtd = str(input("\nDigite o valor:\n$  ")).replace(",",".")
        qtd = float(qtd)
        valor = conversorUSDtoBRL(qtd)
        print("O valor após conversão é de: R$ {:0.2f}".format(valor).replace(".",","))
    resposta = str(input("Deseja continuar? [S/N]\n")).upper()
    if resposta[0] == "N":
        break