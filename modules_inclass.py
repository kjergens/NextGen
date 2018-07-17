import random

secret = random.randint(1,10)
guess = random.randint(1,10)
print("the guess is", guess)

if secret == guess:
    print("Win!")
else:
    print("You lose. You are off by", abs(secret-guess))
    if guess < secret:
        print("too low")
    else:
        print("too high")

print("The number was", secret)

