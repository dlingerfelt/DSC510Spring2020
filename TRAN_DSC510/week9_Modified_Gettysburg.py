# File: Assignment_9.1
# Name: Hanh Tran
# Due Date: 5/10/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)
# Desc: This program will do the following:
# Process a user file. calculate the total words and output the number of occurances of each word in the file.
# sort the output from highest to lowest frequency of words.
# Create a new function called process_file that prints to a file instead of to the screen.
# Modify main method to print the length of the dictionary to the file as opposed to the screen.
# Prompt the user for the filename they wish to use to generate the report.
# Use the filename specified by the user to write the file.


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

# created new function, process_file to print to file instead of screen
def process_file(getty_dict, fname):
    lst = list() # create a list from text to be formatted
    for key, val in list(getty_dict.items()): # format list
        lst.append((val, key))
    lst.sort(reverse=True) # sort list from highest frequency of words to lowest
    outfile = open(fname, 'w') # opens the user-provided text file to write to it
    outfile.write('Length of the dictionary: {}\n'.format(len(getty_dict.keys()))) # write content to file
    outfile.write('Count Word\n') # write content to file
    outfile.write('----------\n') # write content to file
    for key, val in lst[:]:
        outfile.write('{:2}    {:2}\n'.format(key, val)) # write content to file

# main function to open file and call process_line.
fname = input('Enter the file name: ')
def main():
    # Used try/except block to display error if user enters something that is not a file name
    try:
        fhand = open(fname)
    except:
        print('File cannot be found: ', fname)
        exit()
    getty_dict = dict()
    with open(fname, 'r') as gba_file:
        for line in gba_file:
            process_line(line, getty_dict)
    process_file(getty_dict, fname) #call process_file to print dictionary to file

main()