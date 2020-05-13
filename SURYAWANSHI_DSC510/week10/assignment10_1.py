"""
File: assignment10_1.py
Author: Bhushan Suryawanshi
Date:Wednesday, May 12, 2020
Course: DSC510-T303 Introduction to Programming (2205-1)

Desc: The program will allow user to read Chuck Norris jokes till user hit exit option.
request_joke function will request the joke to the external Joke API.
display_joke function will format the API response received. Parameter to function will be response from API.

"""
import requests
from datetime import date


def request_joke():
    joke_api = "https://api.chucknorris.io/jokes/random"

    try:
        # Request the joke from API.
        json_data = requests.get(joke_api).json()
    except Exception as e:
        raise Exception(f"Error accessing Joke API:{e}")

    return json_data


def display_joke(joke):
    today = date.today().strftime("%m/%d/%y")

    # Format the response.
    print(f'{"-" * 50} \nThis is Chuck Norris\'s Joke World. \n{"-" * 50}\nTime:{today}')
    print(f'Joke Categories:{joke["categories"]}\nJoke:')

    # Split the joke into words.
    list_of_words = str(joke['value']).split()
    char_to_str = ""

    # Print words to format each line for 50 characters.
    for word in list_of_words:
        char_to_str = f'{char_to_str} {word}'
        if len(char_to_str) >= 50:
            print(char_to_str)
            char_to_str = ""
    print(char_to_str)
    print("-" * 50)


def main():
    print(f" Welcome to Joke Application.")
    while True:
        print(f" To Continue Press Y/y.\n"
              " To Exit. Press N/n.\n")
        option = input("Enter your option : ").upper()
        if option == "Y":
            try:
                # Request joke and display the response.
                display_joke(request_joke())
            except Exception as e:
                print(f"API_Exception:{e}")
        elif option == "N":
            break
        else:
            print(f"Wrong Input.")


if __name__ == '__main__':
    main()
