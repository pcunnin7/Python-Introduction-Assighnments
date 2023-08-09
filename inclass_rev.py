class revListIter(object):
    def __init__(self,lst):
        self.ilst = lst
        self.index = len(lst) - 1
        
    def __next__(self):
        if self.index == -1:
            raise StopIteration()
        val = self.ilst[self.index]
        self.index = self.index - 1
        return val
        

class revList(list):
    def printName(self):
        print('Pat')
    def __iter__(self):
        return revListIter(self)
