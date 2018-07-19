import dice

print('Let\'s roll the dice!')

dice_a = dice.Dice()
print(dice_a.current_side_up)

dice_a.roll()

print(dice_a)