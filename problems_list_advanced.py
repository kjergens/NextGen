import random

# 1.1
# things = ['hat', 'cat', 'book']
#
# for i in range(len(things)):
#     things[i] += 's'
#
# print(things)

# 1.2
# nums = [x+1 for x in range(6)]
#
# for i in range(len(nums)):
#     nums[i] = nums[i] ** 2  # change the list
#
# print(nums)

# 1.3
# weights = [
#     ['dog', 30],
#     ['mug', 2],
#     ['book', 4]
# ]
#
# # print('A', weights[1][0], 'weighs', weights[1][1], 'pounds.')
# # print('A ' + weights[1][0] + ' weighs ' + str(weights[1][1]) + ' pounds.')
#
# weights.append(['truck', 5000])
#
# print(weights)
#
# for i in range(len(weights)):
#     print('A', weights[i][0], 'weighs', weights[i][1], 'pounds.')
#
#

# 2
# Create my game variables
targets = ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
player_guess = None # at the start make sure they didn't win
turns = 0
prize_spots = [random.randint(0, len(targets)), random.randint(0, len(targets))]

# Keep getting two different spots until they are not the same
while prize_spots[0] == prize_spots[1]:
    prize_spots = [random.randint(0, len(targets)), random.randint(0, len(targets))]

print(prize_spots)

# Play game
while len(prize_spots) > 0 and turns < 6:
    player_guess = int(input('\nGuess which spot I hid the prize: \n'))

    turns += 1  # count the turn

    if player_guess not in prize_spots:
        print('Wrong!')
        targets[player_guess] = 'x'
    else:
        print('Correct!')
        targets[player_guess] = '!!@!!'
        prize_spots.remove(player_guess)

    # print the board nicely
    for t in targets:
        print(t, end=' ')

# End of game message
if turns == 6:
    print('\nYou lost')
else:
    print('\nYou win!!!!')