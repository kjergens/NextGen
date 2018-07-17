prize_spots = [(1, 2), (3, 3)]

while len(prize_spots) > 0:
    user_tuple = tuple(map(int, input('Guess').split()))

    print(user_tuple)

    if user_tuple in prize_spots:
        print("you found one")
        prize_spots.remove(user_tuple)
        print(prize_spots)