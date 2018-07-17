stocks = []

with open('/Users/kjergens/Desktop/apple_stocks.txt') as f:
    for line in f:
        stocks.append(line.split())

# delete the first line
#del stocks[0]

# convert to a float
for y in range(1, len(stocks)):
    for x in range(len(stocks[y])):
        if '-' not in stocks[y][x]:
            stocks[y][x] = float(stocks[y][x])

for y in stocks:
    print(y)