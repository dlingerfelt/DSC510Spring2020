# File: Assignment_3_1.py
# Sara Herbstreit
# 03/29/20
# DSC510-T303 Introduction to Programming (2203-1)

# Retrieve Company name
company = input('Welcome! Which company are you shopping for?\n')
# Tell about discounts
print('Bulk discount can apply')
print('500+ feet is $0.50/foot')
print('251-499 feet is $0.70/foot')
print('101-250 feet is $0.80/foot')
print('Under 100 feet is $0.87/foot')
# Retrieve number of feet desired.
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
# Multiply feet by price
cost = int(price * feet)
# Convert price to $x.xx
price = '{0:.2f}'.format(price)
price = '$' + str(price)
# Convert cost to $x.xx
cost = '{0:.2f}'.format(cost)
cost = 'The total cost is $' + str(cost)
# Display total cost
print(cost)
# Display receipt
print('Receipt')
# Display company name
print(company)
# Display feet requested
print('Feet requested')
print(feet)
# Display price per foot
print('Price per foot')
print(price)
# Display total cost
print(cost)
