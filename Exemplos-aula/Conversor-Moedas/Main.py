from API import Conversor_de_moedas


class Main:
    def __init__(self):
        print("\n**Conversor de moedas**\n\n\
    1 - Converter Real para Dólar\n\
    2 - Converter Real para Euro\n\
    3 - Converter Real para Bitcoin")

        escolha = int(input("\nEscolha: "))
        real = float(input("Valor em real a ser convertido: "))
        conversor = Conversor_de_moedas(escolha, real)
        conversor.converter()


if __name__ == "__main__":
    Main()
