from tkinter import Button, Tk
from tkinter.messagebox import showinfo

class Reply(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Reply')
        self.make_widgets()

    # The event-handler for button clicks
    def reply(self):
        showinfo(title='Button', message='Button pressed!')
    
    def make_widgets(self):
        Button(self, text="Press here", command=self.reply).pack()

Reply().mainloop()
