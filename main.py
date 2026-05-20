from funcoes import * 

def menu():
    while True:
        print("\n SISTEMA DE LOGÍSTICA MODULAR ")
        print("1. Cadastrar Nova Carga")
        print("2. Listar Todas as Cargas")
        print("3. Atualizar Status de uma Carga")
        print("4. Cadastrar Novo Motorista")        
        print("5. Atribuir Motorista a uma Carga")  
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_carga()
        elif opcao == "2":
            listar_cargas()
        elif opcao == "3":
            atualizar_status_carga()
        elif opcao == "4":
            cadastrar_motorista()
        elif opcao == "5":
            atribuir_motorista_a_carga()
        elif opcao == "6":
            print("\nEncerrando o sistema de logística. Até logo!")
            break
        else:
            print("\n Opção inválida!")

if __name__ == "__main__":
    menu()