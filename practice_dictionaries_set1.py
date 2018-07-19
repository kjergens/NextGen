# Set 1
# 1

# residents = {'Puffin': 104, 'Sloth': 105, 'Burmese Python': 106}
# print(residents['Sloth'])

# 2
# menu = {}
# menu['Sunday'] = 16.78
# print(menu['Sunday'])
#
# menu['Monday'] = 3
# menu['Tuesday'] = 0
#
# # BONUS: print each value on its own line
# for key in menu:
#     print(key, ":", menu[key])


# 3
# key - animal_name : value - location
# zoo_animals = { 'Unicorn' : 'Cotton Candy House',
# 'Sloth' : 'Rainforest Exhibit',
# 'Bengal Tiger' : 'Jungle House',
# 'Atlantic Puffin' : 'Arctic Exhibit',
# 'Rockhopper Penguin' : 'Arctic Exhibit'}
#
# del zoo_animals['Sloth']  # kill the sloth
# del zoo_animals['Bengal Tiger']  # kill the tiger
#
# zoo_animals['Rockhopper Penguin'] = 'Children Zoo Area'
#
# for k in zoo_animals:
#     print(k, ":", zoo_animals[k])

# 4
# webster = {
#       "Aardvark" : "A star of a popular children's cartoon show.",
#       "Baa" : "The sound a goat makes.",
#       "Carpet": "Goes on the floor.",
#       "Dab": "A small amount."
# }
#
# for k in webster:
#     print(k, ":", webster[k])

#5
my_dict={'title':'Stranger Things', 'is_show':True, 'seasons':2}

print(my_dict.items())

for k, v in my_dict.items():
    print(k, ":", v)
