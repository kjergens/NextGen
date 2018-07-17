from time import sleep


# #Print literals
# print (9)
# print(6)
# print("Hello World!")


# # Resolve math first
# print(9 + 6)
#
# # Combining strings and numbers
# print("hi", "there", 9)
# print("9 + 6 =", 9 + 6)
# print("The answer is", 9 + 6, ".")
#
# # Optional arguments
# print("The answer is ", 9 + 6, ".", sep="")
#
# print("Done.")
#
# print("The answer is ", 9 + 3, ".", sep="", end=" ")
# print("Done")
#
# print("The answer is", 9 + 1, ".", end="\n\n")
# print("done")
#
# # Print to file (overwrite)
# f = open('hello.txt', 'w')
# print("Hello World", file=f)
# f.close()
#
# # Print to file (append)
# f = open('hello.txt', 'w')
# print("Hello World", file=f)
# f.close()

# Flush
print("Sleeping...", end=" ")

sleep(.5)

print("Done")

# Flush=False means waits 5 seconds first then prints Sleeping...Done together
# Flush=True means prints Sleeping, waits 5 seconds, then prints Done.

# print("9 + 6 = %d." % (9 + 6))
# print("9.5 + 6.99 = %.2f." % (9.5 + 6.99))

# Other than printing, what else can we do?
# https://docs.python.org/3.3/library/functions.html
"""
len()
abs()
round()
min()
max()

"""
# print(len("hello"))
# print(round(4.5))
# print(max((9, 3, 6)))
# print(min((9, 3, 6)))
# print(abs(-4))
#
# l = [5, 6, 7]

# play_again = "yes"
# while play_again == "yes":
#     print("I will add two random numbers and tell you the answer.")
#     rand_a = random.randint(0, 100)
#     rand_b = random.randint(0, 100)
#     print(rand_a, "+", rand_b, "=", rand_a + rand_b)
#     play_again = input("Play again? (yes/no) ")
# print("Good bye")

# age = 21
#
# name = "Katie"
#
# name: str = 'Katie'
#
# print(name)
# print()
#
# print("age.bit_length = ", age.bit_length())
#
#
# print(locals())
#
# def get_decade(exact_age):
#     decade = (exact_age // 10) + 1
#     print("Local variables: ", locals())
#     print("Global variables: ", globals())
#     return decade
#
#
# print("You are in decade #", get_decade(age), " of life.", sep="")
