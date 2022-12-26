import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


lista_moedas = ["USD", "EUR"]

janela = tk.Tk()

janela.title("Sistema de Cotações de Moedas")

label_cotacao_unid = tk.Label(
    text="Cotações de Moedas", bg="grey", foreground="white", borderwidth=3, relief="solid")
label_cotacao_unid.grid(row=0, column=0, columnspan=3,
                        padx=10, pady=10, sticky="nsew")
# padx=10, pady=10 - distançia superior e anterior

label_selecionar_moeda = tk.Label(
    text="Selecione a moeda que deseja consultar: ", anchor="e")
label_selecionar_moeda.grid(
    row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

combobox_selecionar_moedas = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moedas.grid(
    row=1, column=2, padx=10, pady=10, sticky="nsew")

label_selecionar_data = tk.Label(
    text="Selecione a data que deseja consultar a cotação: ", anchor="e")
label_selecionar_data.grid(
    row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

calendario_moeda = DateEntry(year=2022, locale='pt_br')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

label_cotacao_unid = tk.Label(text="")
label_cotacao_unid.grid(row=3, column=0, columnspan=2)


def pegar_cotacao():
    label_cotacao_resultado = tk.Label(text="Aqui")
    label_cotacao_resultado.grid(row=3, column=0, columnspan=2, sticky="nsew")
    pass


botao_pg_cotacao = tk.Button(
    text="Pegar Cotação", command=pegar_cotacao, borderwidth=1, relief="solid")
botao_pg_cotacao.grid(row=3, column=2, padx=10, pady=10)


# cotação de varias moedas

label_cotacao_multi = tk.Label(text="Cotações de Multiplas Moedas",
                               bg="grey", foreground="white", borderwidth=3, relief="solid")
label_cotacao_multi.grid(row=4, column=0, columnspan=3,
                         padx=10, pady=10, sticky="nsew")


label_selecionar_arq = tk.Label(
    text="Selecione um arquivo em Execel com as Moedas na Coluna A: ")
label_selecionar_arq.grid(row=5, column=0, columnspan=2, sticky="nsew")


def selecionar_arq():
    pass


botao_selecionar_arq = tk.Button(
    text="Clique para Selecionar", command=selecionar_arq, borderwidth=1, relief="solid")
botao_selecionar_arq.grid(row=5, column=2, padx=10, pady=10)

label_arquivo_selecionado = tk.Label(
    text="Nenhum Arquivo Selecionado", anchor="e")
label_arquivo_selecionado.grid(
    row=6, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

label_data_inicial = tk.Label(text="Data Inicial: ", anchor="e")
label_data_inicial.grid(row=7, column=0)

calendario_data_inicial = DateEntry(year=2022, locale='pt_br')
calendario_data_inicial.grid(row=7, column=1, padx=10, pady=10, sticky="nsew")

label_data_final = tk.Label(text="Data Inicial: ", anchor="e")
label_data_final.grid(row=8, column=0)

calendario_data_final = DateEntry(year=2022, locale='pt_br')
calendario_data_final.grid(row=8, column=1, padx=10, pady=10, sticky="nsew")


def atualizar_cotacoes():
    pass


botao_Atualizar_Cotacoes = tk.Button(
    text="Atualizar Cotações", command=atualizar_cotacoes, borderwidth=1, relief="solid")
botao_Atualizar_Cotacoes.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")

label_arquivo_atualizado = tk.Label(text="")
label_arquivo_atualizado.grid(row=9, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

botao_fechar = tk.Button(text="Fechar", command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky="nsew")

janela.mainloop()
