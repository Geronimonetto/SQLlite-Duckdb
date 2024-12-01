import os
import duckdb

sqlite_file = 'C:/Users/geron/Documents/Python_estudos/Projetos/ETL_database/SQLlite-Duckdb/databases/professores.db'

if not os.path.exists(sqlite_file):
    print(f"Erro: O arquivo {sqlite_file} não foi encontrado!")
else:
    con = duckdb.connect()

    tables = con.execute(f"SELECT name FROM sqlite_master WHERE type='table';").fetchall()
    print(f"Tabelas no arquivo SQLite: {tables}")

    
    try:
        con.execute(f"CREATE TABLE professores AS SELECT * FROM sqlite_scan('{sqlite_file}', 'PROFESSOR');")
        
        df_professores = con.execute("SELECT * FROM professores;").fetch_df()
        print(df_professores)

    except Exception as e:
        print(f"Erro ao criar a tabela no DuckDB: {e}")


    con.close()
