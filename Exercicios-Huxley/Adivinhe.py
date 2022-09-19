numero_de_jogos = int(input())
eb = []

for x in range(numero_de_jogos):
    tamanho_senha = int(input())
    if tamanho_senha == 0:
        break
    senha = input()
    valores_senha = []

    for x in senha:
        valores_senha.append(x)

    if len(valores_senha) == tamanho_senha:
        while True:
            chute = input()
            valores_chute = []
            excelente = 0
            bom = 0

            for x in chute:
                valores_chute.append(x)

            if len(valores_chute) != tamanho_senha:
                break

            if valores_chute.count('0') == tamanho_senha:
                break

            else:
                posicoes_boas = []
                for posicao in range(len(valores_senha)):
                    if valores_senha[posicao] == valores_chute[posicao]:
                        excelente += 1
                    elif valores_senha[posicao] != valores_chute[posicao] and valores_chute[posicao] in valores_senha and posicao not in posicoes_boas:
                        bom += 1
                        posicoes_boas.append(posicao)

            eb1 = (excelente, bom)
            eb.append(eb1)

            if valores_senha == valores_chute:
                break

    else:
        break

for valor, valor2 in eb:
    print(f'({valor},{valor2})')
