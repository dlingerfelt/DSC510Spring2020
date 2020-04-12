# File: Assignment_5.1
# Name: Hanh Tran
# Due Date: 4/12/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: This program will do the following:
# Define a function, performCalculation that takes one operator as a parameter.
# Prompt the user for two numbers then perform the expected operation.
# The operation depends on the parameter that's passed into the function.
# Function will print the calculated value for user.
# Define a function, calculateAverage which takes no parameters.
# Ask user how many number they wish to input.
# Use the number of times to run program within for loop in order to calculate total and average.
# Function will print the calculated average.

# defined function performCalculation that takes one parameter, the operator.
def performCalculation(operation):
    # prompt the user for two numbers.
    number_1 = int(input('Please provide a whole number for calculation:\n'))
    number_2 = int(input('Please provide another whole number for calculation:\n'))
    # evaluate the entered data using if statements and prints calculated value.
    if operation == '+':
        print('Your sum is: ', number_1 + number_2)
    elif operation == '-':
        print('Your difference is: ', number_1 - number_2)
    elif operation == '*':
        print('Your product is: ', number_1 * number_2)
    elif operation == '/':
        print('Your division comes to: ', number_1 / number_2)
# Define a function, calculateAverage which takes no parameters.
def calculateAverage():
    # function asks user for how many numbers to average.
    num = int(input('How many numbers do you wish to average?: '))
    total_sum = 0
    # function uses the for loop to calculate total and average.
    for n in range(num):
        numb = int(input('Please enter a number: '))
        total_sum += numb
    avg = total_sum / num
    # function prints the calculated average.
    print('The calculated average of these numbers is: ', avg)
# function has a main section containing a while loop that allows user to exit.
operator = ['+','-','*','/']
averg = ['avg']
def main_wloop():
    while True:
        # main program that prompts user for operation
        operation = input('Please choose an operation to perform: +, -, *, /, avg or exit to stop\n')
        if operation in operator:
            # calls the necessary function to perform calculation
            performCalculation(operation)
        if operation in averg:
            # calls the necessary function to perform calculation
            calculateAverage()
            # the sentinel value to end the loop is none.
        if operation == 'exit':
            break
    print ('You have exited')
main_wloop() # calls the main function to run main loop.
