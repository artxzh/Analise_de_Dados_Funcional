import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistic import *

def create_graph(x, y):
  bars = np.array(x)
  values = np.array(y)

  plt.bar(bars, values)
  print("""Deseja criar um arquivo para o gráfico?
    1: Sim
    2: Não
  """)
  check = input("")
  if check == 1:
    nome_arquivo = input("Digite o nome do arquivo: ")
    plt.savefig(f"./report/{nome_arquivo}.png")
  plt.show()