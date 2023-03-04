import random
import tkinter as tk
import tkinter.messagebox as messagebox
import sqlite3
from gtts import gTTS
from playsound import playsound
from os import path, remove

def hacer_pregunta():
    preguntas = [
        "¿Cuál es la capital de Francia?",
        "¿Cuál es el océano más grande del mundo?",
        "¿En qué país se encuentra la Torre Eiffel?",
        "¿Quién escribió el Quijote?",
        "¿Cuál es el río más largo del mundo?",
        "¿Cuál es la moneda oficial de Japón?",
        "¿Qué elemento químico tiene el símbolo Fe?",
        "¿Cuál es el planeta más cercano al sol?",
        "¿Quién descubrió la penicilina?",
        "¿Cuál es el número atómico del hidrógeno?",
        "¿Cuál es el animal más rápido del mundo?",
        "¿Quién pintó la Mona Lisa?",
        "¿Cuál es el país más grande del mundo?",
        "¿En qué año se descubrió América?",
        "¿Cuál es el segundo idioma más hablado del mundo?",
        "¿Cuál es el hueso más largo del cuerpo humano?",
        "¿En qué país se encuentra Machu Picchu?",
        "¿Quién fue el primer presidente de los Estados Unidos?",
        "¿Cuál es el nombre del continente más frío del mundo?",
        "¿Cuál es el libro más vendido de la historia?"]
    respuestas = [
        ("A) París\nB) Berlín\nC) Londres", "A"),
        ("A) Atlántico\nB) Pacífico\nC) Índico", "B"),
        ("A) Italia\nB) España\nC) Francia", "C"),
        ("A) Cervantes\nB) Shakespeare\nC) Dante", "A"),
        ("A) Amazonas\nB) Nilo\nC) Yangtze", "B"),
        ("A) Dólar\nB) Euro\nC) Yen", "C"),
        ("A) Hierro\nB) Hidrógeno\nC) Helio", "A"),
        ("A) Mercurio\nB) Venus\nC) Marte", "A"),
        ("A) Alexander Fleming\nB) Louis Pasteur\nC) Robert Koch", "A"),
        ("A) 1\nB) 2\nC) 3", "A"),
        ("A) Leopardo\nB) Guepardo\nC) Jaguar", "B"),
        ("A) Leonardo da Vinci\nB) Pablo Picasso\nC) Vincent van Gogh", "A"),
        ("A) Rusia\nB) China\nC) Canadá", "A"),
        ("A) 1492\nB) 1776\nC) 1812", "A"),
        ("A) Español\nB) Inglés\nC) Chino mandarín", "B"),
        ("A) Fémur\nB) Tibia\nC) Húmero", "A"),
        ("A) Perú\nB) Chile\nC) Argentina", "A"),
        ("A) George Washington\nB) Thomas Jefferson\nC) John Adams", "A"),
        ("A) Antártida\nB) África\nC) Asia", "A"),
        ("A) La Biblia\nB) Don Quijote\nC) El Corán", "A")]
        # Seleccionar una pregunta aleatoria
    indice_pregunta = random.randint(0, len(preguntas) - 1)
    pregunta = preguntas[indice_pregunta]
    opciones, respuesta_correcta = respuestas[indice_pregunta]
    
    # Crear una ventana de diálogo para la pregunta
    root = tk.Tk()
    s_w = root.winfo_screenwidth(); s_h = root.winfo_screenheight()
    w = 300; h = 200; x = (s_w/2) - (w/2) ; y = ((s_h/2)+200) - (h-2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.title(f"Pregunta {indice_pregunta + 1}")

    RootFrame = tk.Frame()
    RootFrame.place(x = 0, y = 0, relwidth = 1, relheight = 1)
    
    # Agregar la pregunta y las opciones como etiquetas
    pregunta_label = tk.Label(root, text=pregunta)
    pregunta_label.grid(row=0,column=1)

    opciones_label = tk.Label(root, text=opciones)
    opciones_label.grid(row=1,column=1)

    
    
    # Función para verificar la respuesta del usuario
    def verificar_respuesta(respuesta):
        if respuesta == respuesta_correcta:

            answer_generator(answer = "True")

            messagebox.showinfo("Resultado", "¡Respuesta correcta!")
            root.destroy()  # Cerrar la ventana de diálogo
        else:

            answer_generator(answer = "False")

            messagebox.showerror("Resultado", f"Respuesta incorrecta.\nLa respuesta correcta era: {respuesta_correcta}")
            root.destroy()  # Cerrar la ventana de diálogo
           
    # Agregar botones para las opciones
    boton_a = tk.Button(root, text="A", command=lambda: verificar_respuesta("A"))
    boton_a.grid(row=2,column=0)


    boton_b = tk.Button(root, text="B", command=lambda: verificar_respuesta("B"))
    boton_b.grid(row=2,column=1)


    boton_c = tk.Button(root, text="C", command=lambda: verificar_respuesta("C"))
    boton_c.grid(row=2,column=2)

    #pregunta_label.pack(pady=10)


    
    # Mostrar la ventana de diálogo
    root.mainloop()
    
    return indice_pregunta, pregunta, opciones

def make_matrix(how_long = 20):
    try:
        if how_long % 5 != 0:
            print("Lo sentimos, intentas hacer una matrix que no es multiplo de 5")
        else:
            list = []
            for i in range(0,how_long):
                list.append(f"  ")
            return list
    except ValueError as Error:
        print("Error:",Error)

def print_matrix(ListToPrint):
    try:
        how_long = len(ListToPrint)
        if how_long % 5 != 0:
            print("Lo sentimos, intentas imprimir una matrix que no es multiplo de 5")
        else:
            for i in range(0, len(ListToPrint), 5):
                print(ListToPrint[i:i+5])
    except ValueError as Error:
        print("Error:",Error)

def take_files(file = "nothing"):
    try:
        import sys
        import os
        file = str(file)
        if (file != "nothing"):
            give = os.path.join(sys.path[0], f"{file}")
            return give
        else:
            return "> You must enter a file to find it <"
    except ValueError as Error:
        print("Error:",Error)

def make_players():
    PlayerA = input("Ingresa el nombre del jugador A: ")
    PlayerB = input("Ingresa el nombre del jugador B: ")
    if len(PlayerA) > 7 or len(PlayerB) > 7:
        print("Lo sentimos... Pero los nicks no deben superar los 7 carácteres...")
        print(f"Jugador A ({PlayerA} x{len(PlayerA)})\nJugador B ({PlayerB} x{len(PlayerB)})")
        return False,False
    else:
        return PlayerA,PlayerB

def make_database(database_name = "game_info.db"):
    try:
        connector = sqlite3.connect(take_files(database_name))
        cursor = connector.cursor()
        connector.close()
        file = open(take_files("current_turn.txt"),"a")
        file.close()
    except sqlite3.Error as the_error:
            print("Hay un imprevisto en la zona de DB...")
            print("Tipo de error:",the_error)

def make_table(database_name = "game_info.db"):
    try:
        connector = sqlite3.connect(take_files(database_name))
        cursor = connector.cursor()
        cursor.execute("CREATE TABLE players_info (player text PRIMARY KEY, position integer, score integer)")
        connector.close()
    except sqlite3.Error as the_error:
            print("Hay un imprevisto en la zona de DB...")
            print("Tipo de error:",the_error)

def delete_database(database_name = "game_info.db"):
    file_deleter(database_name)
    file_deleter("answer.txt")
    file_deleter("current_turn.txt")

def insert_players_basic_info(playera,playerb,database_name = "game_info.db"):
    try:
        connector = sqlite3.connect(take_files(database_name))
        cursor = connector.cursor()
        cursor.execute("INSERT INTO players_info VALUES (?,?,?)", (playera,0,0))
        cursor.execute("INSERT INTO players_info VALUES (?,?,?)", (playerb,0,0))
        connector.commit()
        connector.close()
    except sqlite3.Error as the_error:
            print("Hay un imprevisto en la zona de DB...")
            print("Tipo de error:",the_error)

def roll_dice(limit = 6):
    return random.randint(1,limit)

def answer_generator(answer = "False",answer_file = "answer.txt"):
    file_deleter(answer_file)
    file = open(take_files(answer_file),"w")
    file.write(answer)

def select_1st_player(pa,pb):
    #1 = a ; 2 = b
    file = open(take_files("current_turn.txt"), "w")
    if random.randint(1,2) == 1: #if 1
        file.write(pa)
    else: #if 2
        file.write(pb)

def add_score(player, increment = 1, database = "game_info.db"):

    #Connecting and creating cursos just to take current score
    connector = sqlite3.connect(take_files(database))
    cursor = connector.cursor()

    current_score = check_current_score(player,database)

    #+1 score to current score
    current_score += increment
    cursor.execute(f"update players_info set score = {current_score} where player == '{player}'")
    connector.commit()

    #closing database connection
    connector.close()

def check_current_score(player, database = "game_info.db"):

    #Connecting and creating cursos just to take current score
    connector = sqlite3.connect(take_files(database))
    cursor = connector.cursor()

    cursor.execute(f"select score from players_info where player == '{player}'")
    
    current_score = cursor.fetchall()
    current_score = current_score[0] #taking 1st element of the list
    current_score = current_score[0] #taking 1st element of the tuple
    connector.close()
    return current_score

def check_current_player(file_to_check = "current_turn.txt"):
    file = open(take_files(file_to_check),"r")
    current = file.readlines()
    return(current[0])

def check_current_answer(file_to_check = "answer.txt"):
    file = open(take_files(file_to_check))
    answer = file.readlines()
    answer = answer[0]
    return answer == "True"

def file_deleter(file_name = "answer.txt"):
    if path.exists(take_files(file_name)):
        remove(take_files(file_name))

def change_current_player(pa,pb,file_to_change = "current_turn.txt"):
    currentis = check_current_player()
    file = open(take_files(file_to_change), "w")
    if currentis == pa:
        file.write(pb)
    else:
        file.write(pa)
        
def player_mover(list, player, moving):
    limit = len(list)
    current_position = check_current_position(player)
    current_position = int(current_position)
    
    #If dice marks a > number 
    if ((current_position + moving) > limit):
        change_current_player_position(player,limit)

    #If dice marks a < number and that numbers pass 0 index
    
    elif current_position + moving <= 0:
        change_current_player_position(player, 0)

    #If dice marks a < number
    elif ((current_position + moving) < limit):
        change_current_player_position(player, (current_position+moving))

def check_current_position(player, database = "game_info.db"):

    #Connecting and creating cursos just to take current score
    connector = sqlite3.connect(take_files(database))
    cursor = connector.cursor()

    cursor.execute(f"select position from players_info where player == '{player}'")
    
    current_score = cursor.fetchall()
    current_score = current_score[0] #taking 1st element of the list
    current_score = current_score[0] #taking 1st element of the tuple
    connector.close()
    return current_score

def change_current_player_position(player, new_position, database = "game_info.db"):
    #Connecting and creating cursos just to take current score
    connector = sqlite3.connect(take_files(database))
    cursor = connector.cursor()

    cursor.execute(f"update players_info set position = {new_position} where player == '{player}'")
    
    connector.commit()
    connector.close()

def punishment(list, player):
    punishement_type = random.randint(1,3)

    if punishement_type == 1:
        #Puente
        player_mover(list,player,-3)
        talker(f"{player}, has respondido fatal... La sanción por tu error será Puente... (Retrocederas 3 casillas)")


    elif punishement_type == 2:
        #Resbalon
        player_mover(list,player,-2)
        talker(f"{player}, has respondido fatal... La sanción por tu error será Resbalon... (Retrocederas 2 casillas)")


    elif punishement_type == 3:
        #Calavera
        player_mover(list, player, -99999)
        talker(f"{player}, has respondido fatal... La sanción por tu error será Calavera... (Retrocederas hasta el inicio)")
    
def talker(StringToVoice):
    tts = gTTS(StringToVoice, lang='es-US')
    tts.save(take_files("punishment_audio.mp3"))
    playsound(take_files("punishment_audio.mp3"))
    file_deleter("punishment_audio.mp3")

def winer_detector(database = "game_info.db"):

    #Connecting and creating cursos just to take current score
    connector = sqlite3.connect(take_files(database))
    cursor = connector.cursor()

    cursor.execute(f"select player from players_info where position == 20")
    
    current_score = cursor.fetchall()
    if current_score == []:
        return None
    else:
        return current_score[0]
    connector.close()
    return current_score
    
def game_stopper(database = "game_info.db"):
    messagebox.showinfo(title="Juego finalizado", message = f"Tenemos un ganador, y es: {winer_detector()}\n\nEl juego ya acabo :(. Te invitamos a que mires el siguiente resumen de la partida)")
    messagebox.showinfo(title="Juego finalizado", message=game_current_info())

def game_current_info(database = "game_info.db"):
    dict_with_info = {}

    connector = sqlite3.connect(take_files(database))
    cursor = connector.cursor()




    cursor.execute(f"select player from players_info")
    all_players = cursor.fetchall()

    dict_with_info["PlayerA_name"] = all_players[0][0]
    dict_with_info["PlayerB_name"] = all_players[1][0]



    cursor.execute(f"select position from players_info")
    all_positions = cursor.fetchall()

    dict_with_info["PlayerA_position"] = all_positions[0][0]
    dict_with_info["PlayerB_position"] = all_positions[1][0]

    cursor.execute(f"select score from players_info")
    all_score = cursor.fetchall()

    dict_with_info["PlayerA_score"] = all_score[0][0]
    dict_with_info["PlayerB_score"] = all_score[1][0]

    connector.close()
    
    PA_name = dict_with_info["PlayerA_name"]
    PA_position = dict_with_info["PlayerA_position"]
    PA_score = dict_with_info["PlayerA_score"]

    PB_name = dict_with_info["PlayerB_name"]
    PB_position = dict_with_info["PlayerB_position"]
    PB_score = dict_with_info["PlayerB_score"]

    temp_msg = (
        f"""
        Jugador (A)
            - Nombre: {PA_name}
            - Posición: {PA_position}
            - Aciertos: {PA_score}

        Jugador (B)
            - Nombre: {PB_name}
            - Posición: {PB_position}
            - Aciertos: {PB_score}
        """
    )

    return temp_msg

def spacer(jumps):
    for i in range(0,jumps-1):
        print("\n")

