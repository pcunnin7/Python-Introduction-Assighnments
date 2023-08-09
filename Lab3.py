class Stat(object):
    'a stat class'
    
    def __init__(self,l=[]):
        'constructor accepting a list'
        self.list = l
        

    def sum(self):
        'sum of all values in Stat'
        Sum = 0
        for num in self.list:
            Sum += num
        return Sum

    def max(self):
        'largest value in stat'
        if len(self.list) > 0:
            return max(self.list)
        if len(self.list) == 0:
            return 0.0

    def min(self):
        'smallest value in stat'
        if len(self.list) > 0:
            return min(self.list)
        if len(self.list) == 0:
            return 0.0

    def clear(self):
        'remove all items from stat'
        return self.list.clear()

    def mean(self):
        'mean of all values in stat'
        if len(self.list) > 0:
            mean = self.sum() / len(self.list)
            return mean
        if len(self.list) == 0:
            return 0.0

    def add(self,val):
        'add a value to Stat. must be a number'
        if type(val) == int or type(val) == float:
            self.list.append(val)
        else:
            return('{} not added. Value must be a number'.format(val))
        
    

    def __eq__(self,other):
        'returns True if the sum of the two Stat objects is equal'
        om = other.sum()
        if om == self.sum():
            return True
        else:
            return False

    def __str__(self):
        'string representation of stat'
        return('Stat object with {} items.'.format(len(self.list)))

    def __repr__(self):
        'python representation of object'
        return str(self.list)
