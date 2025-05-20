import tkinter as tk
from tkinter import colorchooser

current_x, current_y = 0, 0
cor = "black"
pen_size = 5

def comecar_posicao(evento):
    global current_x,current_y
    current_x, current_y = evento.x, evento.y

def desenhar_linha(evento):
    global current_x,current_y
    canvas.create_line(current_x,current_y,evento.x,evento.y,
                       fill=cor,width=pen_size, capstyle=tk.ROUND, smooth=True)
    
    current_x, current_y = evento.x, evento.y

def mudar_cor():
    global cor
    nova_cor = colorchooser.askcolor()[1]
    if nova_cor:
        cor = nova_cor
        botao_cor.config(bg=cor)

def limpar_canvas():
    canvas.delete("all")

def mudar_pen_size(new_size):

    global pen_size
    pen_size = new_size

def set_small_pen():

    mudar_pen_size(2)

def set_medium_pen():

    mudar_pen_size(5)

def set_large_pen():
    mudar_pen_size(10)

janela = tk.Tk()
janela.title("App Simples Desenho")
janela.geometry("800x600")

label_titulo = tk.Label(janela, text="App Simples de Desenho", font=("Arial", 16))
label_titulo.pack(pady=10)

toolbar = tk.Frame(janela)
toolbar.pack(fill=tk.X, pady=5)

botao_cor = tk.Button(toolbar, text="Escolha Cor", command=mudar_cor, bg=cor)
botao_cor.pack(side=tk.LEFT, padx=5)

botao_limpar = tk.Button(toolbar, text="Limpar Canvas", command=limpar_canvas)
botao_limpar.pack(side=tk.LEFT, padx=5)

size_frame = tk.Frame(toolbar)
size_frame.pack(side=tk.LEFT, padx=15)

size_label = tk.Label(size_frame,text="Tamanho da Lapiseira:")
size_label.pack(side=tk.LEFT)

botao_pequeno = tk.Button(size_frame,text="Pequeno", command=set_small_pen)
botao_pequeno.pack(side=tk.LEFT, padx=2)


botao_medio = tk.Button(size_frame,text="Médio", command=set_medium_pen)
botao_medio.pack(side=tk.LEFT, padx=2)


botao_grande = tk.Button(size_frame,text="Grande", command=set_large_pen)
botao_grande.pack(side=tk.LEFT, padx=2)

canvas = tk.Canvas(janela, bg="white")
canvas.pack(fill=tk.BOTH, expand=True, padx=10,pady=10)

canvas.bind("<Button-1>", comecar_posicao) # registra o comeco cordenada para o desenho
canvas.bind("<B1-Motion>", desenhar_linha) # isto acompanha movimentos e desenha linhas

instruction_label = tk.Label(janela, text="Clique e arrasta para desenhar", font=("Arial",10))
instruction_label.pack(pady=5)

manufacturer_label = tk.Label(janela, text="Desenvolvido por Wilson Cosmopolita", font=("Arial",10))
manufacturer_label.pack(pady=5)

janela.mainloop()
