from tkinter import Tk,Scale,Label,PhotoImage,HORIZONTAL


class HappyScale(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.minsize(width=500,height=200)
        self.title('Happy Scale')
        self.make_widgets()

    def updateImage(self,event):
        val=self.slider.get()
        if val>=0 and val<5:
            self.photo = PhotoImage(file='happy.gif')
        elif val>=5 and val<8:
            self.photo = PhotoImage(file='ok.gif')
        else:
            self.photo = PhotoImage(file='sad.gif')
        self.label.configure(image=self.photo)
    
    def make_widgets(self):
        self.photo = PhotoImage(file='happy.gif')
        self.label = Label(self, image = self.photo)
        self.label.pack()
        self.slider = Scale(self, from_=0, to=10,orient=HORIZONTAL, command=self.updateImage)
        self.slider.pack()

HappyScale().mainloop()
