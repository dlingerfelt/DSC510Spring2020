"""
File: assignment5_1.py
Author: Bhushan Suryawanshi
Date:Wednesday, April 07, 2020
Course: DSC510-T303 Introduction to Programming (2205-1)
Desc: The program will do followings:
This program will perform various calculations (addition, subtraction, multiplication, division, and
average calculation)
This program will contain a variety of loops and functions.
The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the
user.
Define a function named perform_calculation which takes one parameter. The parameter will be the operation being
performed (+, -, *, /).
    - This function will perform the given prompt the user for two numbers then perform the expected operation
      depending on the parameter that's passed into the function.
    - This function will print the calculated value for the end user.
Define a function named calculate_average which takes no parameters.
    - This function will ask the user how many numbers they wish to input.
    - This function will use the number of times to run the program within a for loop in order to calculate the total
      and average.
    - This function will print the calculated average.
This program will have a main section which contains a while loop. The while loop will be used to allow the user to run
the program until they enter a value which ends the loop.
The main program should prompt the user for the operation they wish to perform.
The main program should evaluate the entered data using if statements.
The main program should call the necessary function to perform the calculation.
"""


def print_dash():
    print('-' * 51)


def perform_calculation(operation):
    first_value = input("Please Enter first value:->")
    second_value = input("Please Enter first value:->")
    total = 0
    try:
        if operation == "+":
            total = float(first_value) + float(second_value)
        elif operation == "-":
            total = float(first_value) - float(second_value)
        elif operation == "*":
            total = float(first_value) * float(second_value)
        elif operation == "/":
            total = float(first_value) / float(second_value)
        else:
            print("Operation {} not supported.".format(operation))
    except ZeroDivisionError:
        print("**ERROR ==> Divide by zero not allowed.")
    except Exception:
        print("**ERROR ==> Check input parameters.")

    print_result(total)


def print_result(total):
    print_dash()
    print("Result={:0.2f}".format(total))
    print_dash()


def calculate_average():
    try:
        num_cnt = int(input("Enter how many numbers you want to input: "))
        input_num = []
        for i in range(num_cnt):
             input_num.append(float(input("Enter number {} : ".format(i + 1))))

        tot_sum = 0
        for i in input_num:
            tot_sum += i

        print_result(tot_sum / num_cnt)

    except Exception:
        print("**ERROR: Wrong input parameter")


def main():
    print(" Welcome to math calculation.")
    while True:
        print(" Please Enter one of following options. \n"
              " 1. If operation being performed  is (+, -, *, /). \n"
              " 2. If want average of numbers.\n"
              " 3. Exit.")
        option = input("Enter your option : ")
        if option == "1":
            operation = input("Enter Operation to be performed : ")
            if _is_valid_operation(operation):
                perform_calculation(operation)
            else:
                print("Wrong operation {}".format(operation))
        elif option == "2":
            calculate_average()
        elif option == "3":
            break
        else:
            print("Wrong Input.")


def _is_valid_operation(operation):
    valid = True
    if (operation != "+" and operation != "-"
            and operation != "/" and operation != "*"):
        valid = False

    return valid


if __name__ == '__main__':
    main()
