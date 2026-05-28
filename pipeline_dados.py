# Importando a ferramenta de banco de dados relacional 
#sqlite3 cria esse banco de dados 
import sqlite3

def executar_pipeline_etl():
    print("\n==============================================")
    print("INICIANDO PIPELINE DE ENGENHARIA DE DADOS")
    print("\n==============================================")

    # Dados brutos
    dados_brutos = [
        ("Daniel Sousa", "danielsousa1234@gmail.com", "Tech", "R$ 5000"),
        ("Ana Gabriela", "ana.silva@email.com", "financeiro", "R$3000"),
        ("Carlos Eduardo", "carlosedu@gmail.com", "TECH", "R$12000"), 
        ("Daniel Sousa", "danielsousa1234@gmail.com", "Tech", "R$ 5000"),
    ]

    #Laço para limpar os dados 
    dados_tratados = []
    for nome, email, setor, valor in dados_brutos:
        email_limpo = email.strip() #remoção de espaços 
        setor_tratado = setor.upper() #transforma tudo em Maiusculo
        valor_limpo = int(valor.replace("R$", ""))#remove o "R$"
        dados_tratados.append((nome, email_limpo, setor_tratado, valor_limpo))

#Criando um arquivo físico do banco localmente 
    conexao = sqlite3.connect("banco_empresarial.db")
    cursor = conexao.cursor()

#Criação da Tabela
    cursor.execute ("""
        CREATE TABLE IF NOT EXISTS leads_negocios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            setor TEXT,
            valor_estimado INTEGER
        )
    """)

    cursor.executemany("""
        INSERT OR IGNORE INTO leads_negocios (nome, email, setor, valor_estimado)
        VALUES(?, ?, ?, ?)""", dados_tratados)

    #Registrando as alterações da tabela no banco 
    conexao.commit()
    print("Dados salvos permanentemente no banco SQL.")

    print("\n[Executando Query SELECT para ler os dados gravdaos]:")
    print("-" * 65)

    cursor.execute("SELECT id, nome, email, setor, valor_estimado FROM leads_negocios")

    for linha in cursor.fetchall():
        print(f"ID: {linha[0]} | Nome: {linha[1]} | Setor:{linha[3]} | Valor: R$ {linha[4]}")
  
    conexao.close()
    print("==============================================")

if __name__ == "__main__":
    executar_pipeline_etl()