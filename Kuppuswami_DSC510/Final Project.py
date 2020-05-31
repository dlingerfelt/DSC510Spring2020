#Algoritham to get input from the user for their city or zip code and request weather forecast data from OpenWeatherMap
#Python Application which asks the user for their zip code or city.
#Allows the user to select City or zipcode
#DSC510-T303 Introduction to Programming (2205-1)
#Created by Rajkumar Kuppuswami
#Created on 06/01/2020
#welcome message for the user
#Use try Except method to catch the error and display.

import requests

api_key = '657347e2ddf92cec868c3a7f1a49d70b'
api_call = 'http://api.openweathermap.org/data/2.5/forecast?appid=' + api_key

execute = True
print('-' * 100)
print('Welcome to weather forecast application using OpenWeatherMap\'s API!')
print('-' * 100)
# Program loop
while execute:

    # Asks the user for the city or zip code to be queried
    while True:

        # Input validation
        try:
            print('\nChoose 0 to input city or Choose 1 to input Zipcode')
            search = int(input('Please input 0 or 1: '))
        except ValueError:
            print("Sorry, Incorrect entry please try again ")
        else:

            # Passed the validation test
            if search == 0:
                city = input('Please input the city name: ')
                if city.lower() == 'au':
                    city = 'Austin, US'

                # Appends the city to the api call
                api_call += '&q=' + city
                break

            elif search == 1:
                zip_code = input('Please input the zip code: ')

                # Appends the zip code to the api call
                api_call += '&zip=' + zip_code
                break

            else:
                # Prints the invalid number (not 0 or 1)
                print('{} is not a valid option.'.format(search))

    # Load the Json values
    json_data = requests.get(api_call).json()

    location_data = {
        'city': json_data['city']['name'],
        'country': json_data['city']['country']
    }
    # Iterates through the array of dictionaries named list in json_data
    for item in json_data['list']:
    # Weather condition with all the attributes
        temperature = item['main']['temp']
        description = item['weather'][0]['description']
        Wind_speed = item['wind']['speed']
        Weather = item['weather'][0]['main'],
# Prints the description,Temperature,convert to celcius/Farenheit,weather condition,wind speed
    print('-' * 100)
    print('{city}, {country}'.format(**location_data))
    print('\nCurrent Temperature: %s' % temperature)
    print('Celcius: {:.2f}'.format(temperature - 273.15))
    print('Farenheit: %.2f' % (temperature * 9 / 5 - 459.67))
    print('Weather condition: %s' % description)
    print('Wind_speed: %s' % Wind_speed)
    print('Weather: %s' % Weather)

#Exit or try again the program id user like to continue
    while True:
        print('-' * 100)
        running = input('\nWould you like to try Again?')
        print('-' * 100)
        if running.lower() == 'yes' or running.lower() == 'y':
            break
        elif running.lower() == 'no' or running.lower() == 'n' or running == 'exit':
            print('Thank you for using weather forecast Program')
            print('-' * 100)
            running = False
            break
        else:
            print('Sorry, Can you please enter correct value')

