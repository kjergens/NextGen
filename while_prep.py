import random

# Simple guessing game
secret_num = random.randint(1, 10)
guess = int(input('Guess 1-10: '))

# If wrong, give them a second guess


print ('The number was', secret_num)