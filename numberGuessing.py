import random

guess = -1
answer = str(random.randint(1, 100))
guessCount = 0
while guess != answer and guess != 'quit':
    guess = input("Pick a number between 1 and 100 ")
    guessCount += 1
    if guess > answer:
        print("too high")
    elif guess < answer:
        print("too low")

    if guessCount > 10:
        print("Type quit at any time to stop playing")
    if guessCount > 20:
        break
if guess == answer:
    print("You got it!")

elif guess == "quit":
    print("Thanks for playing better luck next time")
else:
    print("Number of tries exceded")
