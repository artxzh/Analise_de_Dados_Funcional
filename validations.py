import pandas as pd
import os

def check_column(df, string):
  if True not in df.columns.isin([string]):
    return False

def check_file(paramer_pasta, nome_arquivo):
  pasta = f"./{paramer_pasta}"
  
  for arquivo in os.listdir(pasta):
    if f"{nome_arquivo}.csv" == arquivo:
      return True

  return False