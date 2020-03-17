#The purpose of this program is to retrieve company name and number of feet of fiber optic cable to be installed from user, Assignment number 2.1, Hanh Tran
username= input('What is your username?\n')
print('Welcome '+ username)
company_name=input('What is your company name?\n')
quantity= input('How many feet of fiber optic cable do you want installed?\n') #quantity of fiber optic cable in feet
price= 0.87
total_cost= float(quantity)*price #Calculate installation cost of fiber optic cable to be installed from user
#Receipt for user
print('Receipt\n')
print(username)
print(company_name)
print('-------------------------------------------------\n')
print('ITEM\t\t\t\t\tFiber Optic Cable')
print('QUANTITY IN FEET\t\t\t'+str(quantity))
print('PRICE PER FEET\t\t\t\t'+str(price))
print('-------------------------------------------------\n')
print('Total Cost\t\t\t\t\t'+str(total_cost))




