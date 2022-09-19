leeet = [['a','A','@'],['e','E','3'],['i','I','1'],['o','O','0'],['t','T','7'],['s','S','5']]
frase = input()
frase_quebrada = []
contador = 0

def analise(lista_quebrada,leet,cont):

    for x in frase_quebrada:
        if x.isnumeric() == True:
            print('numeros')
            return 0
    if len(frase_quebrada) == 0:
        print('vazio')
        return cont
    else:
        for y in range(len(leet)):
            for x in range(len(frase_quebrada)):
                if frase_quebrada[x] in leet[y]:
                    frase_quebrada[x] = leet[y][2]
                    cont+=1
        frase_quebrada.reverse()
        print(''.join(frase_quebrada))
        return cont

for x in frase:
    frase_quebrada.append(x)

print(analise(frase_quebrada,leeet,contador))