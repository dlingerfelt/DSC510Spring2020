# File: billingInvoice_assignment2_1.py
# Author: Bhushan Suryawanshi
# Date:Wednesday, April 01, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)
# Desc: The program will do followings:
# Display a welcome message for your user.
# Retrieve the company name from the user.
# Retrieve the number of feet of fiber optic cable to be installed from the user.
# Using the default value of $0.87 calculate the total expense.
# If the user purchases more than 100 feet they are charged $0.80 per foot.
# If the user purchases more than 250 feet they will be charged $0.70 per foot.
# If they purchase more than 500 feet, they will be charged $0.50 per foot.
# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost,
# and total cost in a legible format.


import datetime as date


def main():
    # Setup basic data items
    other_cost = 0.0
    more_than_100_feet_price = 0.80
    more_than_250_feet_price = 0.70
    more_than_500_feet_price = 0.50

    print("Welcome to Fiber Installation Cost calculator.")
    input_value = input("Please Enter your Company Name:->")
    company_name = input_value
    input_value = input("Enter the Fiber to be Installed (in feet):->")

    # Convert input string to float and round the value to 2 decimal.
    feet = round(float(input_value), 2)

    # Calculate the cost of installing fiber and round to 2 decimal.
    if feet > 500:
        cost = calculate_cost(feet, more_than_500_feet_price)
    elif feet > 250:
        cost = calculate_cost(feet, more_than_250_feet_price)
    elif feet > 100:
        cost = calculate_cost(feet, more_than_100_feet_price)
    else:
        cost = calculate_cost(feet)

    display(feet, cost, other_cost, company_name)


def calculate_cost(feet, price_per_feet=0.87):
    cost_of_installation = round(feet * price_per_feet, 2)
    return cost_of_installation


def display(feet, cost_of_installation, other_cost, company_name):
    line = '#'
    space = ' '
    dash = '-'

    # Get input from user
    today = date.date.today().strftime("%m/%d/%y")

    # Print receipt showing details.
    print(line * 51 + '\n' +
          line + space * 19 + 'Billing Invoice' + space * 15 + line + '\n' +
          line * 51 + '\n' +
          line + 'Company Name: ' + company_name + ' \n' +
          line + 'Date:' + today + '\n' +
          dash * 51 + '\n' +
          'Number of Feet tobe Installed: {:0.2f}'.format(feet) + ' feet\n' +
          '      Fiber Installation cost: ${:0.2f}'.format(cost_of_installation) + '\n' +
          '                   Other cost: ${:0.2f}'.format(other_cost) + '\n' +
          dash * 51 + '\n' +
          '   Total cost of Installation: ${:0.2f}'.format(cost_of_installation) + '\n' +
          dash * 51)


if __name__ == '__main__':
    main()
