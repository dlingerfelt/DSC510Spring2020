#Algoritham to create a program which performs three essential operations
#Open the file and process each line.
#Either add each word to the dictionary with a frequency of 1 or update the word’s count by 1.
#Nicely print the output, in this case from high to low frequency.
#DSC510-T303 Introduction to Programming (2205-1)
#Created by Rajkumar Kuppuswami
#Created on 05/01/2020
#Program to perform processing the line by adding each word to the dictionary.
#Once values are added need to format as list to sort the values by desc.

import collections

def main():
    dictionary = dict()
#1st method to open the file
# with open('Gettysburg.txt', 'r') as file_read:
# Read the text file
    file_read = open('Gettysburg.txt', 'r')
# Process word one by one
    for line in file_read:
        process_line(line, dictionary)
    print("Length of Dictionary is : {}".format(len(dictionary.keys())))#Total Lenght of the dictionary

    print(pretty_print(dictionary))#Output of each word with count


def add_word(word, word_count):#Adding the words to the dictionary with count of words
    if word in word_count: #To validate the words to avoid duplicate
            word_count[word] = word_count[word]+1 #counting the number of words
    else:
            word_count[word] =1

def process_line (line, dictionary):
    line = line.lower() ##convert to lower case
    line = line.strip()# remove /n line and unwanted space
    words = line.split(" ")#Split the words from the text by line
    for word in words:
        add_word(word, dictionary)


def pretty_print(dictionary):
    table = collections.defaultdict(list)
    for a , b in dictionary.items():
        table[b].append(a)
    sort_table = sorted(table.items(), reverse=True) # Sort list of tuple by count in descending order.
    for item in sort_table:
        count = item[0]
        for word in item[1]:
            print(word + " " * (30 - len(word)) + str(count))

main()


