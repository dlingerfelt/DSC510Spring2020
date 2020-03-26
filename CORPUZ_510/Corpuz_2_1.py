'''
File : DSCWK2.py
Name: Caleb Corpuz
Date: 03/18/2020
Course: DSC510-T303 Introduction to Programming (2203-1)
Description: The program will do the following:
Display a welcome message for your user.
Retrieve the company name from the user.
Retrieve the number of feet of fiber optic cable to be installed from the user.
Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost,
and total cost in a legible format.

'''


print('Hello! Welcome to the cost calculator.')
#Retrieve the company name
company = input('Please enter the company name:')
#Retrieve the length of the cable
cable_length = input('Please enter how many feet of fiber optic cable you desire: ')
#Calculate the cost
cost = float(cable_length)*0.87
#Print the receipt
print('Company:', company,
"\n" 'Length of fiber optic cable:', cable_length,
"\n"  'Cost per foot: $ 0.87',
"\n" 'Total Cost:$', cost)

