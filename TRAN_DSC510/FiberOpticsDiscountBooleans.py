# File: Assignment_3.1
# Name: Hanh Tran
# Due Date: 3/29/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: This program will do the following:
# Display a welcome message for program.
# Get the company name from the user.
# Get the number of feet of fiber cable to be installed from the user.
# Evaluate the total cost based upon the number of feet requested.
# Display calculated information of feet requested and company name.

print('Welcome to the Fiber Optic Cable installation cost estimator\n')
company_name = input('What is your company name?\n')#
# retrieve number of feet needed from user in positive whole integers only
cable_feet = int(input('How many feet of cable do you need installed?\n'
                       'Please enter whole numbers only\n'))
# calculated total cost depending on number of feet, no discount
if cable_feet <= 100:
    price = .87
    total_cost = cable_feet * price
# calculated discount schedule, greater than 100 feet
elif 250 >= cable_feet >= 101:
    price = .80
    total_cost = cable_feet * price
elif 500 >= cable_feet >= 251:
    price = .70
    total_cost = cable_feet * price
elif cable_feet >= 501:
    price = .50
    total_cost = cable_feet * price

# Display company name and calculated information including number of feet
print(company_name)
print('This is the total cost calculation of your installation:')
print('Discount price per feet only if you request more than 100ft:', price)
print('Quantity of feet you need:', cable_feet)
print(f'Your calculated total cost: ${total_cost:,.2f}')







