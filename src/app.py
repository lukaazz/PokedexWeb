import sqlite3
from flask import Flask, render_template, redirect, url_for
from flask import request


app = Flask(__name__)


# =================================================================================

# INDEX
@app.route("/")
def index():
    return render_template("index.html")

# =================================================================================

# LISTAGEM TREINADOR
@app.route("/treinador")
def listar_treinador():
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM treinador")
    dados = cursor.fetchall()
    conn.close()
    return render_template("treinador_lista.html", dados=dados)

# REMOVER TREINADOR
@app.route("/treinador/remover/<int:id>", methods=["POST"])
def remover_treinador(id):
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("DELETE FROM treinador WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("listar_treinador"))

# CADASTRAR TREINADOR
@app.route("/treinador/cadastro", methods=["GET", "POST"])
def cadastrar_treinador():
    if request.method == "POST":

        nome = request.form["nome"]

        conn = sqlite3.connect('times_pokemon.db')
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        
        cursor.execute("INSERT INTO treinador (nome) VALUES (?)", (nome,))
        
        conn.commit()
        conn.close()

        return redirect(url_for("listar_treinador"))
    
    return render_template("treinador_cadastro.html")

# =================================================================================

# LISTAGEM POKEDEX
@app.route("/pokedex")
def listar_pokedex():
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, pokemon, tipo1, tipo2 FROM pokedex")
    dados = cursor.fetchall()
    conn.close()
    return render_template("pokemon_lista.html", dados=dados)


# REMOVER POKEMON
@app.route("/pokedex/remover/<int:id>", methods=["POST"])
def remover_pokemon(id):
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("DELETE FROM pokedex WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("listar_pokedex"))

# CADASTRAR POKEMON
@app.route("/pokedex/cadastro", methods=["GET", "POST"])
def cadastrar_pokemon():
    if request.method == "POST":

        nome = request.form["nome"]
        tipo1 = request.form["tipo1"]
        tipo2 = request.form["tipo2"]

        conn = sqlite3.connect('times_pokemon.db')
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        
        cursor.execute("INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)", (nome, tipo1, tipo2))
        
        conn.commit()
        conn.close()

        return redirect(url_for("listar_pokedex"))
    
    return render_template("pokemon_cadastro.html")

# =================================================================================

# LISTAR TIMES
@app.route("/times")
def listar_times():
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, id_treinador, id_pokemon FROM times")
    dados = cursor.fetchall()
    conn.close()
    return render_template("time_lista.html", dados=dados)

# CADASTRAR TIME 
@app.route("/times/cadastro", methods=["GET", "POST"])
def cadastrar_time():
    return "Em construção"



if __name__ == "__main__":
    app.run(debug=True)