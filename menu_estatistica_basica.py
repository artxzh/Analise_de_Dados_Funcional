from statistic import *

def menu_estatistica_basica(df):
  while True:
    print("""
      1- Média
      2- Mediana
      3- Moda
      4- Sair do Terminal
    """)
    opcao = int(input("Escolha a opção:"))
    coluna = input("Digite a que coluna você deseja acessar: ")
    df_list = []
    
    match opcao:
      case 1:
        mean = get_mean(df, coluna)
        opcao_mean = int(input("1- Exibir no terminal;\n 2- Retornar novo arquivo;"))
        if opcao_mean == 1:
          print(mean)
        elif opcao_mean == 2:
          df_list = [mean]
          nome_arquivo_mean = input("Digite o nome do arquivo que será retornado: ")
          return new_csv(df_list, nome_arquivo_mean)
        break

      case 2:
        median = get_median(df, coluna)
        opcao_median = int(input("1- Exibir no terminal;\n 2- Retornar novo arquivo;"))
        if opcao_mean == 1:
          print(median)
        elif opcao_mean == 2:
          df_list = [median]
          nome_arquivo_median = input("Digite o nome do arquivo que será retornado: ")
          return new_csv(df_list, nome_arquivo_median)
        break

      case 3:
        mode = get_mode(df, coluna)
        opcao_median = int(input("1- Exibir no terminal;\n 2- Retornar novo arquivo;"))
        if opcao_mean == 1:
          print(median)
        elif opcao_mean == 2:
          df_list = [median]
          nome_arquivo_median = input("Digite o nome do arquivo que será retornado: ")
          return new_csv(df_list, nome_arquivo_median)
        break
    break