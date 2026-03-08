from database import criar_tabela 
from services import adicionar_despesa, listar_despesas, excluir_despesa

criar_tabela()

def menu():
    while True:

        print("\n=== CONTROLE DE DESPESAS ===")
        print("1 - Adicionar despesa")
        print("2 - Listar despesas")
        print("3 - Excluir despesa")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            valor = float(input("Valor: "))
            categoria = input("Categoria: ")
            descricao = input("Descrição: ")

            adicionar_despesa(valor, categoria, descricao)

            print("Despesa registrada!")

        elif opcao == "2":

            despesas = listar_despesas()

            for d in despesas:
                print(d)

        elif opcao == "3":
            id_despesa = int(input("ID da despesa a excluir: "))
            excluir_despesa(id_despesa)
            print("Despesa excluída!")
                    
        elif opcao == "4":
            break
menu()