# Bin-max
# for n in range(0, 256):
#     highest_num = 0  # reset highest number
#
#     # computes highest num for n-places
#     for p in range(0, n):
#         highest_num += (2 ** p)  # add up binary value
#
#     print(n, 'bits lets you go up to', highest_num)

total = 0
for x in range(256):
    total += 2 ** x
    print(x, total)
