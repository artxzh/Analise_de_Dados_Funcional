import pandas as pd
from validations import *
from files_creator import *

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