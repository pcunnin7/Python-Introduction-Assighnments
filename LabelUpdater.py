from tkinter import Button, Entry, Label,Tk
from tkinter.messagebox import showinfo

class LabelUpdater(Tk):
    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Label Updater GUI')
        self.count=0
        self.make_widgets()
        self.updateUI()

    def updateUI(self):
        self.totalClicksValue.config(text=str(self.count))

    def click(self):
        self.count+=1
        self.updateUI()
        
    def make_widgets(self):
        Label(self,text='Total Clicks:').pack()
        self.totalClicksValue = Label(self,text='')
        self.totalClicksValue.pack()
        Button(self, text="Click", command=lambda:self.click()).pack()

LabelUpdater().mainloop()
