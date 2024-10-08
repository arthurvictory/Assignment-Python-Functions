# Objective: The aim of this assignment is to build a basic calculator that can perform 
# addition, subtraction, multiplication, and division.

# Task 1: Create functions for each arithmetic operation.

# Task 2: Use inputs to ask the user what operation they want to perform, and what numbers 
# they want to use.

# Task 3: Ensure your code can handle division by zero and other potential errors. So 
# if you divide by 0, there is error handling set up to prevent an error from showing 
# in the console.

# addition function
def addition(num1, num2):
    return num1 + num2    

# Subtraction function
def subtraction(num1, num2):
    return num1 - num2

# multiplication function    
def multiplication(num1, num2):
    return num1 * num2    

# division function
def division(num1, num2):
    if num2 == 0:
        return ("You can't divide by zero! Try again.")
    return num1 / num2

# While loop to choose the proper operation and numbers. Also a quit function to stop program.
while True:
    print("""
          Which operation do you wanna perform?
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Division
          5. Quit
          """)
    response = input("Please make your selection: ")

    if response in ['1', '2', '3', '4']:
        num1 = int(input("Please enter your first number: "))
        num2 = int(input("Please enter your second number: "))

        if response == "1":
            print(f"Your numbers added is: {addition(num1, num2)}")
        elif response == "2":
            print(f"Your numbers subtracted is: {subtraction(num1, num2)}")
        elif response == "3":
            print(f"Your numbers multiplied is: {multiplication(num1, num2)}")
        elif response == "4":
            print(f"Your numbers divided is: {division(num1, num2)}")
    elif response == "5":
        break    
    else:
        "Please make a valid choice."