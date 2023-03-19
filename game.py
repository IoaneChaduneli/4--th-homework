import random

while True:
    n = int(input("Level: "))
    if n < 0:
        continue
    number = random.randint(1,n)

    guess = int(input("Guess: "))
    
    if guess < 0:
        continue
    elif guess < number:
        print("Too small")
    elif guess > number: 
        print("Too large")
    elif guess == number:
        print("Just right")
        exit()