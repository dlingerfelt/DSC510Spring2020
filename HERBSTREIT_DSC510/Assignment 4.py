# File: Assignment_4_1.py
# Sara Herbstreit
# 04/04/20
# DSC510-T303 Introduction to Programming (2203-1)

# Retrieve Company name
company = input('Welcome! Which company are you shopping for?\n')
print('Thank you for shopping for ' + company)

# Tell about discounts
print('Bulk discount can apply')
print('500+ feet is $0.50/foot')
print('251-499 feet is $0.70/foot')
print('101-250 feet is $0.80/foot')
print('Under 100 feet is $0.87/foot')


# create cost function
def cost(a, b):
    answer = a * b
    return '$''{0:.2f}'.format(answer)


# Inquire number of feet from user
feet = int(input('How many feet of fiber optic cable do you need?\n'))

# Create variable for price
if feet >= 500:
    price = 0.50
elif feet >= 250:
    price = 0.70
elif feet >= 100:
    price = 0.80
else:
    price = 0.87

# Display total cost
print(feet, 'feet will cost', cost(feet, price))

# Display receipt
print('Receipt')
# Display company name
print('Purchased by:', company)
# Display feet requested
print('Feet requested:', feet)
# Display price per foot
print('Price per foot:', '$''{0:.2f}'.format(price))
# Display total cost
print('The total cost is', cost(feet, price))
