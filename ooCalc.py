from tkinter import Tk, Label, Entry, Button, TOP, LEFT, RIGHT, END
from tkinter.messagebox import showinfo


class Calc(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Basic calculator')
        self.create_widgets()

    def evaluate(self):
        result = eval(self.ent.get())
        self.ent.delete(0,END)
        self.ent.insert(END, result)

    def create_widgets(self):
        Label(self, text="Enter an arithmetic expression:").pack(side=TOP)
        self.ent = Entry(self)
        self.ent.pack()
        Button(self, text="Evaluate", command=lambda: self.evaluate()).pack(side=LEFT)
        Button(self, text="Clear", command=lambda: self.ent.delete(0, END)).pack(side=RIGHT)
    
Calc().mainloop()
