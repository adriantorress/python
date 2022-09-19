'''Ester está programando suas férias e decidiu viajar gastando no máximo R$ 300 de passagens (ida e volta). Para usar bem seu dinheiro, ela quer ir para a cidade mais longe possível sem extrapolar seu orçamento. Escreva um programa que receba como entrada o nome, a distância (em quilômetros) e o valor da passagem (só ida) de várias cidades, até que ela informe a cidade FIM, e exiba o nome do melhor destino para ela.

Obs: Considere que as passagens de ida e de volta tenham o mesmo valor

Formato de entrada

Um String (que pode estar escrito de qualquer forma), um inteiro (km) e um real para cada cidade

Para encerrar a entrada, será informado o String FIM (escrito de qualquer forma) como nome da cidade

Formato de saída

Um String com as letras todas maiúsculas

Se nenhuma cidade for informada, deverá ser exibida a mensagem SEM DESTINO

Exemplos de:

Entrada


Natal
154
135
Recife
104
110
Fim
Saída


NATAL'''


passagem_maxima_ida_volta = 300
localidades = []
maior_valor = 0
viajar_para = ''


while True:
    cidade = input().upper()
    if cidade == 'FIM':
      break
    distancia = int(input())
    passagem_ida = float(input())
    if len(cidade) == 0:
        print('SEM DESTINO')
    local =  (cidade,distancia,passagem_ida*2)
    localidades.append(local)


for cidade in localidades:
  valor = cidade[2]
  if valor > maior_valor and valor <= 300:
    maior_valor = valor
    viajar_para = cidade[0]


print(viajar_para)