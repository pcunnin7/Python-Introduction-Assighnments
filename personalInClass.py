from tkinter import Tk, Label, Entry, Button, TOP, LEFT
from tkinter.messagebox import showinfo

class Personal(Tk):
    'a personalized hello'

    def __init__(self, parent = None):
        'the constructor'
        # Call the parent constructor!!!!
        Tk.__init__(self, parent)
        self.title('Echo')
        self.main() # Create the widgets

    def main(self):
        'make the widgets and put them into the window'
        
        Label(self, text="Enter your name:").pack(side=TOP)

        self.ent = Entry(self)
        self.ent.pack(side=TOP)

        btn=Button(self, text="Submit", command=self.reply)

        btn.pack(side=LEFT)

    def reply(self):
        showinfo(title='Reply', message='Hello {}!'.format(self.ent.get()))



