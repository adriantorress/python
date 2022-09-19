from tkinter import *


# Vai parar a tela de cadastro


def load_register_screen():
    home.pack_forget()
    register_screen.pack(fill="both", expand=True)
    delete_entry_values()


# Vai para a tela dos usuários do sistema
def load_users_screen():
    read_values()
    home.pack_forget()
    users_screen.pack(fill="both", expand=True)


# Vai para a tela de remoção de usuários
def load_delete_screen():
    home.pack_forget()
    delete_screen.pack(fill="both", expand=True)


# Volta para a tela inicial
def back_to_home():
    delete_screen.pack_forget()
    users_screen.pack_forget()
    register_screen.pack_forget()
    home.pack(fill="both", expand=True)
