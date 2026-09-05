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
    cursor.execute("SELECT times.id, pokedex.pokemon, treinador.nome FROM times JOIN treinador ON times.id_treinador = treinador.id JOIN pokedex ON times.id_pokemon = pokedex.id")
    dados = cursor.fetchall()
    conn.close()
    return render_template("time_lista.html", dados=dados)

# REMOVER TIME
@app.route("/times/remover/<int:id>", methods=["POST"])
def remover_time(id):
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute("DELETE FROM times WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for("listar_times"))

# CADASTRAR TIME 
@app.route("/times/cadastro", methods=["GET", "POST"])
def cadastrar_time():

    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    if request.method == "POST":
    
        id_treinador = request.form["id_treinador"]
        id_pokemon = request.form["id_pokemon"]

        try:
            cursor.execute("INSERT INTO times (id_treinador, id_pokemon) VALUES (?, ?)", (id_treinador, id_pokemon))
            conn.commit()

        # trata execeção caso o time cadastrado já exista
        except sqlite3.IntegrityError:
            pass

        finally:
            conn.close()

        
        return redirect(url_for("listar_times"))


    cursor.execute("SELECT id, nome FROM treinador")
    dados_treinador = cursor.fetchall()  

    cursor.execute("SELECT id, pokemon FROM pokedex")
    dados_pokedex = cursor.fetchall()  

    conn.close()
    
    return render_template("time_cadastro.html", treinadores=dados_treinador, pokemons=dados_pokedex)

# EDITAR POKEMON
@app.route("/pokedex/editar/<int:id>", methods=["GET", "POST"])
def editar_pokemon(id):
    conn = sqlite3.connect('times_pokemon.db')
    cursor = conn.cursor()

    if request.method == "POST":
        # usuário enviou o formulário preenchido -> atualizar o banco
        nome = request.form["nome"]
        tipo1 = request.form["tipo1"]
        tipo2 = request.form["tipo2"]

        cursor.execute(
            "UPDATE pokedex SET pokemon = ?, tipo1 = ?, tipo2 = ? WHERE id = ?",
            (nome, tipo1, tipo2, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for("listar_pokedex"))

    else:
        # GET -> precisa buscar o registro atual para pré-preencher o form
        cursor.execute("SELECT * FROM pokedex WHERE id = ?", (id,))
        registro = cursor.fetchone()
        conn.close()
        return render_template("pokemon_editar.html", registro=registro)
    
# =================================================================================




if __name__ == "__main__":
    app.run(debug=True)