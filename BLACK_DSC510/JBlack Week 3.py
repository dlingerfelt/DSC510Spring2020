# course: DSC510
# assignment: 3.1
# due date: 3/29/2020
# name: Jessica Black
# this program will do the following:


# Display a welcome message for your program
# Retrieve the company name from the user
# Get the number of feet of fiber optic cable to be installed from the user.
# Evaluate the total cost based upon the number of feet requested.
# Display the calculated information including the number of feet requested and company name.

# One - Display welcome message
user_name = input('Hello, user! Thanks for visiting Fiber Optic Inc. We look forward to assisting you. What is your name?')
print(f'Welcome, {user_name}')

# Two - Retrieve Company Name
Company_Name = input('What is your company name?:\n')
print(f'Welcome {Company_Name}!')

# Three - Retrieve the number of feet of fiber optic cable to be installed from the user
Cable_Length = input('How much feet of fiber optic cable needs to be installed?\n')
print(f'Got it, you need {Cable_Length} feet of fiber optic cable.')

# You will prompt the user for the number of fiber optic cable they need installed.
# Using the default value of $0.87 calculate the total expense.
# If the user purchases more than 100 feet they are charged $0.80 per foot.
# If the user purchases more than 250 feet they will be charged $0.70 per foot.
# If they purchase more than 500 feet, they will be charged $0.50 per foot.

Default_Price = .87
Price_100_Feet = .80
Price_250_Feet = .70
Price_500_Feet = .50

Cable_Needed = float(Cable_Length)

if Cable_Needed > 500:
    print(f'For {Cable_Needed} feet of fiber optic cable, you will be charged $.50 per foot.')
elif Cable_Needed > 250:
    print(f'For {Cable_Needed} feet of fiber optic cable, you will be charged $.70 per foot.')
elif Cable_Needed > 100:
    print(f'For {Cable_Needed} feet of fiber optic cable, you will be charged $.80 per foot.')
elif Cable_Needed < 100:
    print(f'For {Cable_Needed} feet of fiber optic cable, you will be charged $.87 per foot.')

f'\n'

if Cable_Needed > 500:
    Total_Cost = (.50 * Cable_Needed)
elif Cable_Needed > 250:
    Total_Cost = (.70 * Cable_Needed)
elif Cable_Needed >= 100:
    Total_Cost =  (.80 * Cable_Needed)
else:
    Total_Cost = (.87 * Cable_Needed)

print(f'For {Cable_Needed} feet of cable, your total installation cost will be ${Total_Cost}')

print(f'Thank you, {user_name} with {Company_Name}! Fiber Optic Inc. looks forward to working with you.')
