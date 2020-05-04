# File: Assignment_6_1.py
# Name: Roni Kaakaty
# Date: 04/19/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# This program will do the following:
# Create an empty list called temperature.
# Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
# Evaluate the temperature list to determine the largest and smallest temperature.
# Print the largest temperature.
# Print the smallest temperature.
# Print a message that tells the user how many temperatures are in the list.

temperature = []  # Empty temperature list

def main(): # Creating a function to be easily called to use.
    print('Welcome to our weather program!')

    while True:  # Creating a loop with user input
        user_input = input('Please provide a temperature and enter "done" when completed:')
        if user_input.lower() == 'done':  # Sentinel value to end the loop, formats to lowercase.
            break
        try:
            temperature.append(float(user_input))  # Adding temperatures to list and converting to float type.
        except ValueError:  # Error message when non-numerical characters provided.
            print ('Please enter a valid number.')

    print('The maximum temperature entered is: ', max(temperature), 'degrees Fahrenheit')  # Identifies max temp.
    print('The minimum temperature entered is: ', min(temperature), 'degrees Fahrenheit')  # Identifies min temp.
    print('There amount of temperatures entered is: ', len(temperature))  # Identifies how many items entered in list.

main()






