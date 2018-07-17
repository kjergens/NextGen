import random

print('Think of a number between 1 and 10 and I will guess it. Ready? Ok.')
computer_guess = random.randint(1, 10)
answer = input("Is it " + str(computer_guess) + "? ")

# Variables to keep track of the game
turn = 1
old_guesses = (computer_guess,)  # store the first one  # NEW

# Continue to play while the player says 'no' and while the turn did not reach 3.
while answer.lower() == 'no' and turn < 10:

    # Computer picks random number. Keep picking until it's not in old guesses
    computer_guess = random.randint(1, 10)
    while computer_guess in old_guesses:              # NEW
        computer_guess = random.randint(1, 10)        # NEW

    print(old_guesses)  # testing

    # Save
    old_guesses = old_guesses + (computer_guess,)     # NEW

    answer = input("Is it " + str(computer_guess) + "? ")

    # Increment the turn.
    turn = turn + 1

if turn < 3:
    print("I won!")
else:
    print("I ran out of turns.")
