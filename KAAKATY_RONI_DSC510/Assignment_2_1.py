# File: Assignment_2_1.py
# Name: Roni Kaakaty
# Date: 03/21/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: The program will do the following:
# Display a welcome message for the user.
# Retrieve the company name from the user.
# Retrieve the number of feet of fiber optic cable to be installed.
# Calculate installation cost by multiplying numbers of feet x cost of fiber (.87)
# Print a receipt for the user.

userName = input('What is your name?\n')  # Retrieving user's name
print('Welcome ' +userName)
companyName = input('What is your company name?\n')  # Retrieving company name
FoAmount = input('How many feet of fiber optic cable would you like installed?\n')  # Retrieving amount of fiber needed
FoAmount = int(FoAmount)  # Converting to integer
Price = 0.87
Price = float(Price)  # Converting to float
Total = (FoAmount * Price)  # Multiplying feet needed by cost to get total cost.

print(companyName)
print('FIBER OPTIC QTY IN FT  ' + str(FoAmount))
print('PRICE PER FT           ' + str(Price))

print('TOTAL COST IS $' + str(Total))

