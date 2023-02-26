from functions import *
from tkinter import messagebox
from os import system as Terminal
delete_database()

Posiciones = make_matrix(20)
PA,PB = make_players()


make_database()
make_table()
select_1st_player(PA,PB)
insert_players_basic_info(PA,PB)

Terminal('cls')


while(Posiciones[-1] == " 20 "): #Ejecutando el juego mientras nadie este en la casilla 20

#-------------------------------------------#
#Info printer zone
    print(f"\n\nJugador A: {PA}\nJugador B: {PB}\n\n")
    print_matrix(Posiciones)
    print(f"\n{PA} (Puntos: {check_current_score(PA)})")
    print(f"{PB} (Puntos: {check_current_score(PB)})")

#-------------------------------------------#
#Questions zone
    messagebox.showwarning(title="Turno",message=f"Actualmente es el turno de {check_current_player()}\n\nTe daremos una pregunta, ¿Estás listo?")
    hacer_pregunta()
    right_not_right = check_current_answer(file_to_check = "answer.txt")
    #+5 score
    if right_not_right:
        add_score(check_current_player(),5)
    #-2 score
    else:
        add_score(check_current_player(),-2)
    change_current_player(PA,PB)


#-------------------------------------------#
#Clean terminal
    Terminal('cls')