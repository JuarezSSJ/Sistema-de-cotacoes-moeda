import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


lista_moedas = ["USD", "EUR"]

janela = tk.Tk()

janela.title("Sistema de Cotações de Moedas")

label_cotação_unid = tk.Label(
    text="Cotações de Moedas", bg="grey", foreground="white", borderwidth=3, relief="solid")
label_cotação_unid.grid(row=0, column=0, columnspan=3,
                        padx=10, pady=10, sticky="nsew")
# padx=10, pady=10 - distançia superior e anterior

label_selecionar_moeda = tk.Label(
    text="Selecione a moeda que deseja consultar: ")
label_selecionar_moeda.grid(
    row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

combobox_selecionar_moedas = ttk.Combobox(values=lista_moedas)
combobox_selecionar_moedas.grid(
    row=1, column=2, padx=10, pady=10, sticky="nsew")

label_selecionar_data = tk.Label(
    text="Selecione a data que deseja consultar a cotação: ")
label_selecionar_data.grid(
    row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

calendario_moeda = DateEntry(year=2022, locale="pt-br")
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")


def pegar_cotacao():
    pass


botao_pg_cotacao = tk.Button(
    text="Pegar Cotação", command=pegar_cotacao, borderwidth=1, relief="solid")
botao_pg_cotacao.grid(row=3, column=2)


# cotação de varias moedas

label_cotação_multi = tk.Label(text="Cotações de Multiplas Moedas",
                               bg="grey", foreground="white", borderwidth=3, relief="solid")
label_cotação_multi.grid(row=4, column=0, columnspan=3,
                         padx=10, pady=10, sticky="nsew")


def selecionar_arq():
    pass


botao_selecionar_arq = tk.Button(
    text="Clique para Selecionar", command=selecionar_arq, borderwidth=1, relief="solid")
botao_selecionar_arq.grid(row=6, column=2)


janela.mainloop()
