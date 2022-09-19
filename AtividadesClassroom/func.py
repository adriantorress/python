from tkinter import *


# Volta para a tela inicial
def back_to_home():
    delete_screen.pack_forget()
    users_screen.pack_forget()
    register_screen.pack_forget()
    home.pack(fill="both", expand=True)


# Botão para voltar para a homescreen
def button_home(screen, back_to_home):
    button = Button(screen, text='Voltar',
                    width='10', bg='white', fg='#6E326B', cursor="hand2", command=back_to_home, bd=2)
    button.place(x=315, y=380, height='30')
