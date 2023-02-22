# Projeto Sistema de Cotações de Moedas

## Índice

* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-projeto)
* [Funcionalidades](#funcionalidades)
* [Demonstração da Aplicação](#demonstração-da-aplicação)

## Descrição do Projeto

Este projeto consiste em uma aplicação desktop que permite o acesso a informações sobre cotações de moedas. A aplicação utiliza a API AwesomeAPI para obter os dados das moedas e permite ao usuário selecionar a moeda desejada, a data para a qual deseja obter a cotação e a opção de atualizar os dados de uma planilha Excel.

## Status do Projeto

O projeto está em desenvolvimento e ainda não possui todas as funcionalidades implementadas.

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
