import quoter
from urllib import request
import matplotlib

url_peter_pan = 'https://www.gutenberg.org/files/16/16-0.txt'
url_pride = 'https://www.gutenberg.org/files/1342/1342-0.txt'
text = request.urlopen(url_pride).read().decode('UTF-8')

elizabeth_quotes = quoter.get_quotes_by('Elizabeth', text)
darcy_quotes = quoter.get_quotes_by('Darcy', text)

print('Elizabeth speaks', len(elizabeth_quotes), 'times.')
print('Darcy speaks', len(darcy_quotes), 'times.')

