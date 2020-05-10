# File: BUNCH_8_1.py
# Name: Jonathan Bunch
# Date: 3 May, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# We will create a program which performs three essential operations. It will process this .txt file: Gettysburg.txt.
# Calculate the total words, and output the number of occurrences of each word in the file.
#
# Open the file and process each line.
# Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
# Nicely print the output, in this case from high to low frequency. You should use string formatting for this.
# (See discussion 8.3).
# We want to achieve each major goal with a function (one function, one action).
# We can find four functions that need to be created.
#
# add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.
#
# Process_line: There is some work to be done to process the line: strip off various characters, split out the words,
# and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word.
# No return value.
#
# Pretty_print: Because formatted printing can be messy and often particular to each situation
# (meaning that we might need to modify it later), we separated out the printing function.
# The parameter is a dictionary. No return value.
#
# main: We will use a main function as the main program. As usual, it will open the file and call process_line
# on each line. When finished, it will call pretty_print to print the dictionary.
#
# In the main function, you will need to open the file. We will cover more regarding opening of files next week
# but I wanted to provide you with the block of code you will utilize to open the file, see below.


# Checks if each word is in the dictionary.  Adds the word to the dictionary or increases the associated value by 1.
def add_word(word, dictionary_word):
    if word in dictionary_word:
        n = int(dictionary_word[word] + 1)
        dictionary_word.update({word: n})
    else:
        dictionary_word.update({word: 1})


# Takes the line and breaks it into a list, using a space as the separator. Strips off extra spaces and punctuation.
# Runs the add_word() function for each cleaned up word.
def process_line(line_in, dictionary_line):
    line_lower = line_in.lower()
    line_list = line_lower.split()
    for word in line_list:
        if word == '--':
            indx = line_list.index(word)
            line_list.pop(indx)
            continue
        word_cleaned = word.strip('., -""')
        add_word(word_cleaned, dictionary_line)


# This function sorts, formats, and prints the word count dictionary.
def pretty_print(dictionary):
    spacer = '                      '
    line_sep = '-------------------------------'
    dict_length = len(dictionary)
    output1 = 'Total length of dictionary: {}'.format(dict_length)
    print(line_sep)
    print(output1)
    output2 = 'Word' + spacer + 'Count'
    print(output2)
    print(line_sep)
    count_list = list(dictionary.items())
    count_list.sort(key=lambda x: x[1], reverse=True)
    for word, count in count_list:
        print('{:23}    {:4}'.format(word, count))


# Main function that will open the file, then call our functions to process and print the data.
def main():
    word_count = {}
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_count)
    pretty_print(word_count)


main()
