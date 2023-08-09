from tkinter import Tk, Label, Entry, Button, TOP, LEFT, RIGHT, END
from tkinter.messagebox import showinfo


class Calc(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Basic calculator')
        self.create_widgets()

    def evaluate(self):
        pass

    def create_widgets(self):
        pass

Calc().mainloop()
