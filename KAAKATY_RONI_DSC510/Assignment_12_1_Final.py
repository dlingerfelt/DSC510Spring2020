# File: Assignment_12_1.py
# Name: Roni Kaakaty
# Date: 05/29/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# The program will do the following:
# Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap
# Display weather forecast in a readable format to the user.
# Use comments to document what the program is doing.
# Use functions including a main function.
# Allow the user to run the program multiple times to allow them to look up conditions for multiple locations.
# Validate whether the user entered valid data. Notify user if not valid.
# Use request library in order to request data from webservice.
# Use try blocks to ensure request successful.
# Use Python 3

import requests

def main():  # Main function that houses the various created functions and starts the program when called.
    print("~" * 40)
    print("*" * 40)
    print('Welcome to our weather forecast program!')
    print("*" * 40)
    print("~" * 40)
    program = True
    while True:
        try:
            user_location_input = input('Enter your desired city or zipcode forecast to begin, or enter "Exit" when completed: ')  # Captures user's city or zipcode input.
            if user_location_input.lower() =='exit':  #  allows either Exit or exit to process.
                program = False
                print ('Thanks for visiting.')
                break  # Breaks the loop
            else:
                city = user_location_input  # Creates a smaller variable to track for the user input.
                weather_info = retrieve_api(city) # Variable that calls the function that gets the API.
            format_weather(weather_info)  # Calls the formatting function that was created.
        except:
            print('Invalid entry, please check your entry and try again')  # Captures the errors.



def retrieve_api(city):  # Gets the API from the webservice.
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=8788182a2474c03991c8e54ecbb677bb&units=imperial'.format(city)  # Includes base URL+place holder for city input+unique appID+US units.
    try:
        res = requests.get(url)  # requests the API.
        data = res.json()  # Parses data using json.
    except ValueError:
        print('Invalid entry, please check your input and try again')
    return data

def format_weather(weather_info): # formatting function that presents the data in a readable format.
    city_name = weather_info['name']
    latitude = weather_info['coord']['lat']
    longitude = weather_info['coord']['lon']
    current_temp = weather_info['main']['temp']
    feels_like = weather_info['main']['feels_like']
    wind_speed = weather_info['wind']['speed']
    temp_max = weather_info['main']['temp_max']
    temp_min = weather_info['main']['temp_min']
    humidity = weather_info['main']['humidity']
    weather_description = weather_info["weather"]
    description = weather_description[0]["description"]
    print("*" * 40)
    print('The current conditions in {} are:'.format(city_name))
    print('\t')
    print('Description:    {}'.format(description))
    print('Temperature:       ', current_temp)
    print('Feels like:         {}'.format(feels_like))
    print('Latitude:           {}'.format(latitude))
    print('Longitude:         {}'.format(longitude))
    print('Wind speed:      {} m/s'.format(wind_speed))
    print('High for the day:      {}'.format(temp_max))
    print('Low for the day:    {}'.format(temp_min))
    print('Humidity:             {}%'.format(humidity))
    print('\t')

main()  # Starts the program.