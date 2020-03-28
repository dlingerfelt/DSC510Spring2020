# File: Assignment_3_1.py
# Name: Roni Kaakaty
# Date: 03/28/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: The program will do the following:
# Display a welcome message for the program.
# Retrieve the company name from the user.
# Evaluate total cost based on the amount of feet requested.
# Display the calculated information including the number of feet requested and company name.
# Incorporate a bulk discount based on the amount of feet purchased.
# If the user purchases >100 feet then the cost will be $0.80 per foot.
# If the user purchases >250 feet then the cost will be $0.70 per foot.
# If the user purchases >500 feet then the cost will be $0.50 per foot.

print('Welcome to our cost estimator')  # Welcome message

companyName = input('What is your company name?\n')  # Retrieve company name

print('Let me provide you with a breakdown of our costs')  # Cost breakdown


print('We charge $0.87 per foot for jobs requiring less than 100 feet of fiber optic cable')
print('We charge $0.80 per foot for jobs requiring 100-250 feet of cable')
print('We charge $0.70 per foot for jobs requiring 250-500 feet of cable')
print('We charge $0.50 per foot for jobs requiring more than 500 feet of cable')

FoAmount = int(input('How many feet of fiber optic cable would you like installed?\n'))  # Retrieve cable feet needed
FoNeed = float(FoAmount)  # Convert to float

if FoNeed > 500:
    FoCost = (.50 * FoNeed)  # If greater than 500 feet, charge $.50 per ft.
elif FoNeed > 250:
    FoCost = (.70 * FoNeed)  # If greater than 250 feet, charge $.70 per ft.
elif FoNeed > 100:
    FoCost = (.80 * FoNeed)  # If greater than 100 feet, charge $.80 per ft.
else:
    FoCost = (.87 * FoNeed)  # Anything under than 100 feet, charge $.87 per ft.

print('YOU HAVE OPTED TO PURCHASE ' + str(FoAmount) + 'FT OF FIBER OPTIC CABLE')
print('YOUR TOTAL COST IS $' + str(FoCost))

print('THANK YOU ' + str(companyName) + ', FOR YOUR BUSINESS')

