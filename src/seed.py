import sqlite3

conn = sqlite3.connect('times_pokemon.db')
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


# POKEDEX
cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Bulbasaur', 'Planta', 'Venenoso'))
id_pokedex_bulbasaur = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Ivysaur', 'Planta', 'Venenoso'))
id_pokedex_ivysaur = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Venusaur', 'Planta', 'Venenoso'))
id_pokedex_venusaur = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Charmander', 'Fogo'))
id_pokedex_charmander = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Charmeleon', 'Fogo'))
id_pokedex_charmeleon = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Charizard', 'Fogo', 'Voador'))
id_pokedex_charizard = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Squirtle', 'Água'))
id_pokedex_squirtle = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Wartortle', 'Água'))
id_pokedex_wartortle = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Blastoise', 'Água'))
id_pokedex_blastoise = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Caterpie', 'Inseto'))
id_pokedex_caterpie = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Metapod', 'Inseto'))
id_pokedex_metapod = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Butterfree', 'Inseto', 'Voador'))
id_pokedex_butterfree = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Weedle', 'Inseto', 'Venenoso'))
id_pokedex_weedle = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Kakuna', 'Inseto', 'Venenoso'))
id_pokedex_kakuna = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Beedrill', 'Inseto', 'Venenoso'))
id_pokedex_beedrill = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Pidgey', 'Normal', 'Voador'))
id_pokedex_pidgey = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Pidgeotto', 'Normal', 'Voador'))
id_pokedex_pidgeotto = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Pidgeot', 'Normal', 'Voador'))
id_pokedex_pidgeot = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Rattata', 'Normal'))
id_pokedex_rattata = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Raticate', 'Normal'))
id_pokedex_raticate = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Spearow', 'Normal', 'Voador'))
id_pokedex_spearow = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Fearow', 'Normal', 'Voador'))
id_pokedex_fearow = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Ekans', 'Venenoso'))
id_pokedex_ekans = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Arbok', 'Venenoso'))
id_pokedex_arbok = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Pikachu', 'Elétrico'))
id_pokedex_pikachu = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Raichu', 'Elétrico'))
id_pokedex_raichu = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Sandshrew', 'Terra'))
id_pokedex_sandshrew = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Sandslash', 'Terra'))
id_pokedex_sandslash = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Nidoran♀', 'Venenoso'))
id_pokedex_nidoran_f = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Nidorina', 'Venenoso'))
id_pokedex_nidorina = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Nidoqueen', 'Venenoso', 'Terra'))
id_pokedex_nidoqueen = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Nidoran♂', 'Venenoso'))
id_pokedex_nidoran_m = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Nidorino', 'Venenoso'))
id_pokedex_nidorino = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Nidoking', 'Venenoso', 'Terra'))
id_pokedex_nidoking = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Clefairy', 'Normal'))
id_pokedex_clefairy = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Clefable', 'Normal'))
id_pokedex_clefable = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Vulpix', 'Fogo'))
id_pokedex_vulpix = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Ninetales', 'Fogo'))
id_pokedex_ninetales = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Jigglypuff', 'Normal'))
id_pokedex_jigglypuff = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Wigglytuff', 'Normal'))
id_pokedex_wigglytuff = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Zubat', 'Venenoso', 'Voador'))
id_pokedex_zubat = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Golbat', 'Venenoso', 'Voador'))
id_pokedex_golbat = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Oddish', 'Planta', 'Venenoso'))
id_pokedex_oddish = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Gloom', 'Planta', 'Venenoso'))
id_pokedex_gloom = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Vileplume', 'Planta', 'Venenoso'))
id_pokedex_vileplume = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Paras', 'Inseto', 'Planta'))
id_pokedex_paras = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Parasect', 'Inseto', 'Planta'))
id_pokedex_parasect = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Venonat', 'Inseto', 'Venenoso'))
id_pokedex_venonat = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Venomoth', 'Inseto', 'Venenoso'))
id_pokedex_venomoth = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Diglett', 'Terra'))
id_pokedex_diglett = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Dugtrio', 'Terra'))
id_pokedex_dugtrio = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Meowth', 'Normal'))
id_pokedex_meowth = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Persian', 'Normal'))
id_pokedex_persian = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Psyduck', 'Água'))
id_pokedex_psyduck = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Golduck', 'Água'))
id_pokedex_golduck = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Mankey', 'Lutador'))
id_pokedex_mankey = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Primeape', 'Lutador'))
id_pokedex_primeape = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Growlithe', 'Fogo'))
id_pokedex_growlithe = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Arcanine', 'Fogo'))
id_pokedex_arcanine = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Poliwag', 'Água'))
id_pokedex_poliwag = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Poliwhirl', 'Água'))
id_pokedex_poliwhirl = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Poliwrath', 'Água', 'Lutador'))
id_pokedex_poliwrath = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Abra', 'Psíquico'))
id_pokedex_abra = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Kadabra', 'Psíquico'))
id_pokedex_kadabra = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Alakazam', 'Psíquico'))
id_pokedex_alakazam = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Machop', 'Lutador'))
id_pokedex_machop = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Machoke', 'Lutador'))
id_pokedex_machoke = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Machamp', 'Lutador'))
id_pokedex_machamp = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Bellsprout', 'Planta', 'Venenoso'))
id_pokedex_bellsprout = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Weepinbell', 'Planta', 'Venenoso'))
id_pokedex_weepinbell = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Victreebel', 'Planta', 'Venenoso'))
id_pokedex_victreebel = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Tentacool', 'Água', 'Venenoso'))
id_pokedex_tentacool = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Tentacruel', 'Água', 'Venenoso'))
id_pokedex_tentacruel = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Geodude', 'Pedra', 'Terra'))
id_pokedex_geodude = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Graveler', 'Pedra', 'Terra'))
id_pokedex_graveler = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Golem', 'Pedra', 'Terra'))
id_pokedex_golem = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Ponyta', 'Fogo'))
id_pokedex_ponyta = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Rapidash', 'Fogo'))
id_pokedex_rapidash = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Slowpoke', 'Água', 'Psíquico'))
id_pokedex_slowpoke = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Slowbro', 'Água', 'Psíquico'))
id_pokedex_slowbro = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Magnemite', 'Elétrico'))
id_pokedex_magnemite = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Magneton', 'Elétrico'))
id_pokedex_magneton = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ("Farfetch'd", 'Normal', 'Voador'))
id_pokedex_farfetchd = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Doduo', 'Normal', 'Voador'))
id_pokedex_doduo = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Dodrio', 'Normal', 'Voador'))
id_pokedex_dodrio = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Seel', 'Água'))
id_pokedex_seel = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Dewgong', 'Água', 'Gelo'))
id_pokedex_dewgong = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Grimer', 'Venenoso'))
id_pokedex_grimer = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Muk', 'Venenoso'))
id_pokedex_muk = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Shellder', 'Água'))
id_pokedex_shellder = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Cloyster', 'Água', 'Gelo'))
id_pokedex_cloyster = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Gastly', 'Fantasma', 'Venenoso'))
id_pokedex_gastly = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Haunter', 'Fantasma', 'Venenoso'))
id_pokedex_haunter = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Gengar', 'Fantasma', 'Venenoso'))
id_pokedex_gengar = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Onix', 'Pedra', 'Terra'))
id_pokedex_onix = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Drowzee', 'Psíquico'))
id_pokedex_drowzee = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Hypno', 'Psíquico'))
id_pokedex_hypno = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Krabby', 'Água'))
id_pokedex_krabby = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Kingler', 'Água'))
id_pokedex_kingler = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Voltorb', 'Elétrico'))
id_pokedex_voltorb = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Electrode', 'Elétrico'))
id_pokedex_electrode = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Exeggcute', 'Planta', 'Psíquico'))
id_pokedex_exeggcute = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Exeggutor', 'Planta', 'Psíquico'))
id_pokedex_exeggutor = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Cubone', 'Terra'))
id_pokedex_cubone = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Marowak', 'Terra'))
id_pokedex_marowak = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Hitmonlee', 'Lutador'))
id_pokedex_hitmonlee = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Hitmonchan', 'Lutador'))
id_pokedex_hitmonchan = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Lickitung', 'Normal'))
id_pokedex_lickitung = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Koffing', 'Venenoso'))
id_pokedex_koffing = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Weezing', 'Venenoso'))
id_pokedex_weezing = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Rhyhorn', 'Pedra', 'Terra'))
id_pokedex_rhyhorn = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Rhydon', 'Pedra', 'Terra'))
id_pokedex_rhydon = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Chansey', 'Normal'))
id_pokedex_chansey = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Tangela', 'Planta'))
id_pokedex_tangela = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Kangaskhan', 'Normal'))
id_pokedex_kangaskhan = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Horsea', 'Água'))
id_pokedex_horsea = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Seadra', 'Água'))
id_pokedex_seadra = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Goldeen', 'Água'))
id_pokedex_goldeen = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Seaking', 'Água'))
id_pokedex_seaking = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Staryu', 'Água'))
id_pokedex_staryu = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Starmie', 'Água', 'Psíquico'))
id_pokedex_starmie = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Mr. Mime', 'Psíquico'))
id_pokedex_mr_mime = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Scyther', 'Inseto', 'Voador'))
id_pokedex_scyther = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Jynx', 'Gelo', 'Psíquico'))
id_pokedex_jynx = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Electabuzz', 'Elétrico'))
id_pokedex_electabuzz = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Magmar', 'Fogo'))
id_pokedex_magmar = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Pinsir', 'Inseto'))
id_pokedex_pinsir = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Tauros', 'Normal'))
id_pokedex_tauros = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Magikarp', 'Água'))
id_pokedex_magikarp = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Gyarados', 'Água', 'Voador'))
id_pokedex_gyarados = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Lapras', 'Água', 'Gelo'))
id_pokedex_lapras = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Ditto', 'Normal'))
id_pokedex_ditto = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Eevee', 'Normal'))
id_pokedex_eevee = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Vaporeon', 'Água'))
id_pokedex_vaporeon = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Jolteon', 'Elétrico'))
id_pokedex_jolteon = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Flareon', 'Fogo'))
id_pokedex_flareon = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Porygon', 'Normal'))
id_pokedex_porygon = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Omanyte', 'Pedra', 'Água'))
id_pokedex_omanyte = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Omastar', 'Pedra', 'Água'))
id_pokedex_omastar = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Kabuto', 'Pedra', 'Água'))
id_pokedex_kabuto = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Kabutops', 'Pedra', 'Água'))
id_pokedex_kabutops = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Aerodactyl', 'Pedra', 'Voador'))
id_pokedex_aerodactyl = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Snorlax', 'Normal'))
id_pokedex_snorlax = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Articuno', 'Gelo', 'Voador'))
id_pokedex_articuno = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Zapdos', 'Elétrico', 'Voador'))
id_pokedex_zapdos = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Moltres', 'Fogo', 'Voador'))
id_pokedex_moltres = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Dratini', 'Dragão'))
id_pokedex_dratini = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Dragonair', 'Dragão'))
id_pokedex_dragonair = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1, tipo2) VALUES (?, ?, ?)', ('Dragonite', 'Dragão', 'Voador'))
id_pokedex_dragonite = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Mewtwo', 'Psíquico'))
id_pokedex_mewtwo = cursor.lastrowid

cursor.execute('INSERT INTO pokedex (pokemon, tipo1) VALUES (?, ?)', ('Mew', 'Psíquico'))
id_pokedex_mew = cursor.lastrowid


# TREINADOR
cursor.execute('INSERT INTO treinador (nome) VALUES (?)', ('Brenden',))
id_treinador_brenden = cursor.lastrowid


# TIME
cursor.execute('INSERT INTO times (id_pokemon, id_treinador) VALUES (?, ?)', (id_pokedex_venusaur, id_treinador_brenden))



conn.commit()
conn.close()

print("Tabelas preenchidas!")