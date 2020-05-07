"""
File: assignment9_1.py
Author: Bhushan Suryawanshi
Date:Wednesday, May 06, 2020
Course: DSC510-T303 Introduction to Programming (2205-1)

Desc: The program will do followings: We will create a program which performs three essential
operations. It will process file: Gettysburg.txt.
Calculate the total words, and create report for the number of occurrences of each word in the file.

add_word: Add each word to the dictionary. Parameters are the word and a dictionary. No return value.

process_line: process the line: strip off various characters, split out the words,
and so on. Parameters are a line and the dictionary. It calls the function add word with each processed word. No
return value.

process_file: This function takes a dictionary and file name as parameter. Write the report to file.

main:  A main function as the main program. Request user with file name for report file. It will open the file and
call process_line on each line. When finished, it will call process_file to write the dictionary to a file.

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


def process_file(word_dict, filename):
    dash = "-" * 26
    write_to_file(f"word                count\n{dash}", filename, "a")

    # Reverse the dictionary and arrange the words in descending order.
    inv_map = collections.defaultdict(list)
    for k, v in word_dict.items():
        inv_map[v].append(k)
        inv_map[v].sort(reverse=True)

    # Sort list of tuple by count in descending order.
    word_tuple = sorted(inv_map.items(), reverse=True)

    # Get the each item from the word_tuple and format it in tabular structure.
    data = []
    for item in word_tuple:
        count = item[0]
        for word in item[1]:
            data.append(word + " " * (20 - len(word)) + str(count))

    # Write final dictionary to file.
    for data_item in data:
        write_to_file(data_item, filename, "a")


def write_to_file(string_to_write, filename, file_mode):
    with open(f"{filename}.txt", file_mode) as file:
        file.write(string_to_write)
        file.write("\n")


def main():
    filename = input("Enter file name for report (without extension):")

    try:
        with open(f"{filename}.txt", "w") as file:
            pass
    except OSError as error:
        print(f"Wrong file name.{error}")
        exit()

    word_dict = dict()

    # Open data file in read mode.
    gba_file = open('gettysburg.txt', 'r')
    for line in gba_file:
        process_line(line, word_dict)

    write_to_file(f"Length of Dictionary: {len(word_dict.keys())}", filename, "w")

    # Process file content.
    process_file(word_dict, filename)


if __name__ == '__main__':
    main()
