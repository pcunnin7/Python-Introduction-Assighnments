
    
def printTriangleManually3():
    print((' ' * 2) + ('*' * 2))
    
def printTriangleManually2():
    print((' ' * 1) + ('*' * 4))
    printTriangleManually3()
    
def printTriangleManually():
    print((' ' * 0) + ('*' * 6))
    printTriangleManually2()

printTriangleManually()

def printTriangleTop(m,i):
    if m <= 0:
        return
    else:
        print((' ' * i) + ('*' * m))
        printTriangleTop(m -2,i+1)

def printTriangleBottom(m,i):
    if m <= 0:
        return
    else:
        printTriangleBottom(m -2,i+1)
        print((' ' * i) + ('*' * m))
