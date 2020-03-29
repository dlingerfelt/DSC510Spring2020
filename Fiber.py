# Creating a receipt and calculating cost of Fiber Optic Installation, Assignment 2.1, David Lattimer
print('Welcome to Flip Floptics Fiber Optics')
print('Please enter your company name here:')
companyName = input()  # Ask for their company name
print('Welcome ' + companyName)
print('How many feet of fiber optic cable do you need installed?')
feetNeeded = input()  # Ask how much fiber optic cable they need
costFO = str(int(feetNeeded) * .87)
print('The cost of installation will be: $' + costFO)  # Calculating the price

# Start of the receipt
print('Thanks for choosing Flip Floptics Fiber Optics!')
print('For ' + str(int(feetNeeded)) + ' feet of fiber optic cable')
print('The price of installation is: $' + costFO)
print('Thank you ' + companyName + '!')
