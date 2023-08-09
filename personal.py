from tkinter import Tk, Label, Entry, Button, TOP, LEFT
from tkinter.messagebox import showinfo


class Reply(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Echo')
        self.make_widgets()

    def reply(self,name):
        showinfo(title='Reply', message='Hello {}!'.format(name))
    
    def cmd(self):
        self.reply(self.ent.get())
        
    def make_widgets(self):
        Label(self, text="Enter your name:").pack(side=TOP)
        self.ent = Entry(self)
        self.ent.pack(side=TOP)

        btn=Button(self, text="Submit", command=self.cmd)
        btn.pack(side=LEFT)

Reply().mainloop()

