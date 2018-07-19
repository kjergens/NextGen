import random

class Dice():
    num_sides = 6
    current_side_up = 1
    range_of_values = (1,2,3,4,5,6)

    def roll(self):
        self.current_side_up = random.choice(self.range_of_values)

    def __str__(self):
        return str(self.current_side_up)
