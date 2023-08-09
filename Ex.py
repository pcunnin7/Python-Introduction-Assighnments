from tkinter import Tk, Text

class Reporter(Tk):
    def __init__(self, parent = None):
        Tk.__init__(self,parent)
        self.title('Keysym Logger')
        self.make_widgets()

    def reportEvent(self, event):
        print('Keysym = {}. keysym_num = {}'.format(event.keysym,event.
