# File: Assignment_5_1.py
# Sara Herbstreit
# 04/11/20
# DSC510-T303 Introduction to Programming (2203-1)

# Welcome message
print('Welcome to the Python Calculator App!\n')


# Define basic math prompt
def inquiry():

    # Begin loop
    while True:

        # Ask if they want basic math calculator
        basicQ = input('Would you like to perform addition, subtraction, multiplication or division? (yes/no)\n')

        # If user says yes then begin calculator
        if basicQ == 'Yes' or basicQ == 'yes':

            # Ask user for numbers
            try:
                num1 = float(input('Please enter first number \n'))
                num2 = float(input('Please enter second number \n'))

            # Reject non-numerical values and repeat loop
            except ValueError:
                print('Please try again with valid numbers only')
                continue

            # Perform calculation and give answer
            print('The answer is:', performCalculation(num1, num2))

            # Inquire about more calculations
            basicQ2 = input('Would you like to perform another calculation?\n')

            # if user says yes repeat loop
            if basicQ2 == 'Yes' or basicQ2 == 'yes':
                continue

            # if user says no exit loop
            elif basicQ2 == 'No' or basicQ2 == 'no':
                break

            #  Ask user for valid input
            else:
                print('Please enter yes or no')

        # if user says no exit loop
        elif basicQ == 'No' or basicQ == 'no':
            break

        # Ask user for valid input and repeat loop
        else:
            print('Please enter yes or no')


# Define calculator functions
def performCalculation(num1, num2):

    # Begin loop
    while True:

        # Ask user what type of math
        math = input('Input the number representing the calculation you want to perform.\n'
                     '1. Addition\n'
                     '2. Subtraction\n'
                     '3. Multiplication\n'
                     '4. Division\n')

        # Defining calculations
        if math == '1':
            return num1 + num2
        elif math == '2':
            return num1 - num2
        elif math == '3':
            return num1 * num2
        elif math == '4':
            return num1 / num2

        # Ask user for valid input and repeat loop
        else:
            print('Please enter a valid number selection')


# Define average function
def calculateAverage():

    # Begin loop
    while True:

        # Ask if user wants to perform average calculation
        Ask = input('Would you like to calculate an average for a set of numbers?\n')

        # Calculate if user says yes
        if Ask == 'Yes' or Ask == 'yes':

            # Begin valid average total loop
            while True:

                # Ask how many numbers to average
                try:
                    numT = int(input('How many numbers would you like to average?\n'))

                # Reject non-numerical value and repeat loop
                except ValueError:
                    print('Please enter a valid number')
                    continue

                # Begin average calculation
                try:
                    sum = 0
                    for i in range(numT):

                        # Ask user for numbers to average
                        x = float(input('Enter a number: '))

                        # Calculate average
                        sum = sum + x
                    avg = sum / numT

                    # Display answer to user
                    print('The average of these numbers is:', avg)

                # Reject non-numerical values
                except ValueError:
                            print('Please enter valid numbers only')
                            continue

                # Ask if they would like to repeat average calculation
                Ask2 = input('Would you like to calculate another average?\n')

                # If user says yes loop repeats
                if Ask2 == 'Yes' or Ask2 == 'yes':
                    continue

                # If user says no loop exits
                elif Ask2 == 'No' or Ask2 == 'no':
                    print('Thank you for stopping by!')
                    return

                # Ask user for valid input and repeat loop
                else:
                    print('Please enter yes or no')
                    continue

        # If user says no loop exits
        elif Ask == 'No' or Ask == 'no':
            print('Thank you for stopping by!')
            break

        # Ask user for valid input and repeat loop
        else:
            print('Please enter yes or no')
            continue


# Call on functions
inquiry()
calculateAverage()
