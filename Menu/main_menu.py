import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistic import *
from Menu.menu_estatistic import *
from Menu.menu_filtros import *
from files_creator import *

def main_menu():
  while True:
    arquivo = input("Digite o nome do arquivo: ")
    while(check_file("files", arquivo)) == False:
      print("Não existe arquivo com esse nome!")
      arquivo = input("Digite o nome do arquivo: ")
    df = load_csv(arquivo.lower())

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
        menu_estatistic(df)
        break
        
      case 2:
        #filtrar tabela
        menu_filter(df)

      #case 3:
        #análise de faturamento
      #case 4:
        break
