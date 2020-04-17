import datetime as dt
import math
def welcome():
    print('''
Welcome to Calculator
''')



#def calcuate():



print ("# "*20 + 'Please select the operation you want to perform' + " #"*20)
print ('Please enter 1 to perform Addition')
print ('Please enter 2 to perform Substraction')
print ("Please enter 3 to perform Multiplication")
print ("Please enter 4 to preform Division")

operation = input("Enter the Operation ID : ")

#Enter the 2 values to calculate the operation

def performCalculation():
    if operation == '1':
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
        Add=(number_1 + number_2)
        print (Add)
    elif operation == '2':
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
        Sub = (number_1-number_2)
        print (Sub)
    elif operation == '3':
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
        Mul = (number_1*number_2)
        print (Mul)
    elif operation == '4':
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
        Div = (number_1/number_2)
        print (Div)
    else: print('You have not typed a valid operator, please run the program again.')

#performCalculation()

'''Define a function named calculateAverage which takes no parameters.
This function will ask the user how many numbers they wish to input.
This function will use the number of times to run the program within a for loop in order to calculate the total and average.
This function will print the calculated average.
'''
def calculateAverage ():
    number_1 = int(input('Please enter a number: '))
    Total=0
    for val in range(0, number_1+1):
        Total = Total + val
    print(Total)
    Avg= Total/number_1
    print(Avg)

welcome()
performCalculation()
calculateAverage ()
