from statistic import *

def menu_estatistic(df):
  while True:
    print("""
      1- Média
      2- Mediana
      3- Moda
      4- Faturamento Total
      5- Ticket Médio Total
      6- Sair do Terminal
    """)
    opcao = int(input("Escolha a opção:"))
    if 0 < opcao < 4:
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
        opcao_mode = int(input("1- Exibir no terminal;\n 2- Retornar novo arquivo;"))
        if opcao_mode == 1:
          print(mode)
        elif opcao_mean == 2:
          df_list = [mode]
          nome_arquivo_mode = input("Digite o nome do arquivo que será retornado: ")
          return new_csv(df_list, nome_arquivo_mode)
        break

      case 4:
        faturamento = faturamento_total(df)
        print(f"O faturamento total foi de R${faturamento}")

      case 5:
        ticket_medio = ticket_medio_total(df)
        print(f"O Ticket médio total foi de R${ticket_medio}")

      case 6:
        break