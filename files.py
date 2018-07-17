file = open('hp.txt', 'r')

text = file.read()

#print(text)

text = text.lower()

# Remove punctuation
text = text.replace('.', '')
text = text.replace(',', '')
text = text.replace('!', '')
text = text.replace(';', '')
text = text.replace(':', '')
text = text.replace('?', '')
text = text.replace('"', '')

# # Male references
# print(text.count(" he ") + text.count(" him ") + text.count(" his "))
#
# # Female references
# print(text.count(" she ") + text.count(" her ") + text.count(" hers "))

m_count = 0
male_pronouns = ('he', 'him', 'his')
for m in male_pronouns:
    m_count = m_count + text.count(' ' + m + ' ')  # Pad with spaces so we don't count "The", "She", etc.

f_count = 0
female_pronouns = ('she', 'her', 'hers')
for f in female_pronouns:
    f_count = f_count + text.count(' ' + f + ' ')  # Pad with spaces so we don't count "The", "She", etc.

print("Male pronouns:", m_count)
print("Female pronouns:", f_count)

text = tuple(text.split())
text = sorted(text)
print("There are", len(text), "words total.")

unique_words = set(text)  # Turn the tuple into a set
print("There are", len(unique_words), "unique words.")

# Count all the words
for word in unique_words:
    print(word, ":", text.count(word))

# bonus: get most frequent word.
# You can remove words from sets
unique_words.remove("theΩ")
max_count = 0
for word in unique_words:
    if text.count(word) > max_count:
        max_count = text.count(word)
        max_word = word
print("Most frequent word is", max_word, "with", max_count, "occurrences")


