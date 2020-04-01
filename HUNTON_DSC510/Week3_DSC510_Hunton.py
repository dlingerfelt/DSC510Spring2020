# File: Assignment_3_1.py
# Name:  Deborah Hunton
# Due Date: 3/29/20
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: The program will do following:
# Display a welcome message for your program.
# Get the company name from the user.
# Get the number of feet of fiber optic cable to be installed from the user.
# Calculate the cost of fiber optic cable installation by multiplying the number of feet needed by $0.87.
# Evaluate a bulk discount.
# Using the default value of $0.87 calculate the total expense.
# If the user purchases more than 100 feet they are charged $0.80 per foot.
# If the user purchases more than 250 feet they will be charged $0.70 per foot.
# If they purchase more than 500 feet, they will be charged $0.50 per foot.
# Prompt the user for the number of fiber optic cable they need installed.
# Evaluate the total cost based upon the number of feet requested.
# Display the calculated information including the number of feet requested and company name.

# Welcome user
print('Hello, welcome to the ABC Cabling Estimating System\n')

# Gather Info
comp_name = input('What is your company name?\n')
ft_cable = input('How many feet of fiber optic cable will you need?\n')

# Calculate cost after converting ft_cable input to integer,
# taking into account bulk discounts
try:
    length = int(ft_cable, base=10)
    if length < 1:
        print("I can't calculate a cost using a negative length.")
    elif length > 500:
        cost  = length * 0.50
    elif length > 250:
        cost = length * 0.70
    elif length > 100:
        cost = length * 0.80
    else:
        cost = length * 0.87

    # Print receipt
    if length >= 1:
        print('Thank you for using the ABC Cabling Estimating System')
        print('Company: ', comp_name)
        print('Cable Length:', ft_cable, ' ft')
        print('Total Cable Cost: ${:,.2f}'.format(cost))

except:
    print("I'm sorry, but I didn't understand the length you need.")
