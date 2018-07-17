import random

# Simple guessing game with while loop

secret_num = random.randint(1, 10)
guess = int(input('Guess 1-10: '))

while guess != secret_num:
    guess = int(input('Wrong. Guess again: '))

print('Yes! You win! The number was', secret_num)
