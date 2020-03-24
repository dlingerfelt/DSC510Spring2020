# Program Name: Quotation for Fiber Cable Installation
#Calculate the installation cost of fiber optic cable by multiplying the total cost as the number of feet times $0.87.
# Print a receipt for the user including the company name, number of feet of fiber to be installed, the calculated cost, and total cost in a legible format.
# Author: Rajkumar Kupuswamii
# Date:Wednesday, March 21, 2020
# Display a welcome message for your user.
# Retrieve the company name from the user.
# Retrieve the number of feet of fiber optic cable to be installed from the user.

import datetime as dt
#Set variable
space= " "
Symbol1 = "#"
amt = 0.87
#Get the input
Quotation_date = dt.date.today().strftime("%d/%m/%y")
print("Welcome to fiber optics installation company")
get_input = input("Please enter your company name :")
company_name = get_input
get_input = input("Please enter the feet for fiber optics installation :")
#get input qty
qty = round(float(get_input), 2)
#Calculate the qty * Cost
total_cost_of_installation = round(qty * amt, 2)
#Print the output
print (Symbol1*80 + '\n' +
     Symbol1 + space*20 + "Quotation for fiber Optics Installation" + space*10 + Symbol1 + '\n'+
      Quotation_date + '\n'+
      company_name + '\n' +
      Symbol1*80 + '\n' +
'Number of Feet tobe Installed: ' + str(qty) + ' qty\n' +
      '      Fiber Installation cost: $' + str(total_cost_of_installation) + '\n' +

      Symbol1 * 80 + '\n' +
      '   Total cost of Installation: $' + str(total_cost_of_installation) + '\n' +
      Symbol1 * 80)
