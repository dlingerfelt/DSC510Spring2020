
'''
File : DSC510Wk5.py
Name: Caleb Corpuz
Date: 04/12/2020
Course: DSC510-T303 Introduction to Programming (2203-1)
Description: The program will do the following:
Part 1:
Ask the user what operation they would like to perform, if the input is not valid then it repeats prompt till a valid answer is received
Ask the user for two numbers and performs the operation on those two numbers
Part 2:
Ask the user how many numbers they wish to input
Prompts the user to enter the numbers
Finds the sum and average of the numbers

The program then asks the user if they want to enter another set of numbers. If yes then the program repeats
'''

#Function that takes a math operation as the argument. Obtains 2 numbers from user input and performs the operation on the two numbers
def performCalculation(x):
    first_number = float(input('Enter the first number:'))
    second_number = float(input('Enter the second number:'))
    if x == "/":
        return first_number / second_number
    elif x == "*":
        return first_number * second_number
    elif x == "+":
        return first_number + second_number
    elif x == "-":
        return first_number - second_number
    else:
        print("Enter a valid operator")

#Function that has no arguments. The function asks the user how many numbers they wish to input and finds the sum and average of those numbers
def calculateAverage():
    num = int(input('How many numbers do you wish to input?'))
    for i in range(0, num):
        number = int(input('Enter a number: '))
        user_list.append(number)

#initialize user_response to YES
user_response = "YES"

#while user response is yes, perform functions performCalculation() and calculateAverage()
while user_response == "YES":
    user_list = []
    operator = ""

    while operator not in ("+", "-", "*", "/"):
        operator = input("Enter the operation you would like to perform (+, -, *, /): ")

    result = performCalculation(operator)

    print("Result:", result)

    calculateAverage()

    print('Total:', sum(user_list),
          "\n" 'Average:', sum(user_list)/len(user_list))

    user_response = input("Would you like to enter another set of answers? Please enter Yes or No: ").upper()
