from functions import *
from tkinter import messagebox
from os import system as Terminal
delete_database()

Posiciones = make_matrix(20)
Posiciones[-1] = " ⭐ "
Posiciones[0] = " ❂ "

PA,PB = make_players()


make_database()
make_table()
select_1st_player(PA,PB)
insert_players_basic_info(PA,PB)

Terminal('cls')
player_mover(Posiciones,PA,15)

while(winer_detector() == None): #Ejecutando el juego mientras nadie este en la casilla 20

#-------------------------------------------#
#Info printer zone
    print(f"\n\nJugador A: {PA}\nJugador B: {PB}\n\n")
    print_matrix(Posiciones)
    spacer(2)
    print(f"{PA} (Puntos: {check_current_score(PA)})")
    print(f"{PA} (Posición: {check_current_position(PA)})")
    spacer(2)
    print(f"{PB} (Puntos: {check_current_score(PB)})")
    print(f"{PB} (Posición: {check_current_position(PB)})")

#-------------------------------------------#
#Questions zone

    current_player = check_current_player()
    messagebox.showinfo(title = "Tirar dado", message=f"!{current_player}, es tu turno de tirar el dado! ¿Estás listo?")
    dice_number = roll_dice()
    messagebox.showwarning(title ="Resultado", message=f"{current_player}, te moveremos {dice_number} casillas")
    player_mover(Posiciones,current_player,dice_number)
    messagebox.showwarning(title="Turno",message=f"Actualmente es el turno de {current_player}\n\nTe daremos una pregunta, ¿Estás listo?")
    hacer_pregunta()

    right_not_right = check_current_answer(file_to_check = "answer.txt")
    #+5 score
    if right_not_right:
        add_score(current_player,1)
    #-2 score
    else:
        add_score(current_player,0)
        punishment(Posiciones,current_player)
    change_current_player(PA,PB)


#-------------------------------------------#
#Clean terminal
    Terminal('cls')




game_stopper()