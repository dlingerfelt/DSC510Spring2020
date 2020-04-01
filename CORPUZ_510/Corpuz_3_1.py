"""
File : DSC510Wk3.py
Name: Caleb Corpuz
Date: 03/18/2020
Course: DSC510-T303 Introduction to Programming (2203-1)
Description: The program will do the following:
Display a welcome message for your user.
Retrieve the company name from the user.
Retrieve the number of feet of fiber optic cable to be installed from the user.
Calculate the cost of fiber optic cable installation by multiplying the number of feet needed by $0.87.
Evaluate a bulk discount.
Using the default value of $0.87 calculate the total expense.
If the user purchases more than 100 feet they are charged $0.80 per foot.
If the user purchases more than 250 feet they will be charged $0.70 per foot.
If they purchase more than 500 feet, they will be charged $0.50 per foot.
Prompt the user for the number of fiber optic cable they need installed.
Evaluate the total cost based upon the number of feet requested.
Display the calculated information including the number of feet requested and company name.

"""

print('Hello! Welcome to the cost calculator.')
# Retrieve the company name
company = input('Please enter the company name:')
# Retrieve the length of the cable
cable_length = input('Please enter how many feet of fiber optic cable you desire: ')

# Calculate the cost
if 100 < float(cable_length) <= 250:
    cost_per_foot = 0.80
elif 250 < float(cable_length) <= 500:
    cost_per_foot = 0.70
elif float(cable_length) > 500:
    cost_per_foot = 0.50
else:
    cost_per_foot = 0.87

cost = float(cable_length) * cost_per_foot

print('Company:', company,
      "\n" 'Length of fiber optic cable:', cable_length,
      "\n" 'Cost per foot: $', cost_per_foot,
      "\n" 'Total Cost: $', cost)
