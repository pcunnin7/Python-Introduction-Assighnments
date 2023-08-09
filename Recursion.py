lst = [1,2, 'a', 'b', 'some string',2.5]

def printNum(L):
    if L ==[]:
        return
    else:
        if type(L[0]) == int or type(L[0]) == float:
            print(L[0])
        printNum(L[1:])
            
        


def recLenL(L):
    if L == []:
        return 0
    else:
        return 1 + recLenL(L[1:])
        

def printL(L):
    #base case / end base - How do we know we are done
    if len(L) == 0:
        return
    #recursive step - How do we reduce the problem
    else:
        print(L[0])
        printL(L[1:])

def vertical(n):
    if n < 10:
        print(n)
    else:
        x = n % 10
        print(x)
        y = n // 10
        vertical(y)
