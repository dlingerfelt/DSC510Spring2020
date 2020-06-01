# File: BUNCH_FINAL_PROJECT.py
# Name: Jonathan Bunch
# Date: 31 May, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# Thank you for your feedback on all of the assignments. I really enjoyed the course!

import requests
import json


# This function prompts the user for a zip code or city and checks that the input matches the expected format.
def get_user_location():
    entry_error_zip = 'Error: zip code must consist of five numerical digits with no letters or symbols.'
    entry_error_name = 'Error: please enter city, state, and country in the following format: city,state,country'
    location_u = 0
    while location_u == 0:
        location_u = input('Please enter a five digit zip code OR city, state, and country (separated by commas) OR '
                           'enter x to exit:')
        if location_u.lower() == 'x':
            return False
        elif location_u.isdigit():
            if len(location_u) != 5:
                print(entry_error_zip)
                location_u = 0
                continue
        else:
            location_split = location_u.split(',')
            if len(location_split) != 3:
                print(entry_error_name)
                location_u = 0
                continue
            else:
                user_city = location_split[0].strip()
                user_state = location_split[1].strip()
                user_country = location_split[2].strip()
                if not user_city.isalpha() or not user_state.isalpha() or not user_country.isalpha():
                    location_u = 0
                    print(entry_error_name)
                    continue
                location_u = user_city.lower() + ',' + user_state.lower() + ',' + user_country.lower()
    return location_u


# This function sends the HTTP request and handles any connection errors that may come up.  It returns a dictionary
# containing the full contents of the JSON file returned by the API call.
def send_request(user_location):
    print('Attempting to connect to API...')
    url_base = 'http://api.openweathermap.org/data/2.5/forecast'
    url_params = {'units': 'imperial', 'appid': 'f96b1a65310dc1228658c8853a71fe67'}
    if user_location.isdigit():
        url_params.update({'zip': user_location})
    else:
        url_params.update({'q': user_location})
    try:
        weather_request = requests.get(url_base, params=url_params, timeout=3)
        weather_request.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Unfortunately there was an error with your request (error type: HTTP Error). Please try again.")
    except requests.exceptions.ConnectionError:
        print("Unfortunately there was an error with your request (error type: Connection Error). Please try again.")
    except requests.exceptions.Timeout:
        print("Unfortunately there was an error with your request (error type: Timeout Error). Please try again.")
    except requests.exceptions.RequestException:
        print("Unfortunately there was an error with your request (error type: Other). Please try again.")
    else:
        weather_json = weather_request.json()
        if weather_json is None:
            return 0
        else:
            print('API connection successful! Retrieving forecast...')
            return weather_json


# This function pulls saved test data from a file. I used this function to test my code without making an excessive
# number of API calls.
def test_data():
    json_data = open('forecast2.txt', 'r')
    weather_raw = json_data.read()
    wj = json.loads(weather_raw)
    return wj


# This function collects the weather data I chose to include from the json file and adds it to a new dictionary.
# The datetime is used for the keys, with the values being dictionaries of weather conditions for that datetime.
def collect_json_data(weather_json):
    data_dict = {}
    data_point = 0
    data_dict.update({'city': weather_json['city']['name']})
    data_dict.update({'country': weather_json['city']['country']})
    for data in weather_json['list']:
        data_dict.update({weather_json['list'][data_point]['dt_txt']: {
            'temp': weather_json['list'][data_point]['main']['temp'],
            'feels_like': weather_json['list'][data_point]['main']['feels_like'],
            'humidity': weather_json['list'][data_point]['main']['humidity'],
            'conditions': weather_json['list'][data_point]['weather'][0]['description']
        }})
        data_point = data_point + 1
    return data_dict


# Since there is too much data to comfortably display to the user, I chose to display the forecast for three
# time frames per day: morning, noon, and evening. This function organizes the data into lists of values for each time
# frame. Depending on the time of the request some values may not be available, so "N/A" is inserted in those places.
def organize_data(data_in):
    date_list = []
    data_org_by_time = {
        'city': data_in['city'],
        'country': data_in['country'],
        'dates': [],
        'am': {'temp': [], 'feels_like': [], 'humidity': [], 'conditions': []},
        'noon': {'temp': [], 'feels_like': [], 'humidity': [], 'conditions': []},
        'pm': {'temp': [], 'feels_like': [], 'humidity': [], 'conditions': []}
    }
    for key in data_in:
        if key == "city" or key == "country":
            continue
        elif key[0:10] not in date_list:
            date_list.append(key[0:10])
    data_org_by_time['dates'].extend(date_list)
    for date in date_list:
        am_date = (date + " 06:00:00")
        noon_date = (date + " 12:00:00")
        pm_date = (date + " 18:00:00")
        if am_date in data_in:
            data_org_by_time['am']['temp'].append(f"{data_in[am_date]['temp']:.1f} F")
            data_org_by_time['am']['feels_like'].append(f"{data_in[am_date]['feels_like']:.1f} F")
            data_org_by_time['am']['humidity'].append(f"{data_in[am_date]['humidity']:.1f} %")
            data_org_by_time['am']['conditions'].append(data_in[am_date]['conditions'])
        else:
            data_org_by_time['am']['temp'].append('N/A')
            data_org_by_time['am']['feels_like'].append('N/A')
            data_org_by_time['am']['humidity'].append('N/A')
            data_org_by_time['am']['conditions'].append('N/A')
        if noon_date in data_in:
            data_org_by_time['noon']['temp'].append(f"{data_in[noon_date]['temp']:.1f} F")
            data_org_by_time['noon']['feels_like'].append(f"{data_in[noon_date]['feels_like']:.1f} F")
            data_org_by_time['noon']['humidity'].append(f"{data_in[noon_date]['humidity']:.1f} %")
            data_org_by_time['noon']['conditions'].append(data_in[noon_date]['conditions'])
        else:
            data_org_by_time['noon']['temp'].append('N/A')
            data_org_by_time['noon']['feels_like'].append('N/A')
            data_org_by_time['noon']['humidity'].append('N/A')
            data_org_by_time['noon']['conditions'].append('N/A')
        if pm_date in data_in:
            data_org_by_time['pm']['temp'].append(f"{data_in[pm_date]['temp']:.1f} F")
            data_org_by_time['pm']['feels_like'].append(f"{data_in[pm_date]['feels_like']:.1f} F")
            data_org_by_time['pm']['humidity'].append(f"{data_in[pm_date]['humidity']:.1f} %")
            data_org_by_time['pm']['conditions'].append(data_in[pm_date]['conditions'])
        else:
            data_org_by_time['pm']['temp'].append('N/A')
            data_org_by_time['pm']['feels_like'].append('N/A')
            data_org_by_time['pm']['humidity'].append('N/A')
            data_org_by_time['pm']['conditions'].append('N/A')
    return data_org_by_time


# This function prints the data in a format that is (hopefully) easy for the user to read and understand.
def print_weather(org_data_in):
    print('')
    welcome_results = f'''{'Weather forecast for ':>85}{org_data_in["city"]}, {org_data_in["country"]}'''
    print(welcome_results)
    header_length = (len(org_data_in['city']) + 23 + len(org_data_in['country']))
    print(f'  {"-" * header_length:>{len(welcome_results) - 2}}')
    i = 0
    indent = 31
    print(f'{"Date:"}', end='')
    for dates in org_data_in['dates']:
        date = f'{org_data_in["dates"][i]:>{indent}}'
        print(date, end='')
        i = i + 1
        indent = 25
    print('\n')
    # Morning
    morning_header = f'{"Morning":>25}'
    print(f'{"Morning":>36}' + (morning_header * ((len(org_data_in['dates'])) - 1)))
    i = 0
    indent = 20
    print(f'{"Temperature (F):"}', end='')
    for temps in org_data_in['am']['temp']:
        am_temp = f'{org_data_in["am"]["temp"][i]:>{indent}}'
        print(am_temp, end='')
        i = i + 1
        indent = 25
    i = 0
    indent = 21
    print('')
    print(f'{"Feels Like (F):"}', end='')
    for feels in org_data_in['am']['feels_like']:
        am_feel = f'{org_data_in["am"]["feels_like"][i]:>{indent}}'
        print(am_feel, end='')
        i = i + 1
        indent = 25
    i = 0
    indent = 23
    print('')
    print(f'{"Humidity (%):"}', end='')
    for hum in org_data_in['am']['humidity']:
        am_hum = f'{org_data_in["am"]["humidity"][i]:>{indent}}'
        print(am_hum, end='')
        i = i + 1
        indent = 25
    i = 0
    indent = 25
    print('')
    print(f'{"Conditions:"}', end='')
    for cond in org_data_in['am']['conditions']:
        am_cond = f'{org_data_in["am"]["conditions"][i]:>{indent}}'
        print(am_cond, end='')
        i = i + 1
        indent = 25
    print('\n')
    # Afternoon
    mid_header = f'{"Mid Day":>25}'
    print(f'{"Mid Day":>36}' + (mid_header * ((len(org_data_in['dates'])) - 1)))
    i = 0
    indent = 20
    print(f'{"Temperature (F):"}', end='')
    for temp in org_data_in['noon']['temp']:
        temps = f'{org_data_in["noon"]["temp"][i]:>{indent}}'
        print(temps, end='')
        i = i + 1
        indent = 25
    i = 0
    indent = 21
    print('')
    print(f'{"Feels Like (F):"}', end='')
    for feels in org_data_in['noon']['feels_like']:
        feel = f'{org_data_in["noon"]["feels_like"][i]:>{indent}}'
        print(feel, end='')
        i = i + 1
        indent = 25
    i = 0
    indent = 23
    print('')
    print(f'{"Humidity (%):"}', end='')
    for hum in org_data_in['noon']['humidity']:
        hum = f'{org_data_in["noon"]["humidity"][i]:>{indent}}'
        print(hum, end='')
        i = i + 1
        indent = 25
    i = 0
    indent = 25
    print('')
    print(f'{"Conditions:"}', end='')
    for cond in org_data_in['noon']['conditions']:
        conditions = f'{org_data_in["noon"]["conditions"][i]:>{indent}}'
        print(conditions, end='')
        i = i + 1
        indent = 25
    print('\n')
    # Evening
    evening_header = f'{"Evening":>25}'
    print(f'{"Evening":>36}' + (evening_header * ((len(org_data_in['dates'])) - 1)))
    i = 0
    indent = 20
    print(f'{"Temperature (F):"}', end='')
    for temp in org_data_in['pm']['temp']:
        temps = f'{org_data_in["pm"]["temp"][i]:>{indent}}'
        print(temps, end='')
        i = i + 1
        indent = 25
    i = 0
    indent = 21
    print('')
    print(f'{"Feels Like (F):"}', end='')
    for feels in org_data_in['pm']['feels_like']:
        feel = f'{org_data_in["pm"]["feels_like"][i]:>{indent}}'
        print(feel, end='')
        i = i + 1
        indent = 25
    i = 0
    indent = 23
    print('')
    print(f'{"Humidity (%):"}', end='')
    for hum in org_data_in['pm']['humidity']:
        hum = f'{org_data_in["pm"]["humidity"][i]:>{indent}}'
        print(hum, end='')
        i = i + 1
        indent = 25
    i = 0
    indent = 25
    print('')
    print(f'{"Conditions:"}', end='')
    for cond in org_data_in['pm']['conditions']:
        conditions = f'{org_data_in["pm"]["conditions"][i]:>{indent}}'
        print(conditions, end='')
        i = i + 1
        indent = 25
    print('\n')
    print('Thanks for using our weather forecast application! Would you like to retrieve another forecast?')


# This is the main function that will welcome the user, call the other functions, and print an exit message when the
# user chooses to exit the application.
def main():
    print('Welcome to our weather forecasting application! Enter your location for a 5 day forecast!')
    print('Note: depending on the time of the request, some values may not be available.')
    run_loop = True
    while run_loop:
        user_location = get_user_location()
        if user_location == 0:
            run_loop = False
            break
        else:
            raw_json_data = send_request(user_location)
        if raw_json_data is None:
            continue
        else:
            weather_data = collect_json_data(raw_json_data)
            org_data = organize_data(weather_data)
            print_weather(org_data)
    print('Thanks for using our weather forecast application!')


main()
