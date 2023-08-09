from tkinter import Tk, Label, Entry, Button, TOP, LEFT
from tkinter.messagebox import showinfo

class Reply(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Echo')
        self.make_widgets()
        
    def make_widgets(self):
        Label(self, text="Enter your name:").pack(side=TOP)
        self.ent = Entry(self)
        self.ent.pack(side=TOP)

        btn=Button(self, text="Submit", command=lambda:  showinfo(title='Reply', message='Hello {}!'.format(self.ent.get())))
        btn.pack(side=LEFT)

Reply().mainloop()
