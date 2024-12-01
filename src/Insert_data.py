from faker import Faker
import sqlite3

# Criar um objeto Faker
fake = Faker()

# Conectar ao banco SQLite
conn = sqlite3.connect('professores.db')
cursor = conn.cursor()

# Criar a tabela PROFESSOR
cursor.execute('''
CREATE TABLE IF NOT EXISTS PROFESSOR (
    id_professor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome_professor TEXT,
    departamento TEXT,
    salario REAL,
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
cursor.executemany('''
INSERT INTO PROFESSOR (nome_professor, departamento, salario, ano_contratacao)
VALUES (?, ?, ?, ?)
''', gerar_dados_fake(1_000_000))

# Confirmar as alterações e fechar a conexão
conn.commit()
print("Dados inseridos com sucesso!")
conn.close()
