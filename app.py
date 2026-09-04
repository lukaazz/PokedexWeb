import sqlite3

conn = sqlite3.connect('times_pokemon.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")









conn.commit()
conn.close()