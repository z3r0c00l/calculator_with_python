# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to substract two numbers


def substract(num1, num2):
    return num1 - num2

# Function to multiply two numbers


def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers


def divide(num1, num2):
    return num1 / num2


print("Please select operation.")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# Taking user inputs
while True:
    choice = (input("Enter choice -->> "))
# check if choice is one of the four options
    if choice in ("1", "2", "3", "4"):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input.Please enter a number.")
            continue

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", substract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

# Check if user wants another calculation
# break the while loop if answer is no
    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
        break
    else:
        print("Invalid Input")
