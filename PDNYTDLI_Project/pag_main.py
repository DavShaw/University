from tkinter import *

class CustomButton():


    def __init__(self,HookedFrame, text = "", row = 0, column = 0, borderwidth = 0):
        
        self.HookedFrame = HookedFrame
        self.text = text
        self.row = row
        self.column = column
        self.borderwidth = borderwidth
        
        a = Button(self.HookedFrame,text = self.text, borderwidth= self.borderwidth)
        a.grid(row= self.row, column= self.column)

root = Tk()



root.title("Alcanza la estrella")
root.state("zoomed")

MainFrame = Frame()
MainFrame.config(width=0,height=0)
MainFrame.place(x=0, y=0, relheight=1, relwidth=1)
MainFrame.config(background="blue")
MainFrame.pack()


StartGame = CustomButton(HookedFrame = MainFrame, text = "¡A jugar!", row = 3, column=1)



root.mainloop()

