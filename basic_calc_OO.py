from tkinter import Tk, Label, Entry, Button, TOP, LEFT, RIGHT, END
from tkinter.messagebox import showinfo

class BasicCalc(Tk):
    'a basic calculator class'

    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.title('Basic calculator')
        self.make_widgets()

    def evaluate(self):
        try:
            result = eval(self.ent.get())
            self.ent.delete(0,END)
            self.ent.insert(END, result)
        except:
            showinfo(title='Error', message="Please enter a valid expression.")
            self.ent.delete(0, END)

    def make_widgets(self):
        Label(self, text="Enter an arithmetic expression:").grid(row=0, column=0, columnspan=2)

        self.ent = Entry(self)
        self.ent.grid(row=1, column=0, columnspan=2)

        Button(self, text="Evaluate", command=self.evaluate).grid(row=2, column=0)
        Button(self, text="Clear", command=lambda: self.ent.delete(0, END)).grid(row=2, column=1)
        
BasicCalc().mainloop()

