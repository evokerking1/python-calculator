import os

def exit():
    _exit = os.system("exit")

print("Hello! Welcome to evokerking's calculator program!"
      "\nThis program is a simple calculator that can perform Addition, Subtraction, Multiplication and Division.")
print("Please enter the numbers you want to perform operations on.")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Please enter the operation you want to perform.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")
operation = int(input("Enter the operation number: "))
if operation == 1:
    print("The result of addition is: ", num1 + num2)
elif operation == 2:
    print("The result of subtraction is: ", num1 - num2)
elif operation == 3:
    print("1. Multiplication")
    print("2. exponents")
    print("3. Exit")
    suboperation = int(input("Enter the sub-operation number: "))
    if suboperation == 1:
        print("The result of multiplication is: ", num1 * num2)
    elif suboperation == 2:
        print("The result of division is: ", num1 ** num2)
    elif suboperation == 3:
        exit()
    else:
        print("Invalid sub-operation number. Please enter a valid sub-operation number.")
elif operation == 4:
    suboperation = int(input("Enter the sub-operation number: "))
    print("1. Division w/ remainders")
    print("2. Just remainders")
    print("3. Division without remainders")
    print("4. Exit")
    if suboperation == 1:
        print("The result of multiplication is: ", num1 / num2)
    elif suboperation == 2:
        print("The result of division is: ", num1 % num2)
    elif suboperation == 3:
        print("The result of division is: ", num1 // num2)
    elif suboperation == 4:
        exit()
    else:
        print("Invalid sub-operation number. Please enter a valid sub-operation number.")
elif operation == 5:
    exit()
else:
    print("Invalid operation number. Please enter a valid operation number.")
print("Thank you for using my calculator program!")

print("Please join my discord server: https://discord.gg/ for updates on all my projects, for a list of my projects, go to https://evokerking.dev/")
