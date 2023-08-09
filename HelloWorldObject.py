from tkinter import Label,Tk

class HelloWorld(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Hello World!')
        self.make_widgets()


    def make_widgets(self):
        widget=Label(self,text='Hello GUI World!')
        widget.pack()

HelloWorld().mainloop()
