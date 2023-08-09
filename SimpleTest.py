

from tkinter import Button, Entry, Label,Tk,TOP,LEFT,RIGHT,END
from tkinter.messagebox import showinfo

class SimpleEntry(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Entry Test')
        self.make_widgets()

    def press(self):
        #get the value from the entry box.
        value=self.entry.get()
        if value=='':
            showinfo(title='Error', message='Must enter a value')
            #return
        if value=='0':
            showinfo(title='Error', message='Come on put more than 0')
            #return
        #clear entry box
        self.entry.delete(0,END)
        #add text to entry box.
        self.entry.insert(END, "See how this got here?")

    def make_widgets(self):
        #keep a reference to entry for later use.
        self.entry = Entry(self, width=40)
        self.entry.pack()

        Button(self, text="Press Me", command=lambda:self.press()).pack()


SimpleEntry().mainloop()
