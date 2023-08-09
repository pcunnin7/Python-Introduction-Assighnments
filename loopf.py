def loopf():
    while True:
        try:
            num = int(input('Please enter a whole number: '))
            break
        except ValueError:
            print('Not a valid integer')
        except KeyboardInterrupt:
            print('You cheated . . . exiting . . .')
    return num
