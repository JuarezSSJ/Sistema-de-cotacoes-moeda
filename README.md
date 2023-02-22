# Projeto Sistema de Cotações de Moedas

## Índice

* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-projeto)
* [Funcionalidades](#funcionalidades)
* [Demonstração da Aplicação](#demonstração-da-aplicação)

## Descrição do Projeto

Este projeto consiste em uma aplicação desktop que permite o acesso a informações sobre cotações de moedas. A aplicação utiliza a API AwesomeAPI para obter os dados das moedas e permite ao usuário selecionar a moeda desejada, a data para a qual deseja obter a cotação e a opção de atualizar os dados de uma planilha Excel.

## Status do Projeto

O projeto está em desenvolvimento e ainda não possui todas as funcionalidades implementadas. Já estou estudando para implementar um botão para gerar uma análise para saber qual a moeda mais rentável para investimento

## Funcionalidades

* Seleção de moeda: o usuário pode selecionar a moeda desejada a partir de uma lista suspensa.
* Seleção de data: o usuário pode selecionar a data para a qual deseja obter a cotação por meio de um calendário.
* Consulta de cotação: ao selecionar a moeda e a data, o usuário pode consultar a cotação da moeda para o dia selecionado.
* Atualização de dados: o usuário pode atualizar os dados de uma planilha Excel com as cotações das moedas para um período de tempo selecionado.

## Demonstração da Aplicação

Para utilizar a aplicação, é necessário ter instalado o Python e as bibliotecas `tkinter`, `ttk`, `tkcalendar`, `pandas`, `requests` e `numpy`. Em seguida, basta executar o seguinte código:

```python
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter.filedialog import askopenfilename
import pandas as pd
import requests
from datetime import datetime
import numpy as np

# código da aplicação aqui
```

Uma vez executado o código, a janela da aplicação será exibida e o usuário poderá selecionar a moeda e a data para consulta de cotação ou selecionar uma planilha Excel para atualização dos dados.

![Tela](https://github.com/JuarezSSJ/Sistema-de-cotacoes-moeda/blob/main/Img/Tela.png?raw=true)

A interface é composta por alguns componentes, como rótulos (labels), comboboxes e calendários, que permitem selecionar datas e moedas específicas. Ao selecionar uma moeda e uma data, o usuário pode obter a cotação correspondente, que é exibida em um rótulo na tela. Além disso, há um botão "Atualizar Cotações" que permite atualizar as cotações de várias moedas de uma vez, com base em um arquivo Excel selecionado pelo usuário.

![Cotação Individual](https://github.com/JuarezSSJ/Sistema-de-cotacoes-moeda/blob/main/Img/Cota%C3%A7%C3%A3o%20individual.png?raw=true)

* Cotação Individual

![Varias Cotação e Seleção de arquivo](https://github.com/JuarezSSJ/Sistema-de-cotacoes-moeda/blob/main/Img/Atualiza%C3%A7%C3%A3o%20em%20arquivo.png?raw=true)

* Seleção de arquivo em excel para cotações de varias moedas - utilizando pandas

![Arquivo selecionado](https://github.com/JuarezSSJ/Sistema-de-cotacoes-moeda/blob/main/Img/excel%20para%20multiplas%20cota%C3%A7%C3%B5es.png?raw=true)

* Arquivo Selecionado

![Novo Arquivo Já com as Cotações](https://github.com/JuarezSSJ/Sistema-de-cotacoes-moeda/blob/main/Img/excel%20organizado%20e%20salvo.png?raw=true)

* Novo Arquivo Salvo e já organizado utilizando pandas
