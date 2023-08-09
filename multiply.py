import random

N = int(input('How many Questions? '))

def game(n):
    correct = 0
    for digit in range(n):
        x = random.randint(0,20)
        y = random.randint(0,20)
        s = random.randint(1,3)
        if s == 1:
            math = ' x '
            z = x * y
        if s == 2:
            math = ' - '
            z = x - y
        if s == 3:
            math = ' + '
            z = x + y
        answer = input(str(x) + math +str(y) + ' = ')
        while True:
            try:
                a = float(answer)
            except ValueError:
                print('Please enter a valid number')
                answer = input(str(x) + math +str(y) + ' = ')
            else:
                break
        if a == z:
            print('Correct')
            correct += 1
        elif a != z:
            print('Incorrect')
            
    print('Score: ' + str(correct) + ' out of ' + str(n))


game(N)
