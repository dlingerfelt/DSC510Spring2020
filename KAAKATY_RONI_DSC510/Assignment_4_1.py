# File: Assignment_4_1.py
# Name: Roni Kaakaty
# Date: 04/05/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: The program will do the following:
# Display a welcome message for the program.
# Retrieve the company name from the user.
# Add a function with two parameters to perform cost function.
# Call function with two arguments (feet of fiber to be installed and cost)
# Incorporate a bulk discount based on the amount of feet purchased.
# If the user purchases >100 feet then the cost will be $0.80 per foot.
# If the user purchases >250 feet then the cost will be $0.70 per foot.
# If the user purchases >500 feet then the cost will be $0.50 per foot.
# Display company name and total calculated cost.

print('Welcome to our cost estimator')  # Welcome message

companyName = input('What is your company name?\n')  # Retrieve company name

print('Let me provide you with a breakdown of our costs')  # Cost breakdown


print('We charge $0.87 per foot for jobs requiring less than 100 feet of fiber optic cable')
print('We charge $0.80 per foot for jobs requiring 100-250 feet of cable')
print('We charge $0.70 per foot for jobs requiring 250-500 feet of cable')
print('We charge $0.50 per foot for jobs requiring more than 500 feet of cable')

feet = float((input('How many feet of fiber optic cable would you like installed?\n')))  # Retrieve cable feet needed

def disc_func(feet, price):  # Function with two parameters to get price
    if feet > 500:
        price = 0.50
    elif feet > 250:
        price = 0.70
    elif feet > 100:
        price = 0.80
    elif feet <100:
        price = 0.87
    print ('Price per foot is......................................' + '$' + '{:.2f}'.format(price))  # Convert to 2 decimal places

def total_cost(feet, price):  # Function to calculate total installation costs
    calc_cost = round(feet * price, 2)
    print ('The total installation cost comes out to.............' + '$' + '{:.2f}'.format(calc_cost))  # Convert to 2 decimal places

print ('Total number of fiber optic cable requested..........' + str(feet) + 'ft')

disc_func(feet, .70)  # Call the function to get discounted price
total_cost(feet, .70)  # Call the function to get total installation cost

print ('Thank you, ' + companyName + ', for your business')
