operand_one = int(input("Enter operand: "))
operator = input("Enter + or - or * or / or weird ")
operand_two = int(input("Enter operand: "))

if operator == "+":
    print(operand_one + operand_two)
elif operator == "-":
    print(operand_one - operand_two)
elif operator == "*":
    print(operand_one * operand_two)
elif operator == "/":
    print(operand_one / operand_two)
elif operator == "weird":
    print(operand_one ** operand_two ** operand_one)
else:
    print("Can't recognize operator")
