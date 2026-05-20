import mysql.connector
from banco import conectar_banco

def cadastrar_carga():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        
        print("\n--- CADASTRO DE NOVA CARGA ---")
        descricao = input("Descrição da mercadoria: ")
        destino = input("Cidade/Estado de destino: ")
        
        comando = "INSERT INTO cargas (descricao_produto, destino) VALUES (%s, %s)"
        valores = (descricao, destino)
        
        try:
            cursor.execute(comando, valores)
            conexao.commit()
            print(f" Carga cadastrada com sucesso! ID da Carga: {cursor.lastrowid}")
        except mysql.connector.Error as erro:
            print(f" Erro ao inserir dados: {erro}")
        
        cursor.close()
        conexao.close()

def listar_cargas():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        
        query = """
            SELECT c.id_carga, c.descricao_produto, c.destino, c.status_envio, m.nome 
            FROM cargas c
            LEFT JOIN motoristas m ON c.id_motorista = m.id_motorista
        """
        try:
            cursor.execute(query)
            resultados = cursor.fetchall()
            
            print("\n=== LISTA DE CARGAS E RESPONSÁVEIS ===")
            if not resultados:
                print("Nenhuma carga encontrada no sistema.")
            else:
                for carga in resultados:
                    motorista = carga[4] if carga[4] else "Sem motorista atribuído"
                    print(f"ID: {carga[0]} | Produto: {carga[1]} | Destino: {carga[2]} | Status: {carga[3]} | Motorista: {motorista}")
                print("=======================================")
        except mysql.connector.Error as erro:
            print(f" Erro ao buscar dados: {erro}")
            
        cursor.close()
        conexao.close()

def atualizar_status_carga():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        
        print("\n--- ATUALIZAR STATUS DA CARGA ---")
        id_carga = input("Digite o ID da carga que deseja atualizar: ")
        
        print("Escolha o novo status:")
        print("1. Em Trânsito")
        print("2. Entregue")
        print("3. Cancelado")
        opcao_status = input("Opção: ")
        
        novo_status = ""
        if opcao_status == "1":
            novo_status = "Em Trânsito"
        elif opcao_status == "2":
            novo_status = "Entregue"
        elif opcao_status == "3":
            novo_status = "Cancelado"
        else:
            print(" Opção inválida!")
            cursor.close()
            conexao.close()
            return

        comando = "UPDATE cargas SET status_envio = %s WHERE id_carga = %s"
        valores = (novo_status, id_carga)
        
        try:
            cursor.execute(comando, valores)
            conexao.commit()
            if cursor.rowcount > 0:
                print(f" Status da carga ID {id_carga} atualizado para '{novo_status}'!")
            else:
                print(" Carga não encontrada com esse ID.")
        except mysql.connector.Error as erro:
            print(f" Erro ao atualizar status: {erro}")
            
        cursor.close()
        conexao.close()

def cadastrar_motorista():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        
        print("\n--- CADASTRO DE MOTORISTA ---")
        nome = input("Nome do Motorista: ")
        placa = input("Placa do Veículo (Ex: ABC1D23): ")
        
        comando = "INSERT INTO motoristas (nome, placa_veiculo) VALUES (%s, %s)"
        valores = (nome, placa)
        
        try:
            cursor.execute(comando, valores)
            conexao.commit()
            print(f" Motorista cadastrado com sucesso! ID: {cursor.lastrowid}")
        except mysql.connector.Error as erro:
            print(f" Erro ao cadastrar motorista: {erro}")
            
        cursor.close()
        conexao.close()

def atribuir_motorista_a_carga():
    conexao = conectar_banco()
    if conexao:
        cursor = conexao.cursor()
        
        print("\n--- ATRIBUIR MOTORISTA A UMA CARGA ---")
        id_carga = input("Digite o ID da carga: ")
        id_motorista = input("Digite o ID do motorista que vai levar a carga: ")
        
        comando = "UPDATE cargas SET id_motorista = %s, status_envio = 'Em Trânsito' WHERE id_carga = %s"
        valores = (id_motorista, id_carga)
        
        try:
            cursor.execute(comando, valores)
            conexao.commit()
            if cursor.rowcount > 0:
                print(f" Motorista {id_motorista} vinculado à carga {id_carga}! Status alterado para 'Em Trânsito'.")
            else:
                print(" Carga não encontrada.")
        except mysql.connector.Error as erro:
            print(f" Erro ao vincular (verifique se os IDs existem): {erro}")
            
        cursor.close()
        conexao.close()