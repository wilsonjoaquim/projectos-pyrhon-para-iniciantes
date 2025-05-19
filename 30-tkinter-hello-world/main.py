import tkinter as tk

def dizer_ola():
    nome = label_nome.get()
    if nome:
        label_saudacao.config(text=f"Olá, {nome}")
    else:
        label_saudacao.config(text="Olá, Mundo!")

janela = tk.Tk()
janela.title("Minha primeira App Tkinter")
janela.geometry("300x200")

janela.resizable(False,False)

label_titulo = tk.Label(janela, text="Bem vindo ao Tkinter!", font=("Arial",16))
label_titulo.pack(pady=10)

label_nome = tk.Entry(janela, width=20)
label_nome.pack(pady=10)

botao_ola = tk.Button(janela,text="Diga Ola",command=dizer_ola)
botao_ola.pack(pady=10)

label_saudacao = tk.Label(janela, text="", font=("Arial",12))
label_saudacao.pack(pady=10)
janela.mainloop()