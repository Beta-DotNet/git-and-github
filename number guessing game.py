import random

random_number = random.randint(1, 100)
count = 0
guess = int(input("Guess any number between 1 and 100: "))

while guess != random_number:
    if guess > random_number:
        print("Too High")
    else:
        print("Too Low")
        count =+ 1
    guess = int(input("Guess any number between 1 and 100: "))

print("You have succesfully guessed the right number after " + count + " times")
