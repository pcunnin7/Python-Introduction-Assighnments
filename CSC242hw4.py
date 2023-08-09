#I worked on this alone

import random

class Car (object):
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def __str__(self):
        return 'I am a {} {} made in {}.'.format(self.make,self.model,self.year)

    def __repr__(self):
        return "Car('{}','{}','{}')".format(self.make,self.model,self.year)
    
        
class Garage(object):
    'an object that contains cars'

    def __init__(self):
        'When a garage is created, an empty list is assigned to the variable self.garage'
        self.garage = []
        

    def __contains__(self,car):
        'Returns True if the garage contains and car that matches the make, model and year.'
        '''The variable match is assigned to a empty list. The variable make is assigned to the result of the getMake method of the parameter car,
the variable model is assigned to the result of the getModel method of the parameter car, and the
year variable is assigned to the result of the getYear method of the parameter car. The method then
iterates through the self.garage list, and checks to see if make, model, and year of the parameter car
is equal to the make, model, and year of the entry of self.garage. If all three are true for an entry in
garage, the entry is added to match. After iterating, the method checks if match is empty. If True, the method
returns False, otherwise the function returns True.'''
        match = []
        make = car.getMake()
        model = car.getModel()
        year = car.getYear()
        for i in self.garage:
            if make == i.getMake():
                if model == i.getModel():
                    if year == i.getYear():
                        match.append(i)
        if len(match) == 0:
            return False
        else:
            return True

    def getCarsBasedOnMake(self,make):
        'get a list of all the instances of the car object that match the make'
        '''the variable cars is assigned to an empty list. The method iterates through
the list self.garage and for each entry checks if the make of that entry is equal to parameter
make. If True, the entry is appended to the list cars. After iterating, the method returns cars'''
        cars = []
        for i in self.garage:
            if make == i.getMake():
                cars.append(i)
        return cars

    def getRandomCar(self):
        'returns a ranom car from the garage or None if the garage is empty'
        '''rand is assigned a random integer from 0 to the number of entries in cars -1.
The function then returns self.garage at rand'''
        rand = random.randint(0,(len(self.garage) -1))
        return self.garage[rand]

    def add(self,car):
        'add a car to the garage'
        '''The parameter car is added to the list self.garage'''
        self.garage.append(car)

    def __len__(self):
        'returns the number of entries in self.garage'
        return len(self.garage)

    def __str__(self):
        "return the string 'There are _ cars in the garage', formatted with the number of entries in self.garage"
        return ("There are {} cars in the garage".format(len(self.garage)))
    def __iter__(self):
        'Iterates through the list self.garage'
        return iter(self.garage)


from tkinter import Button, Entry, Label,Tk
from tkinter.messagebox import showinfo

class CookieOrderForm(Tk):

    def __init__(self,parent=None):
        'initializes a GUI with title Cookie Form and calls the function make widgets'
        Tk.__init__(self, parent)
        self.title('Cookie Form')
        self.make_widgets()

    def total(self):
        ''' Attempts to convert each entry to a float, if any are unsuccesful then creates an error popup,
then exits the function. If all are successful, then calculates the total cost by multiplying each entry
by the respective cost per cookie, then displays that total in popup titled Total'''
        try:
            chocolate = float(self.enter1.get())
        except:
            showinfo(title='Cookie Count', message = "Error. Incorrect value entered for Chocolate Chips count.")
            return
        try:
            oat = float(self.enter2.get())
        except:
            showinfo(title='Cookie Count', message = "Error. Incorrect value entered for Oatmeal count.")
            return
        try:
            oreo = float(self.enter3.get())
        except:
            showinfo(title='Cookie Count', message = "Error. Incorrect value entered for Oreo count.")
            return
        total = (chocolate * 1) + (oat * 1.5) + (oreo * 2)
        showinfo(title='Total', message="Your order total is ${:0.2f}.".format(total))
        

    def make_widgets(self):
        '''creates three labels located in column. Creates a label with the text 'Chocolate Chip ($1.00)' in
row 0, creates a label with the text 'Oatmeal ($1.50)' in row 1, creates a label with the text 'Oreo ($2.00)' in row 2.
Then creates three entry boxes of width 20 in column 1, in the rows 0, 1, 2. Then creates a button titled Order Total in row 3,
column 1 that calls the method total.'''
        Label(self, text="Chocolate Chip ($1.00)").grid(row = 0, column = 0)
        Label(self, text="Oatmeal ($1.50)").grid(row = 1, column = 0)
        Label(self, text="Oreo ($2.00)").grid(row = 2, column = 0)
        
        self.enter1 = Entry(self, width = 20)
        self.enter1.grid(row = 0, column = 1)
        self.enter2 = Entry(self, width = 20)
        self.enter2.grid(row = 1, column = 1)
        self.enter3 = Entry(self, width = 20)
        self.enter3.grid(row = 2, column = 1)

        Button(self, text="Order Total", command=self.total).grid(row = 3, column = 1)

CookieOrderForm().mainloop()
