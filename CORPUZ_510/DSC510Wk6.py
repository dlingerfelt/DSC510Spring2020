"""
File : DSC510Wk6.py
Name: Caleb Corpuz
Date: 04/15/2020
Course: DSC510-T303 Introduction to Programming (2203-1)
Description: The program will do the following:
Ask the user how many temperatures they wish to input
Prompt the user to input a temperature
Display the max and min temperatures
Tell the user how many temperatures there are
"""

#Create an empty list, the temperatures the user enters will be appended to this list
temperatures = []

#Ask the user how many temperatures they want to input, this value is used to set number of times of the loop
num_temp = int(input("Enter the number of temperatures you wish to input:"))

loop_value = 1

#ASks the user to enter a temperature and adds this temperature to the list temperatures
while loop_value <= num_temp:
    user_input = float(input("Enter a temperature: "))
    temperatures.append(user_input)
    loop_value = loop_value + 1

print("Max Temperature:", max(temperatures),
    "\n" "Min Tempurature:", min(temperatures),
    "\n" "Number of temperatures:",  len(temperatures))







