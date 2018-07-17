import random

wordlist = ('happy',)
word = random.choice(wordlist)
correct_guesses = ()  # empty tuple to hold correct guesses
num_turns = 0
all_letters = ()    # empty tuple to hold guesses

print(word)

for letter in word:
    print("_", end=' ')

print()
player_letter = input("\nGuess a letter")
player_letter = player_letter.lower()  # make the case not matter
all_letters += (player_letter,)     # save the guess

# Check for correct answer
if player_letter in word:
    print('Good guess!')
    correct_guesses += (player_letter,)  # saves correct answer

# Prints the board
for w in word:
    if w in correct_guesses:
        print(w, end=' ')
    else:
        print('_', end=' ')

while len(word) > len(correct_guesses) and num_turns < 6:
    num_turns += 1   # count the turn

    print()
    print(num_turns)

    print("You have already guessed", all_letters)

    player_letter = input("\nGuess a letter: ")

    # Don't let them repeat guesses
    while player_letter in all_letters:
        print("you guessed that already!")
        player_letter = input("\nGuess a letter: ")

    player_letter = player_letter.lower()  # make the case not matter
    all_letters += (player_letter,)  # save the guess

    # Check for correct answer
    if player_letter in word:
        print('Good guess!')
        correct_guesses += (player_letter,)  # saves correct answer

    # Prints the board
    for w in word:
        if w in correct_guesses:
            print(w, end=' ')
        else:
            print('_', end=' ')

# Tell them if they won or lost
if len(word) > len(correct_guesses):
    print("\nSorry you lost. The word was", word)
else:
    print("\nYou got it!!")
