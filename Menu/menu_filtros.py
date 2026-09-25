from filters import *
from validations import *

def menu_filter(df_):
  while True:
    print("""
      1- Filtrar por coluna;
      2- Filtrar por número
      3- Sair
    """)

    opcao = int(input("Digite a opçao que você deseja acessar: "))

    match opcao:
      case 1:
        column = validate_column(df_)
        parameter = validate_parameter(column)
        break
        
      #case 2:

      #case 3:

