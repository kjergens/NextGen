import random

lightbright = ['.', '.', '.', '.', '.', '.', '.', '.', '.','.']  # one row

board = [] # full board (it starts empty)

# add 10 lightbright rows
for x in range(10):
    board.append(lightbright.copy())  # make a copy (don't just use same row over and over)

# print board nicely
for row in board:
    for dot in row:
        print(dot, end=' ')
    print()  # after each row, print a newline

# Create a secret spot (x, y) and they have to find it
secret_x, secret_y = random.randint(0, 9), random.randint(0, 9)

print((secret_y, secret_x))

turns = 10
while turns > 0:
    # Get row and col from user
    y, x = map(int, input('Enter a row and column. (Example: 1 2): ').strip().split())

    turns = turns - 1  # used up a turn

    # check if they found the secret spot
    if x == secret_x and y == secret_y:
        print('You found it!')
        board[y][x] = 'X'       # if they get it, mark it with an x
        turns = 0  # no more turns
    else:
        board[y][x] = 'O'  # if they got it wrong, update the board to have a 'O'

    # print board nicely
    for row in board:
        for dot in row:
            print(dot, end=' ')
        print()  # after each row, print a newline


