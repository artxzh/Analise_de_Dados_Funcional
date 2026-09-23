from statistic import *
from graphs import *
from files_creator import *
from validations import *

def main_menu():
  while True:
    arquivo = input("Digite o nome do arquivo: ")
    while(check_file("files", arquivo)) == False:
      print("Não existe arquivo com esse nome!")
      arquivo = input("Digite o nome do arquivo: ")
    df = load_csv(arquivo.lower())
    
    print("""
      1: Vizualizar média;
      2: Vizualizar mediana;
      3: Vizualizar moda;
      4: Vizualizar todas estatísticas básicas;
      5: Sair do terminal;
    """)

    opcao = int(input("Digite a opção: "))
    match opcao:
      case 1:
        print("Qual coluna você deseja acessar?")
        coluna_mean = input("")
        mean = get_mean(df, coluna_mean)
        

        opcao_mean = int(input("1- Exibir no terminal;\n 2- Retornar novo arquivo;"))
        if opcao_mean == 1:
          print(mean)
        else:
          df_list = [mean]
          nome_arquivo_mean = input("Digite o nome do arquivo que será retornado: ")
          return new_csv(df_list, nome_arquivo_mean)
        break

      case 2:
        print("Qual coluna você deseja acessar?")
        coluna_median = input("")
        median = get_median(coluna_median)
        

        opcao_median = int(input("1- Exibir no termional;\n 2- Retornar novo arquivo"))
        if opcao_median == 1:
          print(median)
        else:
          df_list = [median]
          nome_arquivo_median = input("Digite o nome do arquivo que será retornado: ")
          return new_csv(df_list, nome_arquivo_median)
        break

      case 3:
        print("Qual coluna você deseja acessar?")
        coluna_mode = input("")
        mode = get_mode(df, coluna_mode)

        opcao_mode = int(input("1- Exibir no terminal;\n 2- Retornar novo arquivo"))
        if opcao_mode == 1:
          print(mode)
        else:
          df_list = [mode]
          nome_arquivo_mode = input("Digite o nome do arquivo que será retornado: ")
          return new_csv(df_list, nome_arquivo_mode)
        break

      case 4:
        print("Qual coluna você deseja acessar?")
        coluna_trio = input("")
        mean = get_mean(df, coluna_trio)
        median = get_median(df, coluna_trio)
        mode = get_mode(df, coluna_trio)

        opcao_trio = int(input("1- Exibir no terminal;\n 2- Retornar novo arquivo;\n 3- Gerar grafico de barras;"))
        match opcao_trio:
          case 1:
            print(f"Media: {mean}; Mediana: {median}; Moda: {mode}")
            break

          case 2:
            nome_arquivo_trio = input("Digite o nome do arquivo que será retornado: ")
            
            df_list = [mean, median, mode]
            columns_list = ["Média", "Mediana", "Moda"]
            return new_csv(df_list, columns_list, nome_arquivo_trio)

          case 3:
            bars = ["Mean", "Median", "Mode"]
            values = [mean, median, mode]
            create_graph(bars, values)
            break

      case 5:
        coluna_graph = input(print("Qual coluna você deseja gerar um grafico?: "))

        break