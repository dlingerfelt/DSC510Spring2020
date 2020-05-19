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

# installed the requests library
import requests
import json

# function to receive a json response and parse json
def service_joke():
    serviceurl = 'https://api.chucknorris.io/jokes/random'
    try:
        joke = requests.get(serviceurl).json()
    except Exception as fail:
        raise Exception(f'==== Fail to Retrieve ===={fail}')
    return joke

# created a pretty print function so only the value is displayed for user
def pretty(joke):
    print('--------This is your joke----------')
    print(joke['value'])
    
# created an error checking function so if user enters various forms of Yes
# the joke will display and forms of No will exit program
# anything that isn't Y/N will be an invalid user response
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
    # Display Welcome message for user
    print('Welcome to the World that is Chuck Norris!')
    # the while loop allows user to request as many jokes as they want
    while True:
        (user_inp())
        pretty(service_joke())


main()
