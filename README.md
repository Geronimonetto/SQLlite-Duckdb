### Instalação e Execução do Projeto

Para executar este projeto, você precisará do **Python 3.8** instalado e das bibliotecas necessárias, como o **DuckDB**. Aqui estão os passos para configurar e rodar os arquivos `main.py` e `insert_data.py`.

#### 1. **Instalar o Python**
Certifique-se de que o **Python 3.8** esteja instalado na sua máquina. Verifique com o seguinte comando:

```bash
python --version
```

Caso não tenha o Python instalado, faça o download e a instalação do [site oficial do Python](https://www.python.org/downloads/).

#### 2. **Instalar as dependências**

Instale as bibliotecas necessárias para o projeto usando o **pip**, o gerenciador de pacotes do Python. Execute o comando abaixo para instalar o **duckdb**:

```bash
pip install duckdb
```

#### 3. **Arquivo `insert_data.py`** (Inserir dados no SQLite)

Este arquivo é responsável por inserir dados no banco SQLite. Para rodar este script e inserir os dados no banco de dados `.db`, execute o seguinte comando no terminal:

```bash
python insert_data.py
```

Este script irá inserir os dados no arquivo SQLite localizado no caminho especificado no código (verifique se o caminho do arquivo `.db` está correto).

#### 4. **Arquivo `main.py`** (Conectar SQLite ao DuckDB e realizar consultas)

Depois de inserir os dados no SQLite, você pode rodar o arquivo `main.py` para integrar os dados entre o SQLite e o DuckDB. No terminal, execute:

```bash
python main.py
```

Esse script irá:

1. Conectar ao banco SQLite que contém os dados.
2. Transferir os dados do SQLite para o DuckDB.
3. Executar consultas sobre os dados no DuckDB e exibir os resultados em um DataFrame.

#### 5. **Resultados**

Após executar o `main.py`, os dados do banco SQLite serão transferidos para o DuckDB, e os resultados das consultas realizadas serão exibidos no terminal.

---

### Exemplo de Comandos para Execução

Se os arquivos estão no mesmo diretório que o terminal, execute os seguintes comandos:

1. **Inserir dados no SQLite**:

```bash
python insert_data.py
```

2. **Transferir e consultar dados no DuckDB**:

```bash
python main.py
```
