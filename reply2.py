from tkinter import Button, Tk
from tkinter.messagebox import showinfo

class Reply(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Reply')
        self.make_widgets()

    # The event-handler for button clicks
    def reply(self,txt):
        showinfo(title='Button', message='Button{} pressed!'.format(txt))
    
    def make_widgets(self):
        b1 = Button(self, text="00", width = 10, command=lambda:self.reply('00'))
        b1.grid(row=0,column=0)
        Button(self, text="01", width = 10, command=lambda:self.reply('01')).grid(row=0,column=1)
        Button(self, text="10", width = 10, command=lambda:self.reply('10')).grid(row=1,column=0)
        Button(self, text="11", width = 10, command=lambda:self.reply('11')).grid(row=1,column=1)

Reply().mainloop()
