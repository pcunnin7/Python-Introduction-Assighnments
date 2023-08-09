from tkinter import Tk
from tkinter.messagebox import showinfo

class Root(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self,parent)
        self.make_widgets()

    def handler(self,e):
        print('you left clicked at ({}, {})'.format(e.x, e.y))

    def handler2(self,ev):
        print('you right clicked at ({}, {})'.format(ev.x, ev.y))
        
    def make_widgets(self):
        self.bind("<Button-1>", self.handler)
        self.bind("<Button-3>", self.handler2)
        #self.bind("<Motion>",self.handler)

Root().mainloop()
    
