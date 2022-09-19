# Consumindo informação de uma api de cotação de moedas
import requests

class Conversor_de_moedas:
    cotacoes = requests.get(
        'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
    cotacoes = cotacoes.json()
    escolha = 0
    real = 0

    def __init__(self, escolha, real):
        self.escolha = escolha
        self.real = real

    def converter(self):
        if self.escolha == 1:
            dolar_real = float(self.cotacoes['USDBRL']['bid'])
            print(
                f"\nCotação do dólar: US$1.00 é equivalente a R${dolar_real:.2f}\n")
            dolar = self.real/dolar_real
            print(f"R${self.real:.2f} é equivalente a US${dolar:.2f}\n")

        elif self.escolha == 2:
            euro_real = float(self.cotacoes['EURBRL']['bid'])
            print(
                f"\nCotação do euro: 1.00€ é equivalente a R${euro_real:.2f}\n")
            euro = self.real/euro_real
            print(f"R${self.real:.2f} é equivalente a {euro:.2f}€\n")

        elif self.escolha == 3:
            bitcoin_real = float(self.cotacoes['BTCBRL']['bid'])*1000

            print(
                f"\nCotação do bitcoin: 1.00₿ é equivalente a R${(bitcoin_real):.2f}\n")
            bitcoin = self.real/bitcoin_real
            print(f"R${self.real:.2f} é equivalente a {bitcoin:.8f}₿\n")

        else:
            print(f"Escolha: {self.escolha} indefinida, tente novamente.")
