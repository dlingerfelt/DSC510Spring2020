# File: Assignment_8_1.py
# Name: Roni Kaakaty
# Date: 05/03/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# This program will do the following:
# Open text file and process each line.
# Either add each word to the dictionary with a frequency of 1 or update the word's count by 1.
# Nicely print the output, from high to low frequency.

import string  # Needed to perform string.punctuation later

def add_word (words, dictionary): # function used to add words to dictionary and calculate word count
        for word in words:
            if word not in dictionary:
                dictionary[word] = 1  # If first instance of word, input a value of 1.
            else:
                dictionary[word] += 1 # If multiple instances of words, add 1 each time.


def process_line (line, dictionary):  # function used to format the strings to eliminate punctuation errors.
    line = line.translate(str.maketrans('', '', string.punctuation))  # removes punctuation
    line = line.lower()  # converts to lowercase
    words = line.split()  # splits the words out
    add_word(words, dictionary)


def pretty_print (dictionary):  # function that will print the code in a readable format and sorts it based on frequency.
    sort_tuple = list(dictionary.items())
    sort_tuple.sort(key=lambda x: x[1], reverse=True)  # sorting format in max frequency order.
    print("Length of the dictionary: ", len(dictionary))  # displays total number of words
    print('Word           Count')
    print('--------------------')
    for key, value in sort_tuple:
        print('{:12}    {:4}'.format(key, value))  # dictates the spaces in between the key and value.



def main ():  # main function that will activate the program and retrieve the text file.
    gba_file = open('gettysburg.txt', 'r')
    counts = dict()
    for line in gba_file:
        process_line(line, counts)
    pretty_print(counts)

main()
