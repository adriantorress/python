def tela_inicial():
    print()
    print('1 - Cadastrar usuário')
    print('2 - Usuários do sistema')
    print('3 - Buscar usuário pelo sexo')
    print('4 - Buscar usuário pelo nome')
    print('5 - Apagar todos os usuários do sistema')
    print('6 - Finalizar')
    print()

    opcao = input('Digite sua opção: ')
    print()

    if opcao == '1':
        return form()
    elif opcao == '2':
        return ler_valores()
    elif opcao == '3':
        sexo = input('Digite o sexo dos usuários a serem mostrados: ')
        return busca_usuario_pelo_sexo(sexo)
    elif opcao == '4':
        nome = input('Digite o nome dos usuários a serem mostrados: ')
        return busca_usuario_pelo_nome(nome)
    elif opcao == '5':
        print('*-*-*-Todos os usuários foram apagados-*-*-*')
        apagar_usuários()
    elif opcao == '6':
        print('*-*-*-Fim do programa-*-*-*')
        print()


def form():
    nome = input('Nome: ')
    idade = input('Idade: ')
    sexo = input('Masculino ou Feminino (M ou F): ')
    telefone = input('Telefone: ')
    valores = nome+'|'+idade+'|'+sexo+'|'+telefone+'\n'
    escrever_valores(valores)
    print()
    print('*-*-*-Usuário cadastrado com sucesso!-*-*-*')
    return tela_inicial()


def escrever_valores(valores):
    try:
        arquivo = open('Exercicios-Leonardo-LNPG/armazenar_dados.txt', 'a')
        arquivo.write(valores)
        arquivo.close()
    except:
        arquivo = open('Exercicios-Leonardo-LNPG/armazenar_dados.txt', 'w')
        arquivo.write(valores)
        arquivo.close()


def ler_valores():
    arquivo = open('Exercicios-Leonardo-LNPG/armazenar_dados.txt', 'r')
    objetos = arquivo.read().split('\n')
    arquivo.close()
    if len(objetos[0]) == 0:
        print('*-*-*-Nenhum usuário cadastrado-*-*-*')
    else:
        print('*-*-*-Usuários do sistema-*-*-*')
        for objeto in objetos:
            try:
                if len(objeto[0]) == 0:
                    pass
                else:
                    valor = objeto.split('|')
                    formatar_objetos(valor)
            except:
                pass
    return tela_inicial()


def busca_usuario_pelo_sexo(sexo):
    arquivo = open('Exercicios-Leonardo-LNPG/armazenar_dados.txt', 'r')
    objetos = arquivo.read().split('\n')
    arquivo.close()
    if len(objetos[0]) == 0:
        print('*-*-*-Nenhum usuário desse sexo cadastrado-*-*-*')
    else:
        print(f'*-*-*-Usuários do sistema do sexo {sexo}-*-*-*')
        for objeto in objetos:
            try:
                if len(objeto[0]) == 0:
                    pass
                else:
                    valor = objeto.split('|')
                    if valor[2] == sexo:
                        formatar_objetos(valor)
                    else:
                        pass
            except:
                pass
    return tela_inicial()


def busca_usuario_pelo_nome(nome_procurado):
    arquivo = open('Exercicios-Leonardo-LNPG/armazenar_dados.txt', 'r')
    objetos = arquivo.read().split('\n')
    arquivo.close()
    if len(objetos[0]) == 0:
        print()
        print('*-*-*-Nenhum usuário encontrado com esse nome-*-*-*')
    else:
        print()
        print(
            f'*-*-*-Usuários do sistema que tem {nome_procurado} no nome-*-*-*')
        for objeto in objetos:
            try:
                if len(objeto[0]) == 0:
                    pass
                else:
                    valor = objeto.split('|')
                    if nome_procurado.lower() in valor[0].lower():
                        formatar_objetos(valor)
                    else:
                        pass
            except:
                pass
    return tela_inicial()


def formatar_objetos(objeto):
    print(f'\nNome: {objeto[0]}')
    print(f'Idade: {objeto[1]}')
    print(f'Sexo: {objeto[2]}')
    print(f'Telefone: {objeto[3]}')


def apagar_usuários():
    arquivo = open('Exercicios-Leonardo-LNPG/armazenar_dados.txt', 'w')
    arquivo.close()
    return tela_inicial()


tela_inicial()
