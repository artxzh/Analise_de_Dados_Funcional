from statistics.faturmento import *

def menu_faturamento(df):
    while True: 
        print("""
        1- Faturamento Total
        2- Ticket Médio Total
              """)
        opcao = int(input())
        match opcao:
            case 1:
                faturamento = faturamento_total(df)
                print(f"O faturamento total foi de {faturamento}")
                break
            case 2:
                ticket_medio = ticket_medio_total(df)
                print(f"O faturamento total foi de {ticket_medio}")
            
            case 3:
                break