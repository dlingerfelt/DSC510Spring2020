# File: BUNCH_3_1.py
# Name: Jonathan Bunch
# Date: 29 March, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Display a welcome message for your program.
# Get the company name from the user.
# Get the number of feet of fiber optic cable to be installed from the user.
# Evaluate the total cost based upon the number of feet requested.
# Display the calculated information including the number of feet requested and company name.

# Print a welcome message for the user.
print('Welcome to our digital quoting system!')

# Prompt the user to enter a company name, and assign the name to a new variable.
company_name = input('Please enter your company name:')

# Prompt the user to enter feet of cable requested, and assign that value to another variable.
feet_cable = input('How many feet of fiber optic cable will you be installing?:')

# Python will return the input value as an "int" type, so we must convert it to a "float" type for compatibility with
# the "price_per_foot" variable.  Note: the program will crash here if the user enters any non-numbers.
feet_cable = float(feet_cable)

# The price per foot changes depending on the number of feet requested.  This statement compares the user provided
# value to the price break points, and changes the "price_per_foot" variable accordingly.
if feet_cable > 500:
    price_per_foot = 0.50
elif feet_cable > 250:
    price_per_foot = 0.70
elif feet_cable > 100:
    price_per_foot = 0.80
else:
    price_per_foot = 0.87

# Multiply the number of feet by the price per foot to calculate the total cost, and assign that value to a variable.
total_cost = feet_cable * price_per_foot

# Print a receipt for the user based on the values of our variables, and format output to standard monetary format.
print('')
print('Thank you for using our digital quoting system.  Please see your quote below.')
print('Company:', company_name)
print(f'Feet of cable requested: {round(feet_cable, 2):.2f}')
print(f'Price per foot: ${price_per_foot:.2f}')
print(f'Total Cost: ${round(total_cost, 2):.2f}')
print('Thank you for considering us for your cable installation needs!')

