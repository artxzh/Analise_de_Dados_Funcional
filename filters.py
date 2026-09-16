import pandas as pd
from statistic import *
from files_creator import *
from files_creator import *


#Filtrar por colunas
def filter_columns(df, column, parameter, int):
  filter = df[df[column] == parameter]
  if int == 0:
    return filter
  #criar função de nomeação dinâmica (prioridade 3)
  nome_arquivo = input("Digite o nome do arquivo que deseja criar: ")
  return filter.to_csv(f"./report/{nome_arquivo}.csv")

#Filtro pronto do faturamento total
def faturamento_total(df):
  filter = df[df["status"] == "Entregue"]
  valor_total = filter["valor_total"].sum()
  new_csv([valor_total], ["Valor Total"], "Teste")
  return valor_total

# Ticket médio total
def ticket_medio_total(df):
  filter = df[df["status"] == "Entregue"]
  ticket_medio = filter["valor_total"].mean()
  return ticket_medio

# Filtragem de Número Acima e Abaixo
def filter_numbers_under(df, number):
  filter = df[df["valor_total"] < number]
  return filter

def filter_number_above(df, number):
  filter = df[df["valor_total"] > number]
  return filter

