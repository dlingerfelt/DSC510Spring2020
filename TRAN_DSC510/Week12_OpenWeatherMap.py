# File: Assignment_12.1
# Name: Hanh Tran
# Due Date: 5/31/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)
# Desc: This program will do the following:
# Prompt user for their zip code to request weather forecast data from One Weather Map
# Display the retrieved weather information in a readable format
# Use functions including a main function
# Allow the user to run the program multiple times to allow them to look up weather conditions for many locations
# Validate whether the user entered valid data. If data is not valid, the user is notified to re-enter zip code
# Use the requests library to request data from webservice. Use try blocks to ensure request was successful
# Display a fail message if the connection was not successful

# import request library to request data from webservice
import requests
import json
import http
from pprint import pprint

# Created function to request data from API webservice, One Weather Map
def service_weather(zip_code):
    # service url includes API key, zip code format and set to imperial units
    url = 'https://api.openweathermap.org/data/2.5/weather?zip={}&appid=34c7532ca1f824b7dd2518fcb9bc2ecf&units=imperial'.format(zip_code)
    try:
        res = requests.get(url)
        res.raise_for_status()
    # Use try block to notify user connection was not successful so they can try again
    except requests.exceptions.HTTPError as fail:
        print(f'==== Cannot Connect: Please retry your entry ====')
    # Use try block to notify user that connection was successful
    if res.status_code == http.HTTPStatus.OK:
        print('==Connection to Open Weather Successful!==')
        return res.json()

# created function to display weather information in readable format
def pretty_print(data):
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max =  data['main']['temp_max']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    print('Description: {}'.format(description))
    print('Current Temperature: {} F'.format(temp))
    print('Feels Like Temperature: {} F'.format(feels_like))
    print('Temperature Low: {} F'.format(temp_min))
    print('Temperature High: {} F'.format(temp_max))
    print('Humidity: {} %'.format(humidity))
    print('Wind Speed: {} mph'.format(wind_speed))
    print('=' * 38)
# created main function to run program as a loop
def main():
    print('Welcome to the Open Weather Program!')
    print('=' * 38)
    # created a while loop to allow user to run the program multiple times to allow them to look up many locations
    while True:
        zip_code = input('Please enter a 5-digit zip code:\n')
        try:
            pretty_print(service_weather(zip_code))
        except:
            print('Invalid zip code. Please re-renter a 5-digit zip code')

# call main function
main()
