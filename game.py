import random

N = int(input('How many Questions? '))

def game(n):
    correct = 0
    for digit in range(n):
        x = random.randint(0,9)
        y = random.randint(0,9)
        z = x + y
        answer = input(str(x) + ' + ' +str(y) + ' = ')
        while True:
            try:
                a = int(answer)
            except ValueError:
                print('Please enter a valid number')
                answer = input(str(x) + ' + ' +str(y) + ' = ')
            else:
                break
        if a == z:
            print('Correct')
            correct += 1
        elif a != z:
            print('Incorrect')
            
    print('Correct Answers: ' + str(correct))


game(N)
