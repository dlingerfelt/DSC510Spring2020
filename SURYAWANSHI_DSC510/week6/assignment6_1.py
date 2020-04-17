"""
File: assignment6_1.py
Author: Bhushan Suryawanshi
Date:Wednesday, April 13, 2020
Course: DSC510-T303 Introduction to Programming (2205-1)
Desc: The program will do followings:
Allow the user to input a series of temperatures along with a sentinel value which will stop the user input.
Evaluate the temperature list to determine the largest and smallest temperature.
Print the largest temperature and the smallest temperature.
A message tells the user how many temperatures are in the list.
"""


def main():
    list_of_temperatures = []

    print(" Welcome to temperature collection in Fahrenheit.\n Enter Q/q to quit.")
    while True:
        try:
            input_temperature = input(" Enter temperature value:")
            if input_temperature.upper() == 'Q':
                break
            else:
                list_of_temperatures.append(round(float(input_temperature), 2))
        except Exception:
            print("**ERROR ==> Check input value.")

    print(" Temperature entries: {} ".format(['%.2f' % temperature for temperature in sorted(list_of_temperatures,
                                                                                            key=float)]))
    print(" Total number of temperature entries: {} ".format(len(list_of_temperatures)))
    print(" Highest temperature in the list: {} F".format(max(list_of_temperatures)))
    print(" Lowest temperature in the list: {} F".format(min(list_of_temperatures)))


if __name__ == '__main__':
    main()
