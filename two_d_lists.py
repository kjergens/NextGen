import random
# # list comprehensions
# # convert a list of strings to ints
# nums = ['5', '3', '0', '12']
# ns = [int(n) for n in nums]
# print(ns)
#
# # create a list of even numbers 0 - 200
# evens = [n for n in range(201) if n%2==0]
# print(evens)
#
# # map
# nms = list(map(int, nums))
# print(nms)
#
# #2D lists
#
# class_list = [
#     ['Donna', 'NYU', 20],
#     ['Valentina', 'Binghamton', 20],
#     ['Will', 'HS', 15]
# ]
#
# firstrow = class_list[0]
# print(firstrow[0])
#
# print(class_list[0][0])
# print the second row, third column (expected 20)
# add a row to the end with 'Bill', 'CUNY', 21
# print all the rows, one one each line
# print all the rows, and in the columns print each value

# students = ['donna', 'eric', 'stuey', 'blake']
#
# weights = [
#     ['dog', 30],
#     ['mug', 2],
#     ['book', 4]
# ]
#
# for s in students:
#     s = s.capitalize()    # You are just re-assigning your looping variable
#
# print(students)
#
# for i in range(len(students)):
#     students[i] = students[i].capitalize()   # You are changing the actual spot in memory
#
# print(students)

# targets = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
#
# #rand_spot = random.randint(0,len(targets))
# # Hold the coordinates of the
# prize_spots = [random.randint(0, 10), random.randint(0,10)]
#
# # make sure the second spot is different from the first one
# while prize_spots[0] == prize_spots[1]:
#     prize_spots = [random.randint(0, 10), random.randint(0, 10)]
#
# print(prize_spots)
# guess = -1
#
# while len(prize_spots) > 0:
#     for t in targets:
#         print(t, '\t', end='')
#
#     guess = int(input('\nGuess the spot I hid a prize:'))
#
#     # Update board
#     if guess in prize_spots:
#         prize_spots.remove(guess)
#         print('You got one!')
#         targets[guess] = '!!@!!'
#     else:
#         print('Nope!')
#         targets[guess] = 'x'
#
#
# if len(prize_spots) == 0:
#     print("You found all the prizes")
# else:
#     print("You didn't find all the prizes.")
#
# for t in targets:
#     print(t, '\t', end='')
#
# print()

lightbright = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
]


for x in range(5):
    lightbright.append(['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'])

for row in lightbright:
    for col in row:
        print(col, end=' ')
    print()

print('\nThere are 4 ships.')

# Hold the coordinates of the ships
secret_ships = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(4)]
print(secret_ships)
while len(secret_ships) > 0:
    coords = input("Enter row and column:")
    (y, x) = map(int, coords.split())

    # bounds checking y
    if y >= len(lightbright):
        y = len(lightbright) - 1
    elif y < 0:
        y = 0

    # bounds checking x
    if x >= len(lightbright[0]):
        x = len(lightbright[0]) - 1
    elif x < 0:
        x = 0

    # check if they found a ship
    if (y, x) in secret_ships:
        print('You found a ship!')
        lightbright[y][x] = 'O'
        secret_ships.remove((y, x))
    else:
        print('Nope!')
        lightbright[y][x] = 'x'

    # print board
    for row in lightbright:
        for col in row:
            print(col, end=' ')
        print()
