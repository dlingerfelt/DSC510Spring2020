# File: Assignment_2_1.py
# Name: Deborah Hunton
# Due Date: 3/22/20
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: The program will do followings:
# Display a welcome message for your program.
# Get the  company name from the user.
# Get the number of feet of fiber optic cable to be installed from the user.
# Evaluate the total cost based upon the number of feet requested.
# Display the calculated information including the number of feet requested and company name.


# Welcome user
print('Hello, welcome to the ABC Cabling Estimating System\n')

# Gather Info
comp_name = input('What is your company name?\n')
ft_cable = input('How many feet of fiber optic cable will you need?\n')

# Check to make sure that user input a positive number of feet
if int(ft_cable) > 0:

    # Calculate cost after converting ft_cable input to integer
    length = int(ft_cable, base=10)
    cost  = length * 0.87

    # Print receipt
    print('Thank you for using the ABC Cabling Estimating System')
    print('Company: ', comp_name)
    print('Cable Length:', ft_cable, ' ft')
    print('Total Cable Cost: ${:,.2f}'.format(cost))

else:
    
    print("I'm sorry, but that isn't a valid entry.")