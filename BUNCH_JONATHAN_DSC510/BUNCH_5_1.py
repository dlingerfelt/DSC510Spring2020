# File: BUNCH_5_1.py
# Name: Jonathan Bunch
# Date: 12 April, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# This program will perform various calculations (addition, subtraction, multiplication, division, and average
# calculation) This program will contain a variety of loops and functions. The program will add, subtract, multiply,
# divide two numbers and provide the average of multiple numbers input by the user. Define a function named
# performCalculation which takes one parameter. The parameter will be the operation being performed (+, -, *, /).
# This function will perform the given prompt the user for two numbers then perform the expected operation
# depending on the parameter that's passed into the function. This function will print the calculated value for the
# end user. Define a function named calculateAverage which takes no parameters. This function will ask the user how
# many numbers they wish to input. This function will use the number of times to run the program within a for loop in
# order to calculate the total and average. This function will print the calculated average. This program will have a
# main section which contains a while loop. The while loop will be used to allow the user to run the program until
# they enter a value which ends the loop. The main program should prompt the user for the operation they wish to
# perform. The main program should evaluate the entered data using if statements. The main program should call the
# necessary function to perform the calculation.


# This function prompts the user for the numbers to be operated upon, using the argument to determine the operator.
# The appropriate calculation is performed and the result is printed.
def perform_calculation(operation):
    num1 = float(input('Enter first number:'))
    num2 = float(input('Enter second number:'))
    calc_value = 0
    if operation == 0:
        calc_value = num1 + num2
    elif operation == 1:
        calc_value = num1 - num2
    elif operation == 2:
        calc_value = num1 * num2
    elif operation == 3:
        calc_value = num1 / num2
    print('Calculated value:', calc_value)


# This function prompts the user for how many numbers they wish to enter, then prompts them to enter each number.
# When all numbers are entered the sum and average are calculated and printed for the user.
def calculate_average():
    nums = int(input('How many numbers would you like to enter?'))
    total_val = 0
    total_val = float(total_val)
    for n in range(nums):
        total_val = total_val + float(input('Enter number ' + str(n + 1) + ':'))
    average = total_val / nums
    print('Sum of values entered:', total_val)
    print('Average of values entered:', average)


# Print a welcome message for the user.
print('Welcome! Would you like to try our calculator program today? Our calculator offers two functions: '
      'two number calculations and multiple number averages.')

# This variable will be used to exit the loop if the user wishes to quit the program.
use_calc = 1

# Our while loop will allow the user to perform as many calculations as they wish.  Each iteration presents them with
# the option of using one of the two functions or exiting the program.
while use_calc != 0:
    mode = int(input('Please enter 1 to perform a two number calculation, enter 2 to perform a '
                     'multiple number average, or enter 0 (zero) to exit the program:'))
    if mode == 0:
        use_calc = 0
        print('Thank you for using our calculator program!')
        break
    if mode == 1:
        print('Our calculator supports the following operations: +, -, *, /.')
        operator = input('Please enter your desired operation:')
        print('Selected operation:', operator)
        if operator == '+':
            perform_calculation(0)
        elif operator == '-':
            perform_calculation(1)
        elif operator == '*':
            perform_calculation(2)
        elif operator == '/':
            perform_calculation(3)
        else:
            print('Please try again. Remember only the following operators are accepted: +, -, *, /.')
        continue
    if mode == 2:
        print('Our program will calculate the total value and average value for as many numbers as you wish to enter.')
        calculate_average()
        continue
    else:
        print('Please try again. Remember only numbers corresponding to available options are accepted.')
        continue
