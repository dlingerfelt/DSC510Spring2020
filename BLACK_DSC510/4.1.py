# course: DSC510
# assignment: 4.1
# due date: 4/5/2020
# name: Jessica Black
# this program will do the following:


# Modify your IF Statement program to add a function. This function will perform the cost calculation.
# The function will have two parameters (feet and price).
# When you call the function, you will pass two arguments to the function; feet of fiber to be installed and the cost
# (remember that price is dependent on the number of feet being installed). You probably should have the following:
# Your program must have a header. Use the SIU Edwardsville Programming Guide for guidance.
# A welcome message
# A function with two parameters
# A call to the function
# The application should calculate the cost based upon the number of feet being ordered
# A printed message displaying the company name and the total calculated cost

Default_Price = .87
Price_100_Feet = .80
Price_250_Feet = .70
Price_500_Feet = .50


def Cost(Cable_Length, Price_Per_Foot):
    Cost = Cable_Length * Price_Per_Foot
    return '$''{0:.2f}'.format(Cost)

# One - Display welcome message
user_name = input('Hello, user! Thanks for visiting Fiber Optic Inc. We look forward to assisting you. What is your name?')
print(f'Welcome, {user_name}')

# Two - Retrieve Company Name
Company_Name = input('What is your company name?:\n')
print(f'Welcome {Company_Name}!')

# Three - Retrieve the number of feet of fiber optic cable to be installed from the user
Cable_Length = int(input('How much feet of fiber optic cable needs to be installed?\n'))
print(f'Got it, you need {Cable_Length} feet of fiber optic cable.')

# You will prompt the user for the number of fiber optic cable they need installed.
# Using the default value of $0.87 calculate the total expense.
# If the user purchases more than 100 feet they are charged $0.80 per foot.
# If the user purchases more than 250 feet they will be charged $0.70 per foot.
# If they purchase more than 500 feet, they will be charged $0.50 per foot.

Cable_Needed = float(Cable_Length)

if Cable_Length > 500:
    print(f'For {Cable_Length} feet of fiber optic cable, you will be charged $.50 per foot.')
elif Cable_Length > 250:
    print(f'For {Cable_Length} feet of fiber optic cable, you will be charged $.70 per foot.')
elif Cable_Length > 100:
    print(f'For {Cable_Length} feet of fiber optic cable, you will be charged $.80 per foot.')
elif Cable_Length < 100:
    print(f'For {Cable_Length} feet of fiber optic cable, you will be charged $.87 per foot.')


f'\n'

if Cable_Length > 500:
    Price_Per_Foot = .50
elif Cable_Length > 250:
    Price_Per_Foot = .70
elif Cable_Length >= 100:
    Price_Per_Foot = .80
else:
    Price_Per_Foot = .87

print(f'For {Cable_Needed} feet of cable, your total installation cost will be {Cost(Cable_Length, Price_Per_Foot)}')
print(f'Thank you, {user_name} with {Company_Name}! Fiber Optic Inc. looks forward to working with you.')
