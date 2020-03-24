# File: BUNCH_2_1.py
# Name: Jonathan Bunch
# Date: 22 March, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: The program will do the following:
# Display a welcome message for your user.
# Retrieve the company name from the user.
# Retrieve the number of feet of fiber optic cable to be installed from the user.
# Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost,
# and total cost in a legible format.
# Include appropriate comments throughout the program.

# Print a welcome message for the user.
print('Welcome to our digital quoting system!')

# Prompt the user to enter a company name, and assign the name to a new variable.
company_name = input('Please enter your company name:')

# Prompt the user to enter feet of cable requested, and assign that value to another variable.
feet_cable = input('How many feet of fiber optic cable will you be installing?:')
# Python will return the input value as an "int" type, so we must convert it to a "float" type for compatibility with
# the "price_per_foot" variable.  Note: the program will crash here if the user enters any non-numbers.
feet_cable = float(feet_cable)

# Declare a variable for the price per foot of cable.  We could simply use this value throughout the program, but
# assigning it to a variable makes changing the price later much simpler.
price_per_foot = 0.87

# Multiply the number of feet by the price per foot to calculate the total cost, and assign that value to a variable.
total_cost = feet_cable * price_per_foot

# Print a receipt for the user based on the values of our variables.
print('')
print('Thank you for using our digital quoting system.  Please see your quote below.')
print('Company:', company_name)
print('Feet of cable requested:', feet_cable)
print('Price per foot: $', price_per_foot)
print('Total Cost: $', total_cost)
print('Thank you for considering us for your cable installation needs!')