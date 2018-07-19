import re
import sys

try:
    f = open('z/Users/kjergens/Desktop/harrypotter.txt', 'r')
    text = f.read()  # read in the file to a string
    f.close()
except:
    text = ""
    print('File not found. The exact error is', sys.exc_info()[0])

harry_quotes = re.findall('".." .. Harry', text)  # find all times Harry speaks

# print nicely
for quote in harry_quotes:
    print(quote)

print(len(harry_quotes))
