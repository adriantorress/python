import sys
sys.setrecursionlimit(5000)

numero = int(input())
casa = 1
contar_jogadas = 1

def ate_o_fim(quantidade, atual, contador):
    dado = [1, 2, 3, 4, 5, 6]
    if 10001 > quantidade > 3:
        for x in dado:
            atual += x
            if atual > quantidade:
                atual -= quantidade
            if atual != quantidade and atual < quantidade:
                contador += 1
            else:
                return contador
        return ate_o_fim(quantidade, atual, contador)


print(ate_o_fim(numero, casa, contar_jogadas))
