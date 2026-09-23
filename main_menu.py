import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistic import *
from menu_estatistica_basica import *

def main_menu(df):
  while True:
    arquivo = input("Digite o nome do arquivo: ")
    while(check_file("files", arquivo)) == False:
      print("Não existe arquivo com esse nome!")
      arquivo = input("Digite o nome do arquivo: ")
    df = load_csv(arquivo.lower())
    df_list = []

    print("""
      1- Funções estatísticas básica
      2- Filtrar tabela
      3- Análise de Faturamento
      4- Sair
    """)

    opcao = int(input("Digite a opção: "))
    match opcao:
      case 1:
        #menu statistica basica
        menu_estatistica_basica(df)
        break
        
      case 2:
        #filtrar tabela
        

      case 3:
        #análise de faturamento
      case 4:
        break