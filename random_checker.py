import random

# lastnum = -1
# thisnum = random.randint(1, 10)
# print(thisnum)

# while(thisnum != lastnum):
#     lastnum = thisnum
#     thisnum = random.randint(1, 10)
#     print(thisnum)

# for name in ('Jennifer', 'April', 'Neil', 'Stu'):
#     print('Hi', name)


# count = 0
# for num in range(1, 200):
#     if num%7 == 0:
#         count += 1
#
# print(count)

# for x in 12, 14, 77, 34, 100, 0, 3:
#     print(x)

# for b in range(9):
#     for c in range(9):
#         print('*', end=' ')
#     print()

for i in range(7):
    for j in range(i):
        print('*', end='')
    print()

for i in range(7,0,-1):
    for j in range(i):
        print('*', end='')
    print()