# Assignment 4.1: Programming Functions
# David Lattimer
# 4/5/2020
# DSC 510 Introduction to Programming

# This program will have:
# A welcome message
# function with two parameters
# A call to the function
# The application should calculate the cost based upon the number of feet being ordered
# A printed message displaying the company name and the total calculated cost

print("Welcome to Tim Tropic's Fiber Optics!") #Welcome message
print('What company are you buying fiber optic installation for?') #Ask for company name
companyName=input()
print('Welcome ' + companyName + " to Tim Tropic's Fiber Optics!")

#Create our cost function
def cost_function(a,b):
    calculation=a*b
    return '$''{0:.2f}'.format(calculation)

print('How many feet of fiber optic cable do you need installed?')
feet=int(input())

if feet<=100:
    price=0.87 #Price for less than 100 feet
elif feet>100 and feet<=250:
    price=0.80  #Price for between 100 and 250
elif feet>250 and feet<=500:
    price=0.70  #Price for between 250 and 500
elif feet>500:
    price=0.50  #Price for over 500 feet

print(str(int(feet)) + ' feet of fiber optic installation will cost: ' + cost_function(price,feet)) #Statement of price for order

#Create reciept
print("Thanks for shopping at Tim Tropic's Fiber Optics!")
print('Your company name: ' + companyName)
print('Amount of fiber optic cable ordered: ' + str(int(feet)) + ' feet')
print('Your total cost is: ' + cost_function(price,feet))
