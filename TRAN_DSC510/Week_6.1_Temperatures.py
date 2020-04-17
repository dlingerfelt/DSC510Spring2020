# File: Assignment_6.1
# Name: Hanh Tran
# Due Date: 4/19/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Desc: This program will do the following:
# create a list of temperatures based on user input
# determine the number of temperatures
# determine the largest temperature and the smallest temperature

# created an empty list called temperatures
temperatures = []
count = 0
while True:
    input_temp = input('Please enter a fahrenheit temperature number or done to stop: ')
    # sentinel value, 'done', stops the user input
    if input_temp == 'done':
        break
    try:
        temp = float(input_temp)
    except ValueError:
        print('Invalid input')
        quit()
    count = count + 1
    temperatures.append(round(float(input_temp), 2))
# populated list of temperatures based on user input
print('Your entered list of temperatures in fahrenheit: ', temperatures)
# evaluate and print largest and smallest temperatures
print('Your highest temperature in fahrenheit is: {} F'.format(max(temperatures)))
print('Your lowest temperature in fahrenheit is: {} F'.format(min(temperatures)))
# print message that tells user how many temperatures are in the list
print('The number of temperatures in your list: ' + str(count))


