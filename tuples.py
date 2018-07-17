my_tuple = ("Katie", "Jared", "Shane", "Sophia", "Kendrick")

print(my_tuple.count("Kendrick"))
print(my_tuple.index("Sophia"))

# Compare strings and tuples
# name = "Valentina"
my_tuple = ("Jared", "Sophia", "Will", "Donna", "Jordan", "Isaac", "Kendrick", "Elliot", "Jared", "Ryan")
#
# print(name[0])
# print(my_tuple[0])
#
# print(name[4:6])
# print(my_tuple[4:6])
#
# print(len(name))
# print(len(my_tuple))
#
# if "V" in name:
#     print("Found a V!")
#
# if "Will" in my_tuple:
#     print("Found Will!")
#
# print(my_tuple.count("Jared"))
# print(name.count("a"))
#
# print(my_tuple.index("Sophia"))
# print(name.index("e"))
#
# for c in name:
#     print(c)
#
# width = int(input("How wide should this be?"))
# for y in range(9):
#     # Print a row of stars
#     for x in range(width):
#         print("*", end=' ', flush=True)
#     # Print new line at the end
#     print("")   # Marks end of row

# Concatenating
# tuple_one = (9, 3, 4)
# tuple_two = (3, 4, 5)
# combined_tuple = tuple_one + tuple_two
# print(combined_tuple)

# In a for-loop
# for person in my_tuple:
#     print(person)

# Splitting text - Turning a string into a tuple
# text = "How are you today good sir? I hope you are well."
# t_tuple = tuple(text.split())
# print(t_tuple)
# print(t_tuple.count("you"))
# t_set = set(t_tuple)
# print("There are", len(t_set), "words in that text")

# for person in "Jared", "Sophia", "Will", "Donna", "Jordan", "Isaac", "Kendrick", "Elliot", "Jared", "Ryan":
#     print(person)

# You can assign two things at once
# x, y = (10, 30)
# reallife example, getting filenames without the extension
import os
filename, extension = os.path.splitext("Hello.txt")
print(filename)
'Hello'
print(extension)
'.txt'

# Make a word a plural
# See namefixer for a practice
# Print all the unique file extensions
# print("These are the types of files you have on your Desktop:")
# extensions = ()
# for f in os.listdir('/Users/kjergens/Desktop'):
#     filename, extension = os.path.splitext(f)
#     if extension not in extensions:
#         extensions += (extension,)
#         print(extension)


# Practice
# Raffle winner - get a random winner from a tuple of names.
#
# Sort the names (use the built-in function)
#
# Reverse sort the names (use the built-in function)
#
# Use a for loop with a tuple to tell these people how many letters are in their names.
#
# Read this text and say how many instance if the word 'the' there is.
#
# How many unique words are in HP?
#
# Capitalize every name and print to a file called names.txt.
#
# Count words in text:
#  Say how frequently the word "you" appears and how frequently the word "I" appears.
#
# magic 8 ball
#
# food-o-matic
#
# update backwardguessing game (problems_loops_set1) so that the computer doesn't use the same guess twice.
#   HINT: use a tuple to save the old guesses and check that the computer's guess is not in it.
#   HINT2: concatenate tuples
#
# Hangman



