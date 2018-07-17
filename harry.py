import random
import time
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# import urllib.request
#
# url = 'https://www.gutenberg.org/files/16/16-0.txt'
#
# fh = urllib.request.urlopen(url)
# text = fh.read().decode("UTF-8")
#

# Open file
with open('/Users/kjergens/Desktop/harrypotter.txt', 'r') as file:
    text = file.read()

# wordcloud = WordCloud().generate(text)
# plt.imshow(wordcloud)
# plt.axis('off')
# plt.show()

# # Make lowercase
tlist = []
text = text.lower()
#
# # Remove punctuation
# text = text.replace(',','')
# text = text.replace(':','')
# text = text.replace('.','')
# text = text.replace('?','')
# text = text.replace(')','')
# text = text.replace('(','')
# text = text.replace('"','')
# text = text.replace('!','')
# text = text.replace(';','')
# text = text.replace('-',' ')
# text = text.replace("'s",' ')
# text = text.replace("'t",' ')
#
# # Turn into a list
# tlist = text.split()

#tz =
#tlist = nltk.TreebankWordTokenizer().tokenize(text)
#tlist = nltk.WordPunctTokenizer().tokenize(text)
tlist = nltk.word_tokenize(text)



# Dictionary (key, value pairs where the key is the word and the value is the count)
# all_words = nltk.FreqDist(tlist)
#
# words = list(all_words.keys())
# counts = list(all_words.values())
#
# print(words[:90])
# print(counts[:90])

# Print how many words
print(len(tlist))
#print(parts_of_speech[:90])
# How many times Harry appears
print("Harry appears:", tlist.count('harry'))
print("Hermione appears:", tlist.count('hermione'))
print("Ron appears:", tlist.count('ron'))

ulist = list(set(tlist))
# Print how many unique words
print("Unique word count:", len(ulist))

# Get parts of speech
# parts_of_speech = nltk.pos_tag(ulist)
# nouns = [w[0] for w in parts_of_speech if w[1].startswith('NN')]
# adjs = [w[0] for w in parts_of_speech if w[1].startswith('JJ')]
# verbs = [w[0] for w in parts_of_speech if w[1].startswith('VB')]
#
# print('There are', len(nouns), 'nouns.')
# print(nouns[:20])
# print('There are', len(adjs), 'adjectives.')
# print(adjs[:20])
# print('There are', len(verbs), 'verbs.')
# print(verbs[:20])

ulist.sort()
adverbs = [word for word in ulist if word.endswith('ly')]
hyphenated = [word for word in ulist if '-' in word]
s_words = [word for word in ulist if word.startswith('s')]
gerunds = [word for word in ulist if word.endswith('ing')]
cap_names = [word.capitalize() for word in ulist if word in ('harry', 'ron', 'hermione', 'hagrid', 'uncle vernon', 'aunt petunia', 'dudley')]
# once_used_words = [word for word in tlist if tlist.count(word) == 1]

gerunds = []
for word in ulist:
    if word.endswith('ing'):
        gerunds.append(word)

print(adverbs)
print(hyphenated)
print(s_words)
print(gerunds)
print(cap_names)
print(random.choice(gerunds), random.choice(adverbs))

rword = random.choice(adverbs)
print("Random word:", rword, 'appears', tlist.count(rword), "time(s).")

# sort the list alphabetically
#unique_list.sort()

# start = time.clock()
# print("starting word counts....")
#
# fh = open('/Users/kjergens/Desktop/harrypotter_wordcount.txt', 'w')
#
# unique_list.sort()
#
# for word in unique_list:
#     print(word, ':', tlist.count(word), file=fh)
#     #fh.write(word + ':' + str(tlist.count(word)) + '\n')
#
# fh.close()
#
# stop = time.clock() - start
#
# print(stop, ' seconds')


# plt.bar(['gerunds', 'hyphenated', 'adverbs'], [len(gerunds), len(hyphenated), len(adverbs)])
# plt.show()
#
#
# plt.scatter(['total words', 'unique words'], [len(tlist), len(ulist)])
# plt.show()
#
#
# plt.plot(['Total words', 'Unique words'], [len(tlist), len(ulist)])
# plt.show()



slices = [len(gerunds),len(adverbs),len(hyphenated)]
activities = ['gerunds','adverbs','hyphenated']
cols = ['c','m','r']

plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0,0.1,0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')
plt.show()