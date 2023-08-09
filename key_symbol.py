from tkinter import Tk, Text

class Reporter(Tk):

    def __init__(self,parent=None):
        Tk.__init__(self, parent)
        self.title('Keysym Logger')
        self.make_widgets()

    def reportEvent(self,event):
        #print(type(event))
        print('keysym={}, keysym_num={}'.format(event.keysym, event.keysym_num))

    def make_widgets(self):
        text=Text(self, width=20, height=5, highlightthickness=2)
        text.bind('<KeyPress>', self.reportEvent)
        text.pack(expand=1, fill="both")

Reporter().mainloop()
