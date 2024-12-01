from faker import Faker
import duckdb

# Criar um objeto Faker
fake = Faker()

# Conectar ao DuckDB (em memória ou arquivo .db)
conn = duckdb.connect('professores.duckdb')

# Criar a tabela PROFESSOR
conn.execute('''
CREATE TABLE IF NOT EXISTS PROFESSOR (
    id_professor INTEGER PRIMARY KEY,
    nome_professor TEXT,
    departamento TEXT,
    salario DOUBLE,
    ano_contratacao INTEGER
)
''')

# Função para gerar dados fake
def gerar_dados_fake(qtd):
    for _ in range(qtd):
        yield (
            fake.name(),                # nome_professor
            fake.job(),                 # departamento
            round(fake.random_number(digits=5, fix_len=True) * 1.1, 2),  # salário
            fake.year()                 # ano_contratacao
        )

# Inserir 1 milhão de registros
print("Inserindo 1 milhão de registros...")

# Inserir dados em massa
conn.executemany('''
INSERT INTO PROFESSOR (nome_professor, departamento, salario, ano_contratacao)
VALUES (?, ?, ?, ?)
''', gerar_dados_fake(1_000_000))

print("Dados inseridos com sucesso!")

# Fechar a conexão
conn.close()
