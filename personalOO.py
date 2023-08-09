from tkinter import * #Tk, Label, Entry, Button, TOP, LEFT, END
from tkinter.messagebox import showinfo

class Personal(Tk):

    def __init__(self, parent=None):
        Tk.__init__(self, parent)
        self.title('Echo')
        self.make_widgets()
        
    def reply(self, name):
        showinfo(title='Reply', message='Hello {}!'.format(name))
        # Clear the entry
        self.ent.delete(0, END)

    # Define the main function
    def make_widgets(self):

        Label(self, text="Enter your name:").pack(side=TOP)

        self.ent = Entry(self)
        self.ent.pack(side=TOP)
        # Change the focus to the entry
        self.ent.focus_set()

        #cmd = lambda: reply(ent.get())
        def cmd():
            return self.reply(self.ent.get())

        btn=Button(self, text="Submit", command=cmd)

        btn.pack(side=LEFT)

# Call the mainloop on an object from the class
Personal().mainloop()
