# File: Assignment_10.1
# Name: Hanh Tran
# Due Date: 5/17/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)
# Desc: This program will do the following:
# Uses the requests library to make a GET request of the following API: https://api.chucknorris.io/jokes/random
# Receive a JSON response which includes various pieces of data
# Parse JSON data to obtain the value key
# Display to user the Data associated with value key
# Allow user to request as many Chuck Norris jokes as they want


import requests
import json

def service_joke():
    serviceurl = 'https://api.chucknorris.io/jokes/random'
    try:
        joke = requests.get(serviceurl).json()
    except Exception as fail:
        raise Exception(f'==== Fail to Retrieve ===={fail}')
    return joke

def pretty(joke):
    print('--------This is your joke----------')
    print(joke['value'])

def user_inp():
    user = input('Are you ready for a Chuck Norris joke? Yes or No:\n')
    if user == 'Yes' or user == 'Y' or user == 'y':
        print('Retrieving Joke...\n')
        user = service_joke()
    elif user == 'No' or user == 'N' or user == 'n':
        print('You have exited')
        exit()
    else:
        print('==== Invalid Response: Failure to Retrieve ====')
        exit()
def main():
    print('Welcome to the World that is Chuck Norris!')
    while True:
        (user_inp())
        pretty(service_joke())


main()
