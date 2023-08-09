from tkinter import Label, Tk
#import tkinter

class HelloWorld(Tk):

    def __init__(self,somedata='Some value', parent=None):
        Tk.__init__(self,parent)
        self.somedata=somedata
        self.title('Hello World!')
        self.make_widgets()

    def make_widgets(self):
        Label(self,text='Hello in class world!').pack()
        Label(self,text='More text').pack()
        Label(self,text=self.somedata).pack()

HelloWorld().mainloop()
