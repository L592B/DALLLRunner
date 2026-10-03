from tkinter import *

class Menu:

    def __init__(self):
        self.fenetre = Tk()
        self.titre = Label(self.fenetre, text="DALL Runner", font=("Arial", 30))
        self.btncommencer = Button(self.fenetre, text="COMMENCER",width=50,height=10, command=self.fenetre.quit)
        self.fenetre.title("DALLLRunner - Menu")
        self.fenetre.geometry("800x600")
        self.btncommencer.place(x=225,y=200)
        pass
    def lancerfenetre(self):
        self.titre.pack()
        self.fenetre.mainloop()
        pass