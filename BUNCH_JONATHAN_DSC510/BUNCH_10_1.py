# File: BUNCH_10_1.py
# Name: Jonathan Bunch
# Date: 17 May, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)


# Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
# The program will receive a JSON response which includes various pieces of data. You should parse the JSON data to
# obtain the “value” key. The data associated with the value key should be displayed for the user (i.e., the joke).
# Your program should allow the user to request a Chuck Norris joke as many times as they would like. You should make
# sure that your program does error checking at this point. If you ask the user to enter “Y” and they enter y, is that
# ok? Does it fail? If it fails, display a message for the user. There are other ways to handle this. Think about
# included string functions you might be able to call.
# Your program must include a header as in previous weeks.
# Your program must include a welcome message for the user.
# Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no
# context does not represent “pretty.”


import requests


# This function asks the user to enter "y" to continue or "n" to exit. Entry can be lower case or capitalized.
# Any other entry will return a different message, but continue to retrieve and display the joke.
def ask_user():
    user_response = input('Enter y for yes or n for no:')
    if user_response == 'y' or user_response == 'Y':
        print('Good answer! Fetching joke from the internet...\n')
        user_response = True
    elif user_response == 'n' or user_response == 'N':
        print('Chuck Norris would be so disappointed in you.')
        user_response = False
    else:
        print('You did not enter a valid response. Therefore we will assume you meant yes.')
        print('Fetching joke from the internet...\n')
        user_response = True
    return user_response


# This function tries to connect to the api. If successful the joke will be retrieved and printed for the user.
# If the request fails, the user will be given an error message and given the option to try again or exit.
def fetch_joke():
    url = 'https://api.chucknorris.io/jokes/random'
    try:
        joke_response = requests.get(url, timeout=2)
        joke_response.raise_for_status()
    except requests.exceptions.RequestException:
        print('Unfortunately there seems to be a problem with the connection.')
        print('We sincerely apologize for depriving you of Chuck Norris jokes.')
        print('Would you like try again?')
        retry = ask_user()
        if retry:
            fetch_joke()
    else:
        joke_json = joke_response.json()
        print(joke_json['value'], '\n')
        print('Hope you enjoyed your Chuck Norris joke! Would you like to hear another?')
        another = ask_user()
        if another:
            fetch_joke()


# Main function that welcomes the user and calls the other functions.
def main():
    print('Welcome! Would you like to hear a Chuck Norris joke?')
    run_program = ask_user()
    if run_program:
        fetch_joke()


main()
