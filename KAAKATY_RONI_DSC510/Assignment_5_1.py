# File: Assignment_5_1.py
# Name: Roni Kaakaty
# Date: 04/11/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# This program will do the following:
# This program will perform various calculations (addition, subtraction, multiplication, division)
# This program will contain a variety of loops and functions.
# The program will add, subtract, multiply, divide two numbers and provide the average of multiple numbers input by the user.
# This program will define a function named performCalculation that has one parameter. The parameter will be the operation performed (+,-,*,/)
# This program will define another function named calculateAverage that has zero parameters.
# calculateAverage function will ask the user for how many numbers to input, use a for loop, and print average.


def performCalculation(x):  # Function that performs the various arithmetic operations based on user input.
    value1 = float(input('Enter your first value: \n'))  # Input converted to float
    value2 = float(input('Enter your second value: \n'))  # Input converted to float
    if x == '+':
        print ('The sum of the two numbers is', value1 + value2)
    elif x == '-':
        print ('The difference between the two numbers is', value1 - value2)
    elif x == '*':
        print ('The product is', value1 * value2)
    elif x == '/':
        print ('The quotient is', value1 / value2)


def calculateAverage():  # Function that will process the averages based on user input.
    user_num = int(input('How many numbers would you like to use? \n'))
    total = 0
    for i in range(user_num):
        user_avg_numbers = float(input('Enter the numbers you would like averaged together: '))  # Converts input to float.
        total = total + user_avg_numbers
    total_avg = total/user_num
    print ('The average is', total_avg)


Operands = ['+','-','*','/']  # Operand List
Avg = ['average','avg']  # Average List
Both = ['+','-','*','/','average','avg', 'none']  # List that returns an error if none selected.

def main():  # Main function to call the loop/other functions.
    print ('Welcome to our calculator')

    while True:  # Loop used to perform the operations based on user's input.
        user_operand = input ('What arithmetic operation would you like to perform? (+,-,*,/,average or none) \n')
        if user_operand in Operands:
            performCalculation(user_operand)  # Calling function to perform operations.
        if user_operand in Avg:
            calculateAverage()  # Calling function to find average of numbers provided.
        if user_operand not in Both:  # Created to catch misspellings and errors
            print('Please check entry and try again')
        if user_operand == 'none':  # Ends the loop.
            break
    print ('Thanks for using our calculator!')

main()









