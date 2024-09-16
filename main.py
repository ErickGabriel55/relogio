# parei no minuto 18:16 Lilizok4 ASMR
import tkinter as tk
from tkinter import *
import os
from time import strftime

def get_saudacao():
    nome_usuario = os.getlogin()
    saudacao.config(text=f'Olá {nome_usuario}')


def get_data():
    data_atual = strftime('%a, %d %b %Y')
    data.config(text=data_atual)

def get_horas():
    hora_atual = strftime('%H:%M:%S')
    horas.config(text=hora_atual)
    horas.after(1000, get_horas)
    

cor_fundo = '#1d1d1d' # cor de fundo da tela do relogio (preta, basicamente)
cor_letra_saudacao = '#0000d4'



tela = tk.Tk() # inicialização da tela
tela.title('Relógio')
tela.geometry('600x320') # tamanho da tela
tela.maxsize(600, 320) # define um tamanho maximo para que o usuario não possa alterar o tamanho da mesma
tela.minsize(600, 320)# define um tamanho minimo para que o usuario não possa alterar o tamanho da mesma
tela.configure(background=cor_fundo) # define a cor de fundo
tela2 = tk.Canvas(tela, width=600, height=60,bg=cor_fundo, bd=0, highlightthickness=0, relief='ridge')
tela2.pack()



saudacao = Label(tela, bg=cor_fundo,fg=cor_letra_saudacao, font=('Montserrat Thin Regular', 16))
saudacao.pack()

data = Label(tela, bg=cor_fundo,fg=cor_letra_saudacao, font=('Montserrat Thin Regular', 14))
data.pack(pady=2)

horas = Label(tela, bg=cor_fundo, fg=cor_letra_saudacao, font=('Montserrat Thin Regular', 64, 'bold'))
horas.pack(pady=2)
get_horas()


get_saudacao()
get_data()



tela.mainloop()