"""
File : DSC510Wk6.py
Name: Caleb Corpuz
Date: 04/15/2020
Course: DSC510-T303 Introduction to Programming (2203-1)
Description: The program will do the following:
"""
temperatures = []

user_input = " "

num_temp = int(input("Enter the number of temperatures you wish to input:"))

sentinal_value = 1

while sentinal_value <= num_temp:
    user_input = float(input("Enter a temperature: "))
    temperatures.append(user_input)
    sentinal_value = sentinal_value + 1

#print(temperatures) #Delete this print statement for the final submission

print("Max Temperature:", max(temperatures),
    "\n" "Min Tempurature:", min(temperatures),
    "\n" "Number of temperatures:",  len(temperatures))







