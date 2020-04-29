"""
File: assignment8_1.py
Author: Bhushan Suryawanshi
Date:Wednesday, April 29, 2020
Course: DSC510-T303 Introduction to Programming (2205-1)

Desc: The program will do followings: We will create a program which performs three essential
operations. It will process this .txt file: Gettysburg.txt. (Click the link to download the text file).  Calculate
the total words, and output the number of occurrences of each word in the file.

Open the file and process each line.
Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1. Nicely print the output,
in this case from high to low frequency. You should use string formatting for this. (See discussion 8.3).
We want to achieve each major goal with a function (one function, one action). We can find four functions that
need to be created.

add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.

Process_line: There is some work to be done to process the line: strip off various characters, split out the words,
and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word. No
return value.

Pretty_print: Because formatted printing can be messy and often particular to each situation (meaning that we might
need to modify it later), we separated out the printing function. The parameter is a dictionary. No return value.

main: We will use a main function as the main program. As usual, it will open the file and call process_line on each
line. When finished, it will call pretty_print to print the dictionary.

"""
import collections
import re


def add_word(word, word_dict):
    # Add the word to the dictionary and increase count
    if word not in word_dict:
        word_dict[word] = 0
    word_dict[word] += 1


def process_line(line, word_dict):
    line = re.sub('\W+', ' ', line)
    # Lower case each word in the line.
    words = [word.lower() for word in line.split()]

    # Call add word for each word in list of words.
    for word in words:
        add_word(word, word_dict)


def pretty_print(word_dict):
    print("word                count")
    print("-" * 26)

    # Reverse the dictionary and arrange the words in descending order.
    inv_map = collections.defaultdict(list)
    for k, v in word_dict.items():
        inv_map[v].append(k)
        inv_map[v].sort(reverse=True)

    # Sort list of tuple by count in descending order.
    word_tuple = sorted(inv_map.items(), reverse=True)

    # Get the each item from the word_tuple and format it in tabular structure.
    for item in word_tuple:
        count = item[0]
        for word in item[1]:
            print(word + " " * (20 - len(word)) + str(count))


def main():
    word_dict = dict()

    # Open data file in read mode.
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_dict)

    print("Length of Dictionary: {}".format(len(word_dict.keys())))

    # Print formatted output.
    pretty_print(word_dict)


if __name__ == '__main__':
    main()
