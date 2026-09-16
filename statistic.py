import pandas as pd
from validations import *


def get_mean(df, string):
#criar uma função para esse loop (Prioridade 3)
  checagem = check_column(df, string)
  while checagem is False:
    print("Essa coluna não existe!")
    string = input("Digite o nome da coluna que deseja acessar: ")
    checagem = check_column(df, string)

  return df[string].mean()

def get_median(df, string):
  checagem = check_column(df, string)
  while checagem is False:
    print("Essa coluna não existe!")
    string = input("Digite o nome da coluna que você deseja acessar: ")
    checagem = check_column(df, string)
    
  return df[string].median()

def get_mode(df, string):
  checagem = check_column(df, string)
  while checagem is False:
    print("Essa coluna não existe!")
    string = input("Digite o nome da coluna que você deseja acessar: ")
    checagem = (df, string)

  return df[string].mode()[0]

def view_medians(list):
  print(
    f"Média: {list[0]} Mediana: {list[1]} Moda: {list[2]}"
  )