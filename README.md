# Pipeline de Engenharia de Dados (ETL) com Python e SQL

Este Projeto p´ratio de engenharia de dados simula um pipeline completo de **ETL (Extract, Transform, Load)**. O objetivo é demonstrar a automaação de processos de dados, padronização de strings, conversão de tipos de dados e a garantia de persistencia em um banco de dador relacional.

## Tecnologias e Ferramentas 
**Python 3** (Lógica central, laços de repetição e trataamento dos dados)
**SQLite3** (Banco de dados relacional nativo para persistência física em disco)

---

## Estrutura do Pipeline (Como funciona?)

O script foi desenhado seguindo a arquitetura de um pipeline único automatizad, dividido em três etapas seguidas obrigatórias:

### 1. Extração (Extract)
Simula a coleta de dados brutos que vieram de um sistema externo ou planilha de Marketing. A lista inicial contém falhas críticas e comuns no uso do dia-dia, tais como:
* Epaços em branco invisíveis nas pontas dos e-mails.
* Categorias de setores despadronizados ( misturando maiúsculas e minúsculas).
* Valores financeiros formatados como texto contendo o símbolo de moeda(`R$`).
* Registros idênticos duplicados.

### 2. Transformação (Transform)
Utiliza recursos nativos do Python para varrer os dados brutos e aplicar as regras de negócio e limpeza antes de enviar para o banco: 
* **`.strip()`**: Remove os espaços vazios e invisíveis do e-mail.
* **`.upper()`**: Padroniza os setores em letras maiúsculas ( ex:`financeiro` vira `FINANCEIRO`).
* **`int(valor.replace("R$", ""))`**: Remove o símbolo da moeda e converte o texto puero em um número inteiro real, permitindo futuras operações matemáticas no banco.

### 3. Caga (Load)
Os dados perfeitamente limpos são enviados em lote para o banco através do comando`executemany`. O     script garante que a tabela seja criada automaticamente caso ela não exista (`CREATE TABLE IF NOT      EXISTS`).

---

## Recursos de Segurança e Boas Práticas

Se este script rodas em rodução múltiplas vezes, ele está protejido por conceitos fundamentais de engenharia:
* **Persistência em Disco:** Diferente de bancos temporários criados na memória RAM(`:memory:`), os dados aqui saõ gravaddos permanentemente no arquivo físico `banco_empresarial.db`.
* **Idempotência (Garantia anti-duplicação):** A coluna de e-mail possui a restrição `UNIQUE`. Combianda com o comando `INSERT OR IGNORE` do SQL, o banco rejeita automaticamente as linhas repetidas sem quebrar a execução do código.
* **Proteção contra SQL Injection:** O uso de placehoolders `(?, ?, ?, ?)` blinda a aplicação contra inserções maliciosas de código nos campos de texto.
* **Validaçao Visual:** Ao final do processo, o script executa uma query `SELECT` puramente para listar no terminal o resultado dinal do banco consolidado.

---

## Como Executar o Projeto.

1. Certifique-se de ter o Python instalado.
2. Abra o terminal (PowerShell ou CMD) na pasta onde o arquivo `pipeline_dados.py` está salvo.
3. Execute o comando:
```bash
python pipeline_dados.py
```
4. O Terminal exibirá o processo e o resultado do banco. Um arquivo chamado banco_empresarial.db será criado no mesmo diretório.
