import random

# Hangman in 11 steps

# Part 1:
# secret_words = ("dog", "cat", "bird")
#
# secret_word = random.choice(secret_words)
#
# print("The secret word is", secret_word)

# Part 2:
# word_list = ("dog", "cat", "bird")
# secret_word = random.choice(word_list)
#
# print("The secret word is", secret_word)
#
# for c in secret_word:
#     print("_ ", end='')
# print("\n")

# Part 3:
# word_list = ("dog", "cat", "bird")
# secret_word = random.choice(word_list)
#
# print("The secret word is", secret_word)
# guess = input("Guess a letter")
# if guess in secret_word:
#     print("Correct!")

# Part 4:
# word_list = ("dog", "cat", "bird")
# secret_word = random.choice(word_list)
#
# print("The secret word is", secret_word)
# # First board printing
# for c in secret_word:
#     print("_ ", end='')
# print("\n")

# taken_letters = ()
# guess = input("Guess a letter")
# if guess in secret_word:
#     print("Correct!")
#     correct_letters = correct_letters + (guess,)

# Part 5: make the case not matter
# word_list = ("dog", "cat", "bird")
# secret_word = random.choice(word_list).lower()
# print("The secret word is", secret_word)
# # First board printing
# for c in secret_word:
#     print("_ ", end='')
# print("\n")
# correct_letters = ()
# guess = input("Guess a letter").lower()
# if guess in secret_word:
#     print("Correct!")
#     correct_letters = correct_letters + (guess,)

# Part 6
# word_list = ("dog", "cat", "bird")
# secret_word = random.choice(word_list)
#
# print("The secret word is", secret_word)
# # First board printing
# for c in secret_word:
#     print("_ ", end='')
# print("\n")
# correct_letters = ()
# guess = input("Guess a letter").lower()
# if guess in secret_word:
#     print("Correct!")
#     correct_letters = correct_letters + (guess,)
#
# for c in secret_word:
#     if c in correct_letters:
#         print(c, end=' ')
#     else:
#         print("_ ", end='')
# print("\n\n")

# Part 7
# word_list = ("dog", "cat", "bird")
# secret_word = random.choice(word_list)
#
# print("The secret word is", secret_word)
#
# # First board printing
# for c in secret_word:
#     print("_ ", end='')
# print("\n")
# correct_letters = ()
# while len(correct_letters) < len(secret_word):
#     guess = input("Guess a letter: ").lower()
#
#     # Check the guess
#     if guess in secret_word:
#         print("Correct!")
#         correct_letters = correct_letters + (guess,)
#
#     # Print the word
#     for c in secret_word:
#         if c in correct_letters:
#             print(c, end=' ')
#         else:
#             print("_ ", end='')
#     print("")
#
# print("You won!")


# # Part 8
# word_list = ("dog", "cat", "bird")
# secret_word = random.choice(word_list)
#
# print("The secret word is", secret_word)
#
# # First board printing
# for c in secret_word:
#     print("_ ", end='')
# print("\n")
# correct_letters = ()
# guesses = 0
# while len(correct_letters) < len(secret_word) and guesses < 6:
#     guess = input("Guess a letter: ").lower()
#
#     # Check the guess
#     if guess in secret_word:
#         print("Correct!")
#         correct_letters = correct_letters + (guess,)
#
#     # Print the word
#     for c in secret_word:
#         if c in correct_letters:
#             print(c, end=' ')
#         else:
#             print("_ ", end='')
#     print("")
#
#     guesses += 1
#
# if guesses < 6:
#     print("You won!")
#
# print("Game over. The word is", secret_word)

# unique words

# Part 9 - BONUS show wrong guesses
# word_list = ("dog", "cat", "bird")
# secret_word = random.choice(word_list)
#
# print("The secret word is", secret_word)

# # First board printing
# for c in secret_word:
#     print("_ ", end='')
# print("\n")

# correct_letters = ()
# all_letters = ()
# while len(correct_letters) < len(secret_word):
#     # Get next guess
#     print("You have already guessed", all_letters)
#     guess = input("Guess a letter: ").lower()
#
#     # Check the guess
#     if guess in secret_word:
#         print("Correct!")
#         correct_letters += (guess,)
#
#     all_letters += (guess,)
#
#     # Print the word so they can guess again
#     for c in secret_word:
#         if c in correct_letters:
#             print(c, end=' ')
#         else:
#             print("_ ", end='')
#     print("")
#
# print("You won!")

# Part 10 - don't let them repeat a guess
# word_list = ("dog", "cat", "bird")
# secret_word = random.choice(word_list)
#
# print("The secret word is", secret_word)

# # First board printing
# for c in secret_word:
#     print("_ ", end='')
# print("\n")

# correct_letters = ()
# all_letters = ()
# while len(correct_letters) < len(secret_word):
#     # Get next guess
#     print("You have already guessed", all_letters)
#     guess = input("Guess a letter: ").lower()
#
#     while guess in all_letters:
#         guess = input("You already guessed that. Guess again:").lower()
#
#     # Check the guess
#     if guess in secret_word:
#         print("Correct!")
#         correct_letters += (guess,)
#
#     all_letters += (guess,)
#
#     # Print the word so they can guess again
#     for c in secret_word:
#         if c in correct_letters:
#             print(c, end=' ')
#         else:
#             print("_ ", end='')
#     print("")
#
# print("You won!")

# # Part 11 - Pick a random word from a large text. Remove punctuation first
# file = open("hp.txt", "r")
# file = open("/Users/kjergens/Desktop/harrypotterbook1.txt", "r")
# all_text = file.read()
# all_text.replace(',', ' ')
# all_text.replace('.', ' ')
# all_text.replace('!', ' ')
# all_text.replace('?', ' ')
# all_text.replace('"', '')
# all_text.replace("'", '')
# word_list = all_text.split()
# secret_word = random.choice(word_list).lower()
# print(secret_word)
# correct_letters = ()
# all_letters = ()
#
# # First board printing
# for c in secret_word:
#     print("_ ", end='')
# print("\n")
#
# while len(correct_letters) < len(secret_word):
#     # Get next guess
#     print("You have already guessed", all_letters)
#     guess = input("Guess a letter: ").lower()
#
#     while guess in all_letters:
#         guess = input("You already guessed that. Guess again:").lower()
#
#     # Check the guess
#     if guess in secret_word:
#         print("Correct!")
#         correct_letters += (guess,)
#     else:
#         print("Incorrect.")
#
#     all_letters += (guess,)
#
#     # Print the word so they can guess again
#     for c in secret_word:
#         if c in correct_letters:
#             print(c, end=' ')
#         else:
#             print("_ ", end='')
#     print("")
#
# print("You won!")

# # Part 11 - 6 wrong guesses max and don't print the secret word.
# # Get secret word
# import urllib.request
# url = "http://www.gutenberg.org/files/43/43-0.txt"
# page = urllib.request.urlopen(url)
# all_text = page.read().decode("UTF-8")
# #file = open("/Users/kjergens/Desktop/harrypotterbook1.txt", "r")
# #all_text = file.read()
# all_text = all_text.replace(',', ' ')
# all_text = all_text.replace('.', ' ')
# all_text = all_text.replace('!', ' ')
# all_text = all_text.replace('?', ' ')
# all_text = all_text.replace('"', '')
# all_text = all_text.replace("'", '')
# all_text = all_text.replace("(", '')
# all_text = all_text.replace(")", '')
# word_list = all_text.split()
# secret_word = random.choice(word_list).lower()
#
# # Variables for tracking
# correct_letters = ()
# all_letters = ()
# wrong_guess = 0
#
# # First board printing
# for c in secret_word:
#     print("_ ", end='')
# print("\n")
#
# num_secret_letters = len(set(secret_word))
#
# while len(correct_letters) < num_secret_letters and wrong_guess < 6:
#     # Get next guess
#     print(6-wrong_guess, "turns to go. Guess a letter. You have already guessed", all_letters, ":", end=' ')
#     guess = input().lower()
#
#     while guess in all_letters:
#         guess = input("You already guessed that. Guess again: ").lower()
#
#     # Check the guess
#     if guess in secret_word:
#         print("Correct!")
#         correct_letters += (guess,)
#     else:
#         print("Incorrect.")
#         wrong_guess+=1
#
#     all_letters += (guess,)
#
#     # Print the word so they can guess again
#     for c in secret_word:
#         if c in correct_letters:
#             print(c, end=' ')
#         else:
#             print("_ ", end='')
#     print("")
#
#
# if len(correct_letters) == len(secret_word):
#     print("You won!")
# else:
#     print("You lose. The secret word was ", secret_word, ".", sep='')


# Part 11 - 6 wrong guesses max and don't print the secret word.
# Get secret word
import urllib.request
url = "http://www.gutenberg.org/files/43/43-0.txt"
page = urllib.request.urlopen(url)
all_text = page.read().decode("UTF-8")
#file = open("/Users/kjergens/Desktop/harrypotterbook1.txt", "r")
#all_text = file.read()
all_text = all_text.replace(',', ' ')
all_text = all_text.replace('.', ' ')
all_text = all_text.replace('!', ' ')
all_text = all_text.replace('?', ' ')
all_text = all_text.replace('"', '')
all_text = all_text.replace("'", '')
all_text = all_text.replace("(", '')
all_text = all_text.replace(")", '')
all_text.replace(' a ', '')
all_text.replace(' the ', '')
all_text.replace(' of ', '')
word_list = all_text.split()
word_list = tuple(set(word_list))
secret_word = random.choice(word_list).lower().strip()

# Variables for tracking
correct_letters = ()
all_letters = ()
wrong_guess = 0

# First board printing
for c in secret_word:
    print("_ ", end='')
print("\n")

num_secret_letters = len(set(secret_word))

while len(correct_letters) < num_secret_letters and wrong_guess < 6:
    # Get next guess
    print(6-wrong_guess, "turns left. You have already guessed", all_letters, ":", end=' ')
    guess = input().lower()

    while guess in all_letters:
        guess = input("You already guessed that. Guess again: ").lower()

    # Check the guess
    if guess in secret_word:
        print("Correct!")
        correct_letters += (guess,)
    else:
        print("Incorrect.")
        wrong_guess += 1

    all_letters += (guess,)

    # Print the word so they can guess again
    for c in secret_word:
        if c in correct_letters:
            print(c, end=' ')
        else:
            print("_ ", end='')
    print("")


if len(correct_letters) == len(set(secret_word)):
    print("You won!")
else:
    print("You lose. The secret word was ", secret_word, ".", sep='')
