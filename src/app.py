import sqlite3
from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)

# LISTAGEM TREINADOR
@app.route("/treinador")
def listar_treinador():
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM treinador")
    dados = cursor.fetchall()
    conn.close()
    return render_template("treinador_lista.html", dados=dados)


@app.route("/treinador/remover/<int:id>", methods=["POST"])
def remover_treinador(id):
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("DELETE FROM treinador WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("listar_treinador"))


# LISTAGEM POKEDEX
@app.route("/pokedex")
def listar_pokedex():
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, pokemon, tipo1, tipo2 FROM pokedex")
    dados = cursor.fetchall()
    conn.close()
    return render_template("pokemon_lista.html", dados=dados)



@app.route("/pokedex/remover/<int:id>", methods=["POST"])
def remover_pokemon(id):
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("DELETE FROM pokedex WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("listar_pokedex"))



if __name__ == "__main__":
    app.run(debug=True)