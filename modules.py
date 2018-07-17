from urllib import request

url = "http://www.py4inf.com/code/clown.txt"
web_page = request.urlopen(url)
print(web_page.read().decode("ASCII"))



