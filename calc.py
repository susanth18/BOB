# define function to perform addition
def add(num1, num2):
    return num1 + num2

# define function to perform subtraction
def subtract(num1, num2):
    return num1 - num2

# define function to perform multiplication
def multiply(num1, num2):
    return num1 * num2

# define function to perform division
def divide(num1, num2):
    return num1 / num2

# main program loop
while True:
    # display menu
    print("Please select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # get user input
    choice = int(input("Enter choice (1/2/3/4/5): "))

    # exit loop if choice is 5
    if choice == 5:
        break

    # get user input for numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # perform calculation based on user choice
    if choice == 1:
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == 2:
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == 3:
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == 4:
        if num2 == 0:
            print("Error: division by zero")
        else:
            print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid input")
