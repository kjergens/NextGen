import random

secret_num = random.randint(1, 10)

guess = int(input("Guess number 1 - 10: "))
wrong_guesses = []  # a list (so we can add to it)

while guess != secret_num:
    wrong_guesses.append(guess)
    if guess > secret_num:
        print("Too high.", end=' ')
    else:
        print("Too low.", end=' ')
    guess = int(input("Guess number 1 - 10: "))

print("You won! The number was", secret_num)
