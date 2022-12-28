import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd
import requests
from datetime import datetime
import numpy as np

# conectando com api, para pegar as moedas
requisicao = requests.get("https://economia.awesomeapi.com.br/json/all")
# o arquivo devolvido pelo site é um json, com isso fica melhora para trabalhar se transformar em dicionario
dicionario_moedas = requisicao.json()

# pegando as moedas que são as chaves do dicionario e transformando em lista
# para ser usada na lista suspensa
lista_moedas = list(dicionario_moedas.keys())


def pegar_cotacao():
    moeda_cotacao = combobox_selecionar_moedas.get()
    data_cotacao = calendario_moeda.get()
    data = data_cotacao[:2]
    mes = data_cotacao[3:5]
    ano = data_cotacao[6:]
    link = f"https://economia.awesomeapi.com.br/json/daily/{moeda_cotacao}-BRL/?start_date={ano}{mes}{data}&end_date={ano}{mes}{data}"
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_cotacao_unid['text'] = f"A cotação da {moeda_cotacao} no dia {data_cotacao} foi de: R${valor_moeda}"


def selecionar_arq():
    endereco_arq = askopenfilename(
        title="Selecione um arquivo em Excel para abrir:")
    var_caminhoarquivo.set(endereco_arq)
    if endereco_arq:
        label_arquivo_selecionado["text"] = f"Arquivo Selecionado: {endereco_arq}"


def atualizar_cotacoes():

    try:
        # ler o dataframe de moedas
        df = pd.read_excel(var_caminhoarquivo.get())
        moedas = df.iloc[:, 0]
        # pegar a data de inicio e data de fim das cotacoes
        data_inicial = calendario_data_inicial.get()
        data_final = calendario_data_final.get()
        ano_inicial = data_inicial[-4:]
        mes_inicial = data_inicial[3:5]
        dia_inicial = data_inicial[:2]

        ano_final = data_final[-4:]
        mes_final = data_final[3:5]
        dia_final = data_final[:2]

        for moeda in moedas:
            link2 = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano_inicial}{mes_inicial}{dia_inicial}&end_date={ano_final}{mes_final}{dia_final}"
            # link = f"https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?" \
            # f"start_date={ano_inicial}{mes_inicial}{dia_inicial}&" \
            # f"end_date={ano_final}{mes_final}{dia_final}"

            requisicao_moeda = requests.get(link2)
            cotacoes = requisicao_moeda.json()
            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in df:
                    df[data] = np.nan

                df.loc[df.iloc[:, 0] == moeda, data] = bid
        df.to_excel("Teste.xlsx")
        label_arquivo_atualizado['text'] = "Arquivo Atualizado com Sucesso"
    except:
        label_arquivo_atualizado['text'] = "Selecione um arquivo Excel no Formato Correto"


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
label_cotacao_unid.grid(row=3, column=0, columnspan=2, sticky="nsew")


botao_pg_cotacao = tk.Button(
    text="Pegar Cotação", command=pegar_cotacao, borderwidth=1, relief="solid")
botao_pg_cotacao.grid(row=3, column=2, padx=10, pady=10)


# cotação de varias moedas

label_cotacao_multi = tk.Label(text="Cotações de Multiplas Moedas",
                               bg="grey", foreground="white", borderwidth=3, relief="solid")
label_cotacao_multi.grid(row=4, column=0, columnspan=3,
                         padx=10, pady=10, sticky="nsew")
var_caminhoarquivo = tk.StringVar()

label_selecionar_arq = tk.Label(
    text="Selecione um arquivo em Execel com as Moedas na Coluna A: ")
label_selecionar_arq.grid(row=5, column=0, columnspan=2, sticky="nsew")

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

label_data_final = tk.Label(text="Data Final: ", anchor="e")
label_data_final.grid(row=8, column=0)

calendario_data_final = DateEntry(year=2022, locale='pt_br')
calendario_data_final.grid(row=8, column=1, padx=10, pady=10, sticky="nsew")

botao_Atualizar_Cotacoes = tk.Button(
    text="Atualizar Cotações", command=atualizar_cotacoes, borderwidth=1, relief="solid")
botao_Atualizar_Cotacoes.grid(row=9, column=0, padx=10, pady=10, sticky="nsew")

label_arquivo_atualizado = tk.Label(text="")
label_arquivo_atualizado.grid(
    row=9, column=1, columnspan=2, padx=10, pady=10, sticky="nsew")

botao_fechar = tk.Button(text="Fechar", command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky="nsew")

janela.mainloop()
