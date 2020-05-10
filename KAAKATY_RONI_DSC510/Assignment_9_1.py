# File: Assignment_9_1.py
# Name: Roni Kaakaty
# Date: 05/09/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# This program will do the following:
# Open text file and process each line.
# Either add each word to the dictionary with a frequency of 1 or update the word's count by 1.
# Nicely print the output, from high to low frequency.
# Create a new function named process_file that will print to a file instead of a screen.
# Modify main method to print to file and not to screen.
# Gather user input for file name.
# Write to the file.

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

def process_file (dictionary, txt_output):  # function that will print the code in a readable format and sorts it based on frequency.
    sort_tuple = list(dictionary.items())
    sort_tuple.sort(key=lambda x: x[1], reverse=True)  # sorting format in max frequency order.
    length = len(dictionary)  # Counts the values in the dictionary.
    output_file = open(txt_output, 'w')  # opens .txt file to write to it.
    output_file.write('The length of the dictionary: {}\n'.format(length))  # writes the length, word count in proper format.
    output_file.write('Word           Count\n')
    output_file.write('--------------------\n')
    for key, value in sort_tuple:
        output_file.write('{:12}    {:4}\n'.format(key, value))  # places the values in proper format.

def main():  # main function that opens the file to begin the program.
    gba_file = open('gettysburg.txt', 'r')  # open gettysburg.txt in readable format.
    counts = dict()
    txt_name = input('What would you like your filename to be?')  # captures user input for desired file name.
    if '.txt' not in txt_name:
        txt_output = txt_name + '.txt'  # Adds .txt extension if not provided by user.
    else:
        txt_output = txt_name  # if .txt is provided by user, no need to add it.
    for line in gba_file:  # processes process_line function for each line in file.
        process_line(line, counts)
    process_file(counts, txt_output)

main()