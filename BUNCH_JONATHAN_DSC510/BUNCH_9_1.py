# File: BUNCH_9_1.py
# Name: Jonathan Bunch
# Date: 9 May, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)


# For this week we will modify our Gettysburg processing program from week 8 in order to generate a text file from the
# output rather than printing to the screen. Your program should have a new function called process_file which prints
# to the file (this method should almost be the same as the pretty_print function from last week. Keep in mind that we
# have print statements in main as well. Your program must modify the print statements from main as well.
# Create a new function called process_fie. This function will perform the same operations as pretty_print from week 8
# however it will print to a file instead of to the screen.
# Modify your main method to print the length of the dictionary to the file as opposed to the screen.
# This will require that you open the file twice. Once in main and once in process_file.
# Prompt the user for the filename they wish to use to generate the report.
# Use the filename specified by the user to write the file.
# This will require you to pass the file as an additional parameter to your new process_file function.


# This function handles the request to the user for a new file name. The entry is restricted to alphanumeric characters
# for convenience, and the user will be prompted to correct any entry containing other characters.
def get_file_name():
    entry_error = 'Please enter a valid file name. Punctuation and special characters are not accepted.'
    file_name = 0
    while file_name == 0:
        file_name = input('Please enter a name for the output file using alphanumeric characters only:')
        if not file_name.isalnum():
            print(entry_error)
            file_name = 0
            continue
    file_name = str(file_name) + '.txt'
    return file_name


# This function formats the output for easier viewing and writes it to the file.
def process_file(dictionary, user_file_name):
    spacer = '                      '
    line_sep = '-------------------------------'
    nl = '\n'
    dict_length = len(dictionary)
    output1 = 'Total length of dictionary: {}'.format(dict_length) + nl
    output2 = 'Word' + spacer + 'Count' + nl
    count_list = list(dictionary.items())
    count_list.sort(key=lambda x: x[1], reverse=True)
    with open(user_file_name, 'w') as output_file:
        output_file.write(line_sep + nl)
        output_file.write(output1)
        output_file.write(output2)
        output_file.write(line_sep + nl)
        for word, count in count_list:
            output_file.write('{:23}    {:4}'.format(word, count) + nl)


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
    clean_list = []
    for word_raw in line_list:
        word_cleaned = word_raw.strip('., -""')
        clean_list.append(word_cleaned)
    fin_list = list(filter(None, clean_list))
    for word in fin_list:
        add_word(word, dictionary_line)


# Main function that will open the read file, then call our functions to process and print the data.
def main():
    word_count = {}
    with open('gettysburg.txt', 'r') as gba_file:
        for line in gba_file:
            process_line(line, word_count)
    fin_file_name = get_file_name()
    process_file(word_count, fin_file_name)


main()
