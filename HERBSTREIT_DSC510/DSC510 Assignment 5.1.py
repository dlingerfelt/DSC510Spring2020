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
        # If user says yes begin calculator
        if basicQ == 'Yes' or basicQ == 'yes':
            # Ask user for information to perform calculation
            while True:
                num1 = float(input('Please enter first number \n'))
                try num1 == float() or num1 == int():
                    continue
                except:
                    print('Please enter a number')
                    break
            num2 = float(input('Please enter second number \n'))
            if num2 == float():
                continue
            else:
                print('Please enter a number')
            # Perform calculation
            print('The answer is:', performCalculation(num1, num2))
            # Inquire about more calculations
            basicQ2 = input('Would you like to perform another basic math calculation?\n')
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
            numT = int(input('How many numbers would you like to average?\n'))
            sum = 0
            for i in range(numT):
                x = float(input('Enter a number: '))
                sum = sum + x
            avg = sum / numT
            # Display answer for user
            print('The average of these numbers is:', avg)
            # Ask if they would like to repeat average calculation
            Ask2 = input(('Would you like to calculate another average?\n'))
            # If user says yes loop repeats
            if Ask2 == 'Yes' or Ask2 == 'yes':
                continue
            # If user says no loop exits
            elif Ask2 == 'No' or Ask2 == 'no':
                print('Thank you for stopping by!')
                break
            # Ask user for valid input
            else:
                print('Please enter yes or no')
        # If user says no loop exits
        elif Ask == 'No' or Ask == 'no':
            print('Thank you for stopping by!')
            break
        # Ask user for valid input
        else:
            print('Please enter yes or no')


# Call on functions
inquiry()
calculateAverage()
