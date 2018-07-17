import nltk
import random
from matplotlib import pyplot

# Open file
with open('/Users/kjergens/Desktop/harrypotter.txt', 'r') as file:
    text = file.read()

# # Make lowercase
tlist = []
text = text.lower()

# Print how many words
print(len(tlist))

# How many times Harry appears
print("Harry appears:", tlist.count('harry'))
print("Hermione appears:", tlist.count('hermione'))
print("Ron appears:", tlist.count('ron'))

ulist = list(set(tlist))
# Print how many unique words
print("Unique word count:", len(ulist))

ulist.sort()
adverbs = [word for word in ulist if word.endswith('ly')]
hyphenated = [word for word in ulist if '-' in word]
s_words = [word for word in ulist if word.startswith('s')]
gerunds = [word for word in ulist if word.endswith('ing')]
cap_names = [word.capitalize() for word in ulist if word in ('harry', 'ron', 'hermione', 'hagrid', 'uncle vernon', 'aunt petunia', 'dudley')]

print(adverbs)
print(hyphenated)
print(s_words)
print(gerunds)
print(cap_names)
print(random.choice(gerunds), random.choice(adverbs))

rword = random.choice(adverbs)
print("Random word:", rword, 'appears', tlist.count(rword), "time(s).")

pyplot.bar(['total words', 'unique words'], [len(tlist), len(ulist)])
pyplot.show()


pyplot.scatter(['total words', 'unique words'], [len(tlist), len(ulist)])
pyplot.show()


pyplot.plot(['total words', 'unique words'], [len(tlist), len(ulist)])
pyplot.show()