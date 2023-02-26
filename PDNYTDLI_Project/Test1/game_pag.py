from tkinter import *
from tkinter import messagebox
from functions import TakeFiles

def Start_game_pag(PlayerA,PlayerB):
    ############################################################
    #Config variables
    from functions import (
        config_font_type
        ,config_bgcolor
    )
    ############################################################
    #Config functions and classes

    def RollDice():
        from random import random,randint
        messagebox.showinfo(title="Dado",message=f"X se moverá {randint(1,6)} casillas")

    class Cells():

        def __init__(self, HookedFrame, row, column, padx = 0, pady = 0, text = "", backgroud = "#D2E0F3", blocked = False, command = None):

            self.HookedFrame = HookedFrame
            self.row = row
            self.column = column 
            self.padx = padx
            self.pady = pady
            self.background = backgroud
            self.text = text
            self.command = command

            TO = Button(master = self.HookedFrame, text = self.text, background = self.background, width = 18, height = 3)
            TO.config(command = self.command)
            TO.grid(row = self.row, column = self.column)
            
            if blocked:
                TO.config(state = "disabled")

    ############################################################
    #Root config
    root = Tk()
    root.resizable(0,0)
    root.title("Catch the star")
    root.config(background = config_bgcolor)
    root.iconbitmap(TakeFiles("img/star.ico"))
    s_w = root.winfo_screenwidth(); s_h = root.winfo_screenheight()
    w = 850; h = 450; x = (s_w/2) - (w/2) ; y = ((s_h/2)+200) - (h-2)
    root.geometry("%dx%d+%d+%d" % (w, h, x, y))
    root.state("zoomed")
    ############################################################
    #Frame config

    MainFrame = Frame()
    MainFrame.config(background = config_bgcolor)
    MainFrame.pack()
    ############################################################
    #Widgets config

    Separator1 = Label(MainFrame, background = config_bgcolor)
    Separator1.grid(row = 0, column = 1, pady = 50)
    Separator2 = Label(MainFrame, background = config_bgcolor)
    Separator2.grid(row = 1, column = 6, padx = 100)

    PA = PlayerA; PB = PlayerB
    WaitingCellA = Cells(MainFrame, row = 1, column = 1, text= PA, backgroud = "#C0FAA3",blocked=True)
    WaitingCellB = Cells(MainFrame, row = 1, column = 2, text = PB, backgroud = "#C0FAA3",blocked=True)

    c1 = Cells(MainFrame, row=2,column=1,text=" 1 ")
    c2 = Cells(MainFrame, row=2,column=2,text=" 2 ")
    c3 = Cells(MainFrame, row=2,column=3,text=" 3 ")
    c4 = Cells(MainFrame, row=2,column=4,text=" 4 ")
    c5 = Cells(MainFrame, row=2,column=5,text=" 5 ")

    c6 = Cells(MainFrame, row=3,column=1,text=" 6 ")
    c7 = Cells(MainFrame, row=3,column=2,text=" 7 ")
    c8 = Cells(MainFrame, row=3,column=3,text=" 8 ")
    c9  = Cells(MainFrame, row=3,column=4,text=" 9 ")
    c10  = Cells(MainFrame, row=3,column=5,text=" 10 ")

    c11 = Cells(MainFrame, row=4,column=1,text=" 11 ")
    c12 = Cells(MainFrame, row=4,column=2,text=" 12 ")
    c13 = Cells(MainFrame, row=4,column=3,text=" 13 ")
    c14  = Cells(MainFrame, row=4,column=4,text=" 14 ")
    c15  = Cells(MainFrame, row=4,column=5,text=" 15 ")

    c16 = Cells(MainFrame, row=5,column=1,text=" 16 ")
    c17 = Cells(MainFrame, row=5,column=2,text=" 17 ")
    c18 = Cells(MainFrame, row=5,column=3,text=" 18 ")
    c19  = Cells(MainFrame, row=5,column=4,text=" 19 ")
    c20  = Cells(MainFrame, row=5,column=5,text=" 20 ")


    InfoA = Cells(MainFrame, row = 2, column = 7, text = f"Info.\n{PA}")
    InfoB = Cells(MainFrame, row = 2, column = 8, text = f"Info. \n{PB}")

    ScoreA = Cells(MainFrame, row = 3, column = 7, text = f"Puntaje: Pendiente")
    ScoreB = Cells(MainFrame, row = 3, column = 8, text = f"Puntaje: Pendiente")

    RollTheDice = Cells(MainFrame, row = 5, column = 7, text = "Tirar dado", command = RollDice)
    ############################################################
    #Root mainloop
    root.mainloop()


#Start_game_pag("David", "Manuela")