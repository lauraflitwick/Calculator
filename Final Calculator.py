# This program is a simple calculator that focuses on Defensive Programming
# It validates user's input using techniques like:
# while loop, try-except-finally and if statements
user_file_name = input("Please, enter the name of the file you'd like to create: ")
# Here the program creates the file using the name chosen by the user and writes the first line there
# The reason for this is to open the file in case no calculations are made.
with open(user_file_name, "w") as file:
    file.write("Equations\n")

# The program first asks the user to choose one option:
# It defines display_or_calculation variable
display_or_calculation = input(
    "To display your equations, please, type 'd' and to make a calculation, please, type 'c': ")

# When the user chooses 'c', the while loop performs what's inside once, then it asks the question again
# Keep asking for input until "c" or "d" is entered - that's what the line below does
while display_or_calculation != "c" and display_or_calculation != "d":
    display_or_calculation = input(
        "To display your equations, please, type 'd' and to make a calculation, please, type 'c' : ")

# The loop below is executed if "c" is entered
while display_or_calculation == "c":
    # While True checks if the input is an integer and if it is, it breaks
    while True:
        try:
            number1 = int(input("Please enter the first number: "))
            break
        # Except below is executed if input is not an integer
        except ValueError:
            print("Invalid input - you did not enter a number.")
            print()

    while True:
        try:
            number2 = int(input("Please enter the second number: "))
            break

        except ValueError:
            print("Invalid input - you did not enter a number.")
            print()
    # Statement below asks for input (we need an operation to perform on numbers)
    operation = input("Please, enter one of the following:\n+ to add\n- to subtract\n"
                      "x to multiply\n/ to divide\n% for modulus\n")
    # The statement below checks if one of the 5 oparations was entered
    while operation != "+" and operation != "-" and operation != "x" and operation != "/" and operation != "%":
        # while operation not in [ `+`. ..]:
        # If none of the above was entered, the below is executed to prompt the user again
        print("You did not enter any of the operations above.")
        operation = input(
            "Please, enter one of the following:\n+ to add \n- to subtract\n ) to multiply\n/ to divide\n% for modulus\n")
    # Once of the if statements below is executed depending on the operation chosen by the user
    if operation == "+":
        addition = (f"{number1}{operation}{number2}={number1 + number2}\n")
        # The result is printed:
        print(addition)
        # The equation is saved:
        with open(user_file_name, "a") as file:
            file.write(addition)
    elif operation == "-":
        subtraction = (f"{number1}{operation}{number2}={number1 - number2}\n")
        print(subtraction)
        with open(user_file_name, "a") as file:
            file.write(subtraction)
    elif operation == "x":
        multiplication = (f"{number1}{operation}{number2}={number1 * number2}\n")
        print(multiplication)
        with open(user_file_name, "a") as file:
            file.write(multiplication)
    elif operation == "/":
        division = (f"{number1}{operation}{number2}={number1 / number2}\n")
        print(division)
        with open(user_file_name, "a") as file:
            file.write(division)
    elif operation == "%":
        modulus = (f"{number1}{operation}{number2}={number1 % number2}\n")
        print(modulus)
        with open(user_file_name, "a") as file:
            file.write(modulus)
    else:
        print("Invalid input")
    # Now the user is asked if they want to keep making calculations or if they want to see the results:
    display_or_calculation = input(
        "To display your equations, please, type 'd' and to make a calculation, please, type 'c': ")
    # Keep asking for input until "c" or "d" is entered - that's what the below does
    while display_or_calculation != "c" and display_or_calculation != "d":
        display_or_calculation = input(
            "To display your equations, please, type 'd' and to make a calculation, please, type 'c' : ")

# If 'd' is selected, the actions below are performed and the program stops/finishes
if display_or_calculation == "d":
    file = None

    while True:
        try:
            file_name = input("Please, enter the name of the file you'd like to open: ")
            file = open(file_name, "r")
            read_file = file.read()
            print(read_file)
            file.close()
            break
            # remove these lines:
            # file = open(file_name, "r")
            #             read_file = file.read()
            # with open(user_file_name, "w") as file:
            #     file.write("Equations\n")

        except FileNotFoundError:
            print("The file you are trying to open does not exist.")

        finally:
            if file is not None:
                file.close()
