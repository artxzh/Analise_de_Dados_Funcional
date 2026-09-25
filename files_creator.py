import pandas as pd
from validations import *
from statistic import *

def load_csv(file):
  return pd.read_csv(f"./files/{file}.csv")

#Criar csv com colunas inexistentes
# Arrumar função
def new_csv(df_list, clomuns_list, string):
  new_df = {}
  for i in range(len(df_list)):
    new_df[f"{clomuns_list[i]}"] = [df_list[i]]

  new_df = pd.DataFrame(new_df)

  while(check_file("report", string)) == True:
    print("Já existe um arquivo com esse nome!")
    string = input("Digite um novo nome para o arquivo: ")
    
  return new_df.to_csv(f"./report/{string}.csv", index=False)