# File: BUNCH_6_1.py
# Name: Jonathan Bunch
# Date: 19 April, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Create an empty list called temperatures.
# Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
# Evaluate the temperature list to determine the largest and smallest temperature.
# Print the largest temperature.
# Print the smallest temperature.
# Print a message tells the user how many temperatures are in the list.


# This function will take the list of user inputted temperatures and return the count, min, max, and average values.
# If there are no entries, the function will return 'err'. This prevents crashes from empty/zero values.
def analyze_temps_list(temps):
    items = float(len(temps))
    if items > 0:
        low = min(temps)
        high = max(temps)
        average = sum(temps) / items
        average = round(average, 1)
        results = [items, low, high, average]
    else:
        results = 'err'
    return results


# This function checks that the user input is in numerical format by attempting to convert the value to float() type.
# If the user enters an appropriate response, that value will be converted to a float and returned by the function.
# If the user enters any non-numerical characters the function will return 'err'.
def check_input_type(x):
    try:
        x = float(x)
    except ValueError:
        x = 'err'
    return x


# Initialize variables.
temperatures = []
run_loop = 1


# Print welcome message for the user.
print('Welcome to our temperature tracking program! Please enter a list of temperatures, one by one, for analysis.')


# This loop will continue to collect values from the user and add them to our list until the user enters the sentinel
# value of 'x'. This will break the loop and print the results for the user.
while run_loop == 1:
    get_temp = input('Enter a temperature or enter "x" to finish:')
    if get_temp == 'x':
        output = analyze_temps_list(temperatures)
        if output == 'err':
            print('Error: Please enter at least one temperature before continuing.')
            continue
        else:
            print('Entry complete! Here is the analysis of your temperature list:')
            print('Number of entries: ', output[0])
            print('Minimum temperature: ', output[1])
            print('Maximum temperature: ', output[2])
            print('Average temperature: ', output[3])
            run_loop = 0
            break
    else:
        get_temp = check_input_type(get_temp)
        if get_temp == 'err':
            print('Error: Please enter numerical values only or "x" to finish.')
            continue
        else:
            get_temp = round(get_temp, 1)
            temperatures.append(get_temp)
            print('Entered so far: ', temperatures)
            continue
