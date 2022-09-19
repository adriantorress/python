from tkinter import *
from main import *


# Função para formatar os valores de uma instancia dos objetos salvos
def instance_format(value):
    print(f"\nNome: {value[0]}")
    lbl = Label(users_screen, bg='white', text=f"\nNome: {value[0]}")
    lbl.pack()
    print(f"\nCPF: {value[0]}")
    lbl2 = Label(users_screen, bg='white', text=f"\nCPF: {value[1]}")
    lbl2.pack()
    print(f"\nMátricula: {value[0]}")
    lbl3 = Label(users_screen, bg='white', text=f"\nMátricula: {value[2]}")
    lbl3.pack()
    print(f"\nNome: {value[0]}")
    lbl4 = Label(users_screen, bg='white',
                 text=f"\nData de nascimento: {value[3]}")
    lbl4.pack()


# Função para salvar os valores no arquivo
def write_values(values):
    try:
        file = open("users.txt", "a", encoding='utf-8')
        file.write(values)
        file.close()
    except:
        file = open("users.txt", "w", encoding='utf-8')
        file.write(values)
        file.close()


# Lê os valores do arquivo
def read_values():
    try:
        file = open("users.txt", 'r', encoding='utf-8')
        objects = file.read().split('\n')
        file.close()
        if len(objects[0]) == 0:
            print("Nenhum usuário cadastrado")
            lbl = Label(users_screen, bg='white',
                        text="Nenhum usuário cadastrado")
            lbl.place(x=275, y=20)
        else:
            print("Usuários cadastrados no sistema")
            lbl2 = Label(users_screen, bg='white',
                         text="Usuários cadastrados no sistema")
            lbl2.pack()
            for instance in objects:
                print(instance)
                try:
                    if len(instance[0]) == 0:
                        pass
                    else:
                        value = instance.split(',')
                        instance_format(value)
                except:
                    pass
    except:
        lbl3 = Label(users_screen, bg='white',
                     text="Nenhum usuário cadastrado")
        lbl3.grid(x=210, y=330)


# Funcão para pegar o valor das variáveis ao apertar o botão
def save_info():
    instance = name.get()+","+cpf.get()+","+registration.get() + \
        "," + birth_date.get()
    instance_values = instance.split(",")
    for value in instance_values:
        if value == "":
            instance_values.remove(value)
    if len(instance_values) != 4:
        print("Algum dado incorreto, tente novamente")
        lbl = Message("Algum dado incorreto, tente novamente")
        delete_entry_values()

    else:
        instance = ",".join(instance_values)
        instance = instance + ("\n")
        print(instance)
        write_values(instance)
        print("O usuário " + name.get() + " foi cadastrado com sucesso")
        lbl = Label(register_screen,
                    text="O usuário " + name.get() + " foi cadastrado com sucesso", bg='white', font=("Roboto"), wraplength=275, width=31)
        lbl.place(x=210, y=310)
        delete_entry_values()
