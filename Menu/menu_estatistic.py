from Analise_de_Dados_Funcional.statistics.statistic import *

def menu_estatistic(df):
  while True:
    print("""
      1- Média
      2- Mediana
      3- Moda
      4- Estatísticas Básicas
      5- Sair do Terminal
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
        if opcao_median == 1:
          print(median)
        elif opcao_median == 2:
          df_list = [median]
          nome_arquivo_median = input("Digite o nome do arquivo que será retornado: ")
          return new_csv(df_list, nome_arquivo_median)
        break

      case 3:
        mode = get_mode(df, coluna)
        opcao_mode = int(input("1- Exibir no terminal;\n 2- Retornar novo arquivo;"))
        if opcao_mode == 1:
          print(mode)
        elif opcao_mean == 2:
          df_list = [mode]
          nome_arquivo_mode = input("Digite o nome do arquivo que será retornado: ")
          return new_csv(df_list, nome_arquivo_mode)
        break
      
      #Todas as 3 estatísticas básicas
      case 4:
        mean = get_mean(df)
        median = get_median(df)
        mode = get_mode(df)
        df_list = [mean, median, mode]
        view_medians(df_list)

      case 5:
        break