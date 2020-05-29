"""
File: final_project.py
Author: Bhushan Suryawanshi
Date:Wednesday, May 27, 2020
Course: DSC510-T303 Introduction to Programming (2205-1)

Desc: The program will get current weather data for the City.
It has two methods -
get_weather_data – Parameter to the method is valid city. Returns weather data as received from OpenWeather API.
get_time_in_readable_format - converts UTC time into readable format.
process_weather - processes response from weather API. Creates weather object and
                  calls print_weather to print weather information in structured format.

Weather class is blue print of weather object and has class method print_weather.

User can request weather for a city multiple times before they quit by pressing Q/q.
"""
import http
import requests
import datetime


class Weather:
    weather_date = ""
    current_temperature = 0
    feel = 0
    description = ""
    min = 0
    max = 0
    humidity = 0
    wind = 0
    sunrise = ""
    sunset = ""

    def __init__(self, weather_date, current_temperature, feel, description,
                 min, max, humidity, wind, sunrise, sunset):
        self.weather_date = weather_date
        self.current_temperature = current_temperature
        self.feel = feel
        self.description = description
        self.min = min
        self.max = max
        self.humidity = humidity
        self.wind = wind
        self.sunrise = sunrise
        self.sunset = sunset

    def print_weather(self):
        # Print response in readable format
        dash = "-"
        print(dash * 40)
        print(
            f'Today: {self.weather_date} \n'
            f'Current Temperature: {int(self.current_temperature)} F \n'
            f'{dash * 40}\n'
            f'Feels Like : {int(self.feel)} F \n'
            f'Description: {self.description} \n'
            f'Min: {int(self.min)} / Max:{int(self.max)} F \n'
            f'Humidity: {self.humidity}  \n'
            f'Wind: {int(self.wind)} mph \n'
            f'{dash * 40}\n'
            f'Sunrise: {self.sunrise} \n'
            f'Sunset: {self.sunset} \n')


def get_weather_data(city):
    api_key = "c3e41524f473982312cc57bf5778b97a"
    current_weather_api_address = "https://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid={}"
    url = current_weather_api_address.format(','.join(city), api_key)

    try:
        # Request weather data using Current weather api
        response = requests.get(url)

    except Exception as e:
        # Added except block to catch any error from open weather api
        raise Exception(f'Unable to access weather data: {e}')

    # Verify response object for success.
    if response.status_code == http.HTTPStatus.OK:
        print(f'Connection to API successful')
        return response.json()
    if response.status_code == http.HTTPStatus.NOT_FOUND:
        raise Exception(f'City not found. Please check city name : {city}.')
    else:
        raise Exception(f'Service error for city : {city} response:{response}')


def get_time_in_readable_format(input_time):
    # Convert UTC time to YYYY-MM-DD HH:MM:SS format
    return datetime.datetime.fromtimestamp(int(input_time)).strftime('%Y-%m-%d %H:%M:%S')


def process_weather(received_response):
    # Create weather data object
    weather_data = Weather(
        get_time_in_readable_format(received_response["dt"]),
        received_response["main"]["temp"],
        received_response["main"]["feels_like"],
        received_response["weather"][0]["main"],
        received_response["main"]["temp_min"],
        received_response["main"]["temp_max"],
        received_response["main"]["humidity"],
        received_response["wind"]["speed"],
        get_time_in_readable_format(received_response["sys"]["sunrise"]),
        get_time_in_readable_format(received_response["sys"]["sunset"])
    )

    # Print weather received.
    weather_data.print_weather()


def main():
    print(f'Welcome to weather app.\n'
          f'Allowed city format - \n'
          f'Omaha\n'
          f'Omaha, USA\n'
          f'Omaha, NE, USA\n')
    while True:
        city = list(map(str, input("Please enter city or q/Q to Quit:").split(',')))
        print(city)
        try:
            if len(city) == 1 and str(city[0]).upper() == "Q":
                break
            elif len(city) > 3 or (len(city) == 1 and city[0] == ""):
                raise Exception(f'City name entered is not in correct format: {city}')
            else:
                print(f'Requesting Weather data...')

                cleaned_city = []
                for item in city:
                    # Check if city name has alpha and city name is greater than 1 character.
                    # It is assumed that city name should be at least 2 character.
                    if str(item).strip().isalpha() and len(str(item).strip()) > 1:
                        cleaned_city.append(str(item).strip())
                    else:
                        raise Exception(f'City name entered is not in correct format: {city}')
                print(cleaned_city)
                # Request weather data from weather API
                received_response = get_weather_data(cleaned_city)
                if len(received_response) > 0:
                    process_weather(received_response)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
