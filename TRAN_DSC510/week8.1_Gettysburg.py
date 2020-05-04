# File: Assignment_8.1
# Name: Hanh Tran
# Due Date: 5/3/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)
# Desc: This program will do the following:
# Open the file and process each line.
# Add each word to the dictionary by updating the word’s count by 1.
# Output the number of occurrences of each word in the file.
# Nicely print the output, in this case from high to low frequency.

import string # used to clean text

# function to add each word to the dictionary, parameters are word and dictionary.
def add_word(word, getty_dict):
    if word not in getty_dict:
        getty_dict[word] = 1
    else:
        getty_dict[word] += 1
# function to process the line. strip off punctuation, split out words. Parameters are line and dictionary.
def process_line(line, getty_dict):
    line = line.rstrip()
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        add_word(word, getty_dict) # calls the function add_word

# function to format word frequency from high to low. Sort the dictionary by value.
def pretty_print(getty_dict):
    print('Length of the dictionary: {}'.format(len(getty_dict.keys())))
    print('Count Word')
    print('-'*10)
    lst = list()
    for key, val in list(getty_dict.items()):
        lst.append((val, key))
    lst.sort(reverse=True)
    for key, val in lst[:]:
        print(key, val)

# main function to open file and call process_line.
def main():
    getty_dict = dict()
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, getty_dict)
    print(pretty_print(getty_dict)) #call pretty_print to print dictionary

print(main())
