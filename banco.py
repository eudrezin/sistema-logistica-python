import mysql.connector 

def conectar_banco():
    try:
        
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",       
            password="26634462Aw@",  
            database="sistema_logistica"
        )
        return conexao
    except mysql.connector.Error as erro:
        print(f"\n Erro ao conectar ao banco de dados: {erro}")
        print("Verifique se o seu servidor MySQL está ligado e se a senha está correta.")
        return None 