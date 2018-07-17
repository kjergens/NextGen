import chardet
import re
from urllib import request

url = "http://www.py4inf.com/code/clown.txt"
#url = 'https://www.gutenberg.org/files/1342/1342-0.txt'

web_page = request.urlopen(url).read()

print(chardet.detect(web_page))

print(type(web_page))

#web_page = web_page.decode(chardet.detect(web_page)['encoding'])

print(web_page[:800])

#print(re.findall(r'\bt\w*\b', web_page))

#print(chardet.detect(web_page))

# print(b'\xc2\xae'.decode())
# print(b'\xdf\x87'.decode())
# print('Ʊ'.encode().decode())
# ®
# registered sign
# Unicode: U+00AE, UTF-8: C2 AE

#grinning face
#Unicode: U+1F600, UTF-8: F0 9F 98 80)