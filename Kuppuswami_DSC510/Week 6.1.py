#Algoritham to get user input and store in the list
#Assignment Number 6.1
#DSC510-T303 Introduction to Programming (2205-1)
#Created by Rajkumar Kuppuswami
#Created on 04/18/2020
#Output to get the Min,Max and size of the list

#Creating Empty list called temperatures
temperatures=[]
def Perform_Calculations():
    Max_Temp= max(temperatures)
    Min_Temp= min(temperatures)
    Len_Temp= len(temperatures)
    print("The Elements inside the temperatures list are : ",temperatures)
    print ("The Maximum temperature in the list is : ", Max_Temp)
    print ("The Minimum temperature in the list is : ", Min_Temp)
    print ("The Size of the temperature list is : ", Len_Temp)

while True:# looping the user inputs
    getuser_input= input("Enter the temperatures \n"
                         "Enter exit to stop the Loop :" )
    if getuser_input=='exit':
        break# to exit the loop
    else:
        try:
            temperatures.append(float(getuser_input))
        except ValueError: #exception handling for invalid entries
            print("Please enter Integer or Float")

# OUTPUT

Perform_Calculations()




