import sqlite3

conn = sqlite3.connect('times_pokemon.db')
cursor = conn.cursor()

# Habilita chaves estrangeiras no SQLite
cursor.execute("PRAGMA foreign_keys = ON")


cursor.execute('''
    CREATE TABLE IF NOT EXISTS treinador (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS pokedex (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pokemon TEXT NOT NULL,
        tipo1 TEXT NOT NULL,
        tipo2 TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS times (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pokemon INT NOT NULL,
        id_treinador INT NOT NULL,
        FOREIGN KEY (id_treinador) REFERENCES treinador(id) ON DELETE CASCADE,
        FOREIGN KEY (id_pokemon) REFERENCES pokedex(id) ON DELETE CASCADE,
        UNIQUE (id_treinador, id_pokemon)
    )
''')


conn.commit()
conn.close()

print("Banco de dados e tabelas criados com sucesso!")