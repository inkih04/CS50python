import random
import sys

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n > 0:
            randomN = random.randint(1, n)
            break
while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess == randomN:
            print("Just right!")
            break
        elif guess < randomN:
            print("Too small!")
        else:
            print("Too large!")