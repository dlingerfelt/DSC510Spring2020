# File: Assignment_4.1
# Name: Hanh Tran
# Due Date: 4/5/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: This program will do the following:
# Display a welcome message for program
# A function with two parameters, feet and price
# A call to the function
# Calculate the cost based on the number of feet ordered
# Print message displaying company name and total calculated cost

print('Welcome to the Fiber Optic Cable installation cost estimator\n')
company_name = input('What is your company name?\n')
# Defined a function with two parameters, feet and price
def func_cost(feet, price):
    if feet <= 100:
        price = .87
    elif 250 >= feet >= 101:
        price = .80
    elif 500 >= feet >= 251:
        price = .70
    elif feet >= 501:
        price = .50
    return feet * price
# call function and pass by reference argument, feet of cable and pass by value price/cost
# price is dependent on the number of feet being installed
feet = int(input('How many feet do you need installed?\n'))
func_cost(feet, .80)
# assigned a variable to function to print calculated cost
total_cost = func_cost(feet, .80)
# printed message displaying company name and total calculated cost in USD
print(company_name + ', Thank you for using the cable cost calculater.\n')
# printed calculated cost based upon number of feet ordered
print(f'Total Calculated Cost: ${total_cost:,.2f}')
