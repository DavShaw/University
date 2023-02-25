from tkinter import *
from tkinter import messagebox
from functions import TakeFiles


##############
#The most important object
root = Tk()

############################################################
#Config variables
from functions import (
    config_font_type
    ,config_bgcolor
)
############################################################
#Config functions

def PlayButton():
    if entry_p1.get() == "" or entry_p2.get() == "":
        messagebox.showwarning(title = "Jugador inválido", message = "Parece que alguno de los jugadores no ha\ningresado su nombre. . .")
    elif not (entry_p1.get() != "" and len(entry_p1.get()) <= 10):
        messagebox.showwarning(title = "Jugador inválido", message = "Lo sentimos, pero el nombre que elegiste parece\nque tiene mas de 10 carácteres\n\n(Jugador A)")
    elif not (entry_p2.get() != "" and len(entry_p2.get()) <= 10):
        messagebox.showwarning(title = "Jugador inválido", message = "Lo sentimos, pero el nombre que elegiste parece\nque tiene mas de 10 carácteres\n\n(Jugador B)")
    else:
        messagebox.showinfo(title = "Catch the star", message = f"¡Bienvenido!")
        from game_pag import Start_game_pag
        pa = entry_p1.get();pb = entry_p2.get()
        root.destroy()
        Start_game_pag(pa,pb)
############################################################
#Root config
root.resizable(0,0)
root.title("Catch the star")
root.config(background = config_bgcolor)
root.iconbitmap(TakeFiles("img/star.ico"))
s_w = root.winfo_screenwidth(); s_h = root.winfo_screenheight()
w = 650; h = 350; x = (s_w/2) - (w/2) ; y = ((s_h/2)+200) - (h-2)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
############################################################
#Frame config

MainFrame = Frame()
MainFrame.config(background = config_bgcolor)
MainFrame.pack()
############################################################
#Widgets config

text1 = Label(MainFrame, text = "* Jugador (A)",font = (config_font_type, 15) ,background = config_bgcolor)
text1.grid(row = 1, column = 0, pady = 15)

entry_p1 = Entry(MainFrame, justify = CENTER, font = (config_font_type, 12))
entry_p1.grid(row = 2, column = 0, pady = 15)

text2 = Label(MainFrame, text = "* Jugador (B)",font = (config_font_type, 15) ,background = config_bgcolor)
text2.grid(row = 3, column = 0, pady = 15)

entry_p2 = Entry(MainFrame, justify = CENTER, font = (config_font_type, 12))
entry_p2.grid(row = 4, column = 0, pady = 15)

Play = Button(MainFrame, text = "  Jugar  ", font = (config_font_type, 12), borderwidth = 10)
Play.config(command = PlayButton)
Play.grid(row = 5, column = 0, pady = 30)







############################################################
#Root mainloop
root.mainloop()
