import random

board = []
show_nums = []
items = ['cat', 'bowl', 'stick', 'flower', 'cup', 'baseball']
items *= 2

while items:
    board.append(items.pop(random.randint(0, len(items)-1)))

# Print board nicely
for i in range(len(board)):
    if (i + 1) % 3 == 0:
        end = '\n'
    else:
        end = ' |'

    print('{:>10}'.format(i), end=end)


while len(show_nums) < len(board):

    guess_a, guess_b = map(int, input('\nGuess 2 spots: ').split())

    if board[guess_a] == board[guess_b]:
        print('You found a match!')
        show_nums.extend([guess_a, guess_b])

    # Print board nicely
    for i in range(len(board)):
        if (i+1) % 3 == 0:
            end = '\n'
        else:
            end = ' |'

        if i in show_nums or i in (guess_a, guess_b):
            print('{:>10}'.format(board[i]), end=end)
        else:
            print('{:>10}'.format(i), end=end)


print("You won!")