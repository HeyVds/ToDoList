import tkinter as tk
from funcoes import *

verificar_arquivo() # Garante que o caminho existe
tarefas = carregar_tarefas() # Carrega o dicionário caso exista, senão, apenas retorna um dicionário vazio

#Janela principal da interface grafica
janela = tk.Tk() 
janela.title("To Do List") #Titulo da janela
janela.geometry("400x300") #Tamanho da janela
janela.configure(bg="#001F3F") #Background da janela

# Frame para adicionar as tarefas 
frame_add_tarefa = tk.Frame(janela,  bg="#001F3F") #
frame_add_tarefa.pack(pady=10)

label = tk.Label(frame_add_tarefa, text="Digite a tarefa:", bg="#001F3F", fg="#FFF", font=("Arial", 10, "bold")) #Texto
label.pack(side="left", padx=5)

entrada = tk.Entry(frame_add_tarefa, width=20,  bg="#1F4E78", fg="#FFF", bd=2, relief="groove") # Campo de entrada de texto
entrada.pack(side="left", padx=5)

botao = tk.Button(frame_add_tarefa, bg="lightgreen", text="Adicionar Tarefa", font=("Arial", 10, "bold"), command = lambda:criar_tarefa(tarefas, entrada,frame_tarefas)) # Botão para adicionar tarefas
botao.pack(side="left", padx=5)

#==========================================#

#frame para exibir as tarefas
frame_tarefas = tk.Frame(janela, bg="#001F3F")
frame_tarefas.pack(pady=10)

atualizar_visualizacao(frame_tarefas, tarefas) #Exibe as tarefas assim que o programa é executado(caso exista)



janela.mainloop() #Mantém o programa rodando
