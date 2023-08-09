import random

class Marble(object):
    def __init__(self):
        x = random.randint(0,4)
        if x == 0:
            self.color = 'chartreuse'
        elif x == 1:
            self.color = 'periwinkle'
        elif x == 2:
            self.color = 'crimson'
        elif x == 3:
            self.color = 'wine purple'
        else:
            self.color = 'goldenrod'
        
    def getColor(self):
        return self.color

    def __str__(self):
        return self.color
    
        


class Jar(object):

    def __init__(self):
        self.marbles = []

    def addMarble(self,marble):
        'add a marble to the jar'
        self.marbles.append(marble)
        
    def getCount(self):
        'get a count of marbles'
        count = 0
        for marble in self.marbles:
            count += 1
        return count

    def getColors(self):
        'get a list of all the marble colors'
        allColors = []
        for marble in self.marbles:
            color = marble.getColor()
            allColors.append(color)
        return allColors

    def getColorCount(self,color):
        'get a count of how many marbles of a specifc color are in the jar'
        count = 0
        allColors = self.getColors()
        for colors in allColors:
            if colors == color:
                count += 1
        return count
            
        

    def __iter__(self):
        'return an iterator'
        return iter(self.marbles)


             
j=Jar()
for i in range(0,100):
    j.addMarble(Marble())


print(j.getColors())
print('Total red marbles : {}'.format(j.getColorCount('red')))

from tkinter import Label,Tk
class Sign(Tk):
    def __init__(self,lst=[],parent=None):
        Tk.__init__(self, parent)
        self.list = lst
        if len(self.list) == 3:
            self.title('Digital Sign')
        else:
            self.title('Warning')
        self.make_widgets()


    def make_widgets(self):
        if len(self.list) == 3:
            Label(self,text=self.list[0]).pack()
            Label(self,text=self.list[1]).pack()
            Label(self,text=self.list[2]).pack()
        else:
            Label(self,text='GREAT DEAL!').pack()
            Label(self,text='Android 1.0 Phones for $10!').pack()
            Label(self,text='Security vulnerabilities included!').pack()
        
        
        

Sign().mainloop()

