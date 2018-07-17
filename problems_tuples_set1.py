import random

# 2
# names = ('Kathy', 'Benji', 'Ian', 'Alejandro')
#
# for n in names:
#     print(n, ':', len(n), 'letters')


# 3 Random names
first_names = ('Frances', 'Perry', 'Kerry', 'Omar', 'Carmen', 'Sonia',
              'Eloise', 'Trevor', 'Ricardo', 'Tyler')

last_names = ('Doyle', 'Floyd', 'Reid', 'Webb', 'Collier', 'Ward',
             'Cannon', 'Blake', 'Ball', 'Munoz')

num_names = int(input('How many names?'))

# For loop version
for n in range(num_names):
    print(random.choice(first_names), random.choice(last_names))


# While loop version
total = 0
while total < num_names:
    print(random.choice(first_names), random.choice(last_names))
    total += 1
