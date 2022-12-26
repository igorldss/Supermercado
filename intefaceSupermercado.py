from funcoesSupermercado import *
from tkinter import *
from tkinter import ttk

def imprimir():
    pass

fundoTela = '#35a1c5'
fundoBotao = '#022a5e'
letra = 'white'
fonte = 'Arial 16'

janela = Tk()
janela.geometry("500x500")
janela.configure(background=fundoTela)
janela.title("Lista de Fornecedores e Produtos")


texto_inicial = Label(janela, text="Lista de fornecedores",background=fundoTela,foreground=fundoBotao)
texto_inicial.place(x=10, y=10, width=150, height=30)

#---------------------------------------------------------------------------------

lb_fornecedores = Listbox(janela)
lb_fornecedores.place(x=50, y=100, width=150, height=30)

botao_fornecedores = Button(janela, text="Fornecedores",command=verforn)
botao_fornecedores.place(x=50, y=50, width=150, height=30)


janela.mainloop()