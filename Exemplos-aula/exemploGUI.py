from tkinter import *  # importa tudo da biblioteca tkinter
from tkinter.ttk import Combobox
from uuid import RFC_4122

window = Tk()  # instancia o Tk() pra criar uma janela com o tkinter -- tem outras formas de se criar uma janela
window.title("Welcome nerds")  # titulo da janela
window.geometry('500x300')  # tamanho da janela
window.configure(bg="blue")  # configurar janela


def clicked():
    lbl.configure(text="Button was clicked !!")


lbl = Label(window, text="Ola")
lbl.pack()
'''cada janela é um container de widget... 
componente visual que agrega outros componentes visuais... 
Label é um componente visual, que usando o pack vai ser jogado no meio... 
com o place você consegue definir a posição do componente na tela, porém o mais convencional e mais correto é definir um layout...
grid é um componente que gerencia layout'''

lbl2 = Label(window, text="Hello", fg='red', font=("Helvetica", 16))
lbl2.place(x=60, y=50)

txtfld = Entry(window, text="This is Entry Widget", bd=1)
txtfld.place(x=80, y=150)

data = ("one", "two", "three", "four")
cb = Combobox(window, values=data)
cb.place(x=80, y=175)

lb = Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END, num)
lb.place(x=80, y=200)

# radiobutton
# checkbox

btn = Button(window, text="Click here!", command=clicked)
btn.pack()
window.mainloop()
