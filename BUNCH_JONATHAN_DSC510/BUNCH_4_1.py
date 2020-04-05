# File: BUNCH_4_1.py
# Name: Jonathan Bunch
# Date: 5 April, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# This week we will modify our If Statement program to add a function to do the heavy lifting.
# Modify your IF Statement program to add a function. This function will perform the cost calculation.
# The function will have two parameters (feet and price). When you call the function, you will pass two arguments
# to the function; feet of fiber to be installed and the cost (remember that price is dependent on the number of
# feet being installed). You probably should have the following:
# A welcome message
# A function with two parameters
# A call to the function
# The application should calculate the cost based upon the number of feet being ordered
# A printed message displaying the company name and the total calculated cost


# This function takes the argument feet that we collect from the user and returns the price based on the bulk discount.
def price_tier(length):
    if length > 500:
        price = 0.50
    elif length > 250:
        price = 0.70
    elif length > 100:
        price = 0.80
    else:
        price = 0.87
    return price


# This function takes our two arguments, feet of cable and price per foot, and returns the total cost.
def calculate_cost(feet, price):
    cost = feet * price
    return cost


# Print a welcome message for the user.
print('Welcome to our digital quoting system!')


# Prompt the user to enter a company name, and assign the name to a new variable.
company_name = input('Please enter your company name:')


# Prompt the user to enter feet of cable requested, and assign that value to another variable.
feet_cable = input('How many feet of fiber optic cable will you be installing?:')


# Python will return the input value as an "int" type, so we must convert it to a "float" type for compatibility with
# the "price_per_foot" variable.  Note: the program will crash here if the user enters any non-numbers.
feet_cable = float(feet_cable)


# Now that we have the length, we can call our "price_tier" function to determine the price per foot.
price_per_foot = price_tier(feet_cable)


# Now that we have determined length and price we can call "calculate_cost" and pass those values in as arguments.
total_cost = calculate_cost(feet_cable, price_per_foot)


# Print a receipt for the user based on the values of our variables, and format output to standard monetary format.
print('')
print('Thank you for using our digital quoting system.  Please see your quote below.')
print('Company:', company_name)
print(f'Feet of cable requested: {round(feet_cable, 2):.2f}')
print(f'Price per foot: ${price_per_foot:.2f}')
print(f'Total Cost: ${round(total_cost, 2):.2f}')
print('Thank you for considering us for your cable installation needs!')

