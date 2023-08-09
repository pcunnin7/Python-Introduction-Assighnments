from tkinter import Label,PhotoImage,Tk

class HelloWorldImage(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.minsize(width=500,height=200)
        self.title('Hello World Image!')
        self.make_widgets()

    def make_widgets(self):
        self.photo = PhotoImage(file='peace.gif')
        widget = Label(self, image = self.photo)
        widget.pack()

HelloWorldImage().mainloop()
