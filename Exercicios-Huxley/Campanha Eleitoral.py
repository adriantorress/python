candidatos = []
while True:
    valor = 0
    candidato_e_midia = input().split()
    candidato = candidato_e_midia[0]
    if candidato.upper() == 'FIM':
        break
    midias = candidato_e_midia[1]
    for x in range(int(midias)):
        qual_midia = input()
        if qual_midia == 'internet':
            valor+=3000
        elif qual_midia == 'revista':
            valor+=750
        elif qual_midia == 'outdoor':
            valor+=1500
        elif qual_midia == 'tv':
            horario = int(input())
            if horario<=20:
                valor+=1200
            elif horario>20:
                valor+=2000
        elif qual_midia == 'radio':
            tipo = input()
            if tipo == 'am':
                valor+=300
            elif tipo=='fm':
                valor+=500
    candidatos.append((candidato,valor))

for candidato in candidatos:
    print(f'{candidato[0]}: {candidato[1]:.2f}')

