from tkinter import *
from func import *
from fileFunc import *
from navFunc import *


# Atribuindo à variável screen a tela do tkinter
screen = Tk()

# Titulo da tela
screen.title("Formulário Python")

# Tamanho da tela
screen.geometry('700x500')
screen.configure(bg='white')
screen.resizable(False, False)

# Configurando um cabeçalho
heading = Label(screen, text='Formulário Python', fg='#6E326B',
                height='2', font=("Roboto", "20", "bold"), bg='white')
heading.pack()

# Tela de cadastro do usuário
register_screen = Frame(screen)
register_screen.configure(bg='white')

# Tela de usuários do sistema
users_screen = Frame(screen)
users_screen.configure(bg='white')

# Tela inicial
home = Frame(screen)
home.configure(bg='white')

delete_screen = Frame(screen)
delete_screen.configure(bg='white')

# Botão cadastrar da tela inicial
user_register = Button(home, text="Cadastrar usuário",  width='30',
                       bg='white', fg='#6E326B', bd=3, font=("Roboto", "14", "bold"), command=load_register_screen)
user_register.place(x=163, y=10)

# Botão, para procurar usuários, da tela inicial
system_users = Button(home, text="Usuários do sistema",  width='30',
                      bg='white', fg='#6E326B', bd=3, font=("Roboto", "14", "bold"), command=load_users_screen)
system_users.place(x=163, y=80)

# Botão, para procurar usuários, da tela inicial
delete_users = Button(home, text="Remover usuários",  width='30',
                      bg='white', fg='#6E326B', bd=3, font=("Roboto", "14", "bold"), command=load_delete_screen)
delete_users.place(x=163, y=150)

# Label com os textos das variáveis
name_text = Label(register_screen, text='Nome', bd='1', bg='white',
                  fg='#6E326B', font=("Roboto", "11"))
cpf_text = Label(register_screen, text='CPF', bd='1', bg='white',
                 fg='#6E326B', font=("Roboto", "11"))
registration_text = Label(register_screen, text='Matrícula', bd='1',
                          bg='white', fg='#6E326B', font=("Roboto", "11"))
birth_date_text = Label(register_screen, text='Data de nascimento',
                        bd='1', bg='white', fg='#6E326B', font=("Roboto", "11"))

# Posicionando as Labels com place, x afasta da lateral e y do topo
name_text.place(x=80, y=30)
cpf_text.place(x=370, y=30)
registration_text.place(x=80, y=140)
birth_date_text.place(x=370, y=140)

# Variáveis (com seus tipos) para armazenamento dos dados das entradas
name = StringVar(register_screen)
cpf = StringVar(register_screen)
registration = StringVar(register_screen)
birth_date = StringVar(register_screen)

# Recebendo as entradas e armazenando nas variáveis
name_entry = Entry(register_screen, textvariable=name, width='28',
                   bg='#D461CE', fg='white', bd=1, font='14')
cpf_entry = Entry(register_screen, textvariable=cpf, width='28', bg='#D461CE',
                  fg='white', bd=1, font='14')
registration_entry = Entry(register_screen, textvariable=registration,
                           width='28', bg='#D461CE', fg='white', bd=1, font='14')
birth_date_entry = Entry(register_screen, textvariable=birth_date,
                         width='28', bg='#D461CE', fg='white', bd=1, font='14')

# Posicionando as entradas
name_entry.place(x=82, y=55, height='60')
cpf_entry.place(x=372, y=55, height='60')
registration_entry.place(x=82, y=165, height='60')
birth_date_entry.place(x=372, y=165, height='60')

# Botão para registrar as entradas
register = Button(register_screen, text='Cadastrar',
                  width='40', bg='white', fg='#6E326B', cursor="hand2", command=save_info, bd=2)
register.place(x=208, y=255, height='40')

# Botão para voltar para a tela inicial
button_home(register_screen, back_to_home)
button_home(users_screen, back_to_home)
button_home(delete_screen, back_to_home)

# Inicia o programa chamando a tela inicial
home.pack(fill="both", expand=True)
screen.mainloop()
