import tkinter as tk
from tkinter import messagebox
import json

def add_tarefa():
    
    tarefa = entrada_tarefa.get()

    if tarefa:
        caixa_lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0,tk.END)
        salvar_tarefa()
    else:
        messagebox.showwarning("Warning","Por favor insira uma tarefa")


def eliminar_tarefa():
    try:
        indice_tarefa_selecionada = caixa_lista_tarefas.curselection()[0]

        caixa_lista_tarefas.delete(indice_tarefa_selecionada)

        salvar_tarefa()

    except IndexError:
        messagebox.showwarning("Warning","Por favor selecione uma tarefa a deletar")

def marcar_completada_tarefa():
    
   try:
        indice_tarefa_selecionada = caixa_lista_tarefas.curselection()[0]
        tarefa = caixa_lista_tarefas.get(indice_tarefa_selecionada)

        if tarefa.startswith("✔ "):
            tarefa = tarefa[2:]
        else:
            tarefa = "✔ " + tarefa
        caixa_lista_tarefas.delete(indice_tarefa_selecionada)
        caixa_lista_tarefas.insert(indice_tarefa_selecionada,tarefa)

        salvar_tarefa()
   except IndexError:
        messagebox.showwarning("Warning","Por favor selecione uma tarefa para marcar como completa")


def salvar_tarefa():
    tarefas = caixa_lista_tarefas.get(0, tk.END) 


    with open("tarefas.json","w") as ficheiro:
        json.dump(list(tarefas), ficheiro)

def processar_tarefas():
    try:
        with open("tarefas.json","r") as ficheiro:
            tarefas = json.load(ficheiro)
        for t in tarefas:
            caixa_lista_tarefas.insert(tk.END, t)
    except FileNotFoundError:
        messagebox.showwarning("Warning","Ficheiro não encontrado")

janela = tk.Tk()
janela.title("App Gestor de Tarefas")
janela.geometry("400x450")
janela.resizable(False,False)

label_titulo = tk.Label(janela, text="Lista de Tarefas a Fazer", font=("Arial",16,"bold"))
label_titulo.pack(pady=5)

quadro_input = tk.Frame(janela)
quadro_input.pack(pady=10)

entrada_tarefa = tk.Entry(quadro_input, width=30, font=("Arial",12))
entrada_tarefa.pack(side=tk.LEFT, padx=5)

botao_add = tk.Button(quadro_input,text="Add Tarefa", command=add_tarefa)
botao_add.pack(side=tk.LEFT)

quadro_lista = tk.Frame(janela)
quadro_lista.pack(pady=10, fill=tk.BOTH,expand=True)

scrollbar = tk.Scrollbar(quadro_lista)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

caixa_lista_tarefas = tk.Listbox(quadro_lista, width=45,height=12,font=("Arial",12))
caixa_lista_tarefas.pack(side=tk.LEFT,fill=tk.BOTH, expand=True)

scrollbar.config(command=caixa_lista_tarefas.yview)

quadro_botao = tk.Frame(janela)
quadro_botao.pack(pady=10)

botao_completar = tk.Button(quadro_botao, text="Marcar como completada",command=marcar_completada_tarefa)
botao_completar.pack(side=tk.LEFT, padx=5)

botao_deletar = tk.Button(quadro_botao,text="Deletar Tarefa",command=eliminar_tarefa)
botao_deletar.pack(side=tk.LEFT, padx=5)
janela.mainloop()

processar_tarefas()
