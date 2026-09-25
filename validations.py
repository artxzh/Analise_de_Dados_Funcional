import pandas as pd
import os

def check_column(df, string):
  if True not in df.columns.isin([string]):
    return 

def check_parameter(df, column, parameter):
  checked = df[column].isin([parameter]).any()
  return checked

def validate_column(df):
  string = input("Digite a coluna que você deseja acessar: ")
  while check_column(df, string) is False:
    print("Essa coluna não existe no seu arquivo")
    string = input("Digite a coluna que você deseja acessar: ")
  return string

def check_file(paramer_pasta, nome_arquivo):
  pasta = f"./{paramer_pasta}"
  
  for arquivo in os.listdir(pasta):
    if f"{nome_arquivo}.csv" == arquivo:
      return True

  return False