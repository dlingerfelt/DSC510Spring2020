# File: Assignment_10_1.py
# Name: Roni Kaakaty
# Date: 05/17/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# This program will do the following:
# Create a program which uses the Request library to make a GET request of the Chuck Norris API.
# Parse JSON data to obtain the "value" key.
# User should be able to request as many jokes as they like. Include error checking. Display error message.
# Include welcome message.
# Display "pretty" output.

import requests
import json

def norris_joke():  # Function to request the joke from the API.
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.request("GET", url)
    line = (response.text)
    output = json.loads(line) # Parse JSON

    print("{}\n".format(output['value'])) # Formats the output.

def main():  # Main function
    print(f'{"-" * 42}')
    print("Welcome to the Chuck Norris Joke Generator")
    print(f'{"-" * 42}')

    while True:
        try:
            option = str(input("Would you like to hear a joke?\nEnter Y for yes, N for no:")) # Requests user input
        except ValueError:
            print("Invalid input, try again") # Returns error if valid input not received.
        if option.upper()=="Y":  # Allows Y and y for formatting purposes.

            norris_joke()
        else:
            if option.upper()=="N": # Allows N and n for formatting purposes.
                print(f'{"-" * 23}')
                print("Thanks for stopping by!")
                print(f'{"-" * 23}')
                break  # Ends the loop.
            else:
                print("Invalid input, try again")

main()  # Begins program
