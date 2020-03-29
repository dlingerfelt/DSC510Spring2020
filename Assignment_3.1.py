print('Welcome to Flip Floptics Fiber Optics!') #Welcome to our company
print('What is your company name?') #Ask for their company name
companyName=input()
print('Welcome' + companyName + ' to Flip Floptics Fiber Optics for all your Fiber Optic installation needs!')
print('How many feet of fiber optic cable do you need installed?') #How many feet of fiber optic they need
feet_of_fiber_optic=int(input())
if feet_of_fiber_optic<=100:
    cost_calculation=str(int(feet_of_fiber_optic)*.87)  #Price for less than 100 feet
elif feet_of_fiber_optic>100 and feet_of_fiber_optic<=250:
    cost_calculation=str(int(feet_of_fiber_optic)*.80)  #Price for between 100 and 250
elif feet_of_fiber_optic>250 and feet_of_fiber_optic<=500:
    cost_calculation=str(int(feet_of_fiber_optic)*.70)  #Price for between 250 and 500
elif feet_of_fiber_optic>500:
    cost_calculation=str(int(feet_of_fiber_optic)*.50)  #Price for over 500 feet
print('The cost of your fiber optic installation is $'+cost_calculation)  #Calculates cost and sends to user

#Start of the receipt/order confirmation
print('Here is all the information about your order! Thank you for choosing Flip Floptics Fiber Optics!')
print('Your company name: '+companyName)
print('Feet of fiber optic installed: '+str(feet_of_fiber_optic) + ' feet')
print('Your price: $'+cost_calculation)