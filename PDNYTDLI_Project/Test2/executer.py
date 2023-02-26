from functions import *
from tkinter import messagebox
delete_database()

Posiciones = make_matrix(20)
PA,PB = make_players()


make_database()
make_table()
select_1st_player(PA,PB)
insert_players_basic_info(PA,PB)


while(Posiciones[-1] == " 20 "): #Ejecutando el juego mientras nadie este en la casilla 20
    messagebox.showwarning(title="Turno",message=f"Actualmente es el turno de {check_current_player()}\n\nTe daremos una pregunta, ¿Estás listo?")
    rightornot = hacer_pregunta()
    print(f"{check_current_player()}, el resultado de tu respuesta ha sido: {rightornot}")
    change_current_player(PA,PB)
    



delete_database()