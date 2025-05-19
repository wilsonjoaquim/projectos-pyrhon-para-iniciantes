import tkinter as tk

def calcular_soma():
    try:
        num1 = float(primeiro_numero.get())
        num2 = float(segundo_numero.get())
        resultado = num1 + num2
        label_resultado.config(text=f"Resultado = {resultado}")
    except ValueError:
        label_resultado.config(text="Por favor insiria valores validos")

# criar a janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x250")

label_titulo = tk.Label(janela,text="Calculadora Simples", font=("Arial",14))
label_titulo.pack(pady=10)

quadro1 = tk.Frame(janela)
quadro1.pack(pady=5)

quadro2 = tk.Frame(janela)
quadro2.pack(pady=5)

label_num1 = tk.Label(quadro1,text="Primeiro Numero:")
label_num1.pack(side=tk.LEFT)

label_num2 = tk.Label(quadro2,text="Segundo Numero:")
label_num2.pack(side=tk.LEFT)

primeiro_numero = tk.Entry(quadro1, width=10)
primeiro_numero.pack()

segundo_numero = tk.Entry(quadro2, width=10)
segundo_numero.pack()

botao_calcular = tk.Button(janela, text="Adicionar Numeros", command=calcular_soma)
botao_calcular.pack(pady=10)

label_resultado = tk.Label(janela,text="Resultado: ",font=("Arial",12))
label_resultado.pack(pady=10)

def limpar_campos():
    primeiro_numero.delete(0,tk.END)
    segundo_numero.delete(0,tk.END)
    label_resultado.config(text="Resultado: ")

botao_limpar = tk.Button(janela,text="Limpar",command=limpar_campos)
botao_limpar.pack(pady=5)

janela.mainloop()