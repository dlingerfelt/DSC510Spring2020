# Program Name: Fiber Cable Receipt
# Calculate the total cost based on the amount of feet requested.
# Provide discount to the customer based on the qty they order.
# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
# Author: Rajkumar Kupuswamii
# Date:Sunday, March 29, 2020
# Display a welcome message for your user.
# Retrieve the company name from the user.
# List the discount price based on the feet
# Get the number of feet of fiber optic cable to be installed  from the users
# Calculate the total cost based on the feet purchased against the discount price 

import datetime as dt
#Set variable
space= " "
Symbol1 = "#"
amt = 0.87
Amtmorethan500= 0.50
Amtmorethan250=0.70
Amtmorethan100=0.80
#Get the input
Quotation_date = dt.date.today().strftime("%d/%m/%y")
print("Welcome to fiber optics installation company")
get_input = input("Please enter your company name :")
company_name = get_input

print('Dear' + company_name + ', We are offering discounts on fiber cable.' + '\n' +
      'On purchasing more than 100 feet of fiber optic cable our discount price is $0.80 per feet' + '\n' +
      'More than 250 feet then our discount price is $0.70' + '\n' +
      'More than 500 feet then our discount price is $0.50' + '\n'
      'Less than 100 feet then our discount price is $0.87' + '\n')

get_input = input("Please enter the feet for fiber optics installation :")
#get input qty
qty = round(float(get_input), 2)

#Calculate the qty * Cost
total_cost_of_installation = round(qty * amt, 2)
if qty > 500: total_cost_of_installation = round(qty * Amtmorethan500,2)
elif qty > 250: total_cost_of_installation = round(qty * Amtmorethan250,2)
elif qty > 100: total_cost_of_installation = round(qty * Amtmorethan100,2)
else: total_cost_of_installation = round(qty * amt, 2)
#Print the output
print (Symbol1*80 + '\n' +
     '' + space*20 + "Price for fiber Optics Installation after discount" + space*10 + '' + '\n'+
      Quotation_date + '\n'+
      company_name + '\n' +
      Symbol1*80 + '\n' +
'Number of Feet to be Installed: ' + str(qty) + ' qty\n' +
      '      Fiber Installation cost: $' + str(total_cost_of_installation) + '\n' +

      Symbol1 * 80 + '\n' +
      '   Total cost of Installation: $' + str(total_cost_of_installation) + '\n' +
      Symbol1 * 80)
