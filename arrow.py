#import hangman

arrow_width = 4  # int(input("Width of arrow:"))

for y in range(arrow_width):
    for x in range(y):
        print("*", end='')
    print()

for y in range(arrow_width, 0, -1):
    for x in range(y):
        print("*", end='')
    print()

students = []
students.append(['donna', 'nyu', 21])
students.append(['valentina', 'nyu', 20])
students.append(['jared', 'hs', 15])
students.append(['ryan', 'bing', 2])

# print(students[0])
# print(students[1])

# use a for loop to print each student row on its own line

# for i in range(len(students)):
#     print(students[i])


for y in range(arrow_width):
    for x in range(y+1):
        print(students[y][x])
