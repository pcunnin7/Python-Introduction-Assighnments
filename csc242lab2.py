import random
class Die(object):
    'a class representing a Die'
    def __init__(self, sides=6):
        'initialize a die, default 6 sides'
        self.Sides = sides

    def roll(self):
        'roll the dice'
        self.value = random.randint(1,self.Sides)

    def get(self):
        'get the current value of the die'
        return self.value
        

    def numSides(self):
        'get the number of sides of the die'
        return self.Sides

    def __str__(self):
        'get the string representation of the die'
        return '{}'.format(self.Sides)

    def __repr__(self):
        'get the python representation of the die'
        return "Die({})".format(self.Sides)

def rollDice(rolls, sides):
    count = 0
    d1 = Die(sides)
    d2 = Die(sides)
    for roll in range(rolls):
        d1.roll()
        d2.roll()
        print('Roll ' + str(count) + ' : ' + str(d1.get()) + ' - ' + str(d2.get()))
        count +=1
        
   
        
