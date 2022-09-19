numero_de_jogos = int(input())


for x in range(numero_de_jogos):
    qntdd_numero_senha = input()
    senha = input().split()
    excelente = 0
    bom = 0
    eb = []
    while True:
        chute = input().split()
        if chute == senha:
            break

        for y in range(len(chute)):
            for z in range(len(senha)):
                print(chute[y],chute[z],senha[y],senha[z])
                if chute[y] == senha[y]:
                    excelente +=1
                    print(excelente)
                elif chute[y] == senha[z]:
                    bom+=1
                    print(bom)
        eb1 = (excelente,bom)
        print(eb1)