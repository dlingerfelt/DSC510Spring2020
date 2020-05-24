# File: BUNCH_11_1.py
# Name: Jonathan Bunch
# Date: 24 May, 2020
# Course: DSC510-T303 Introduction to Programming (2205-1)


# Your program must have a welcome message for the user.
# Your program must have one class called CashRegister.
# Your program will have an instance method called addItem which takes one parameter for price. The method should
# also keep track of the number of items in your cart.
# Your program should have two getter methods.
# getTotal – returns totalPrice
# getCount – returns the itemCount of the cart
# Your program must create an instance of the CashRegister class.
# Your program should have a loop which allows the user to continue to add items to the cart until they request to quit.
# Your program should print the total number of items in the cart.
# Your program should print the total $ amount of the cart.
# The output should be formatted as currency. Be sure to investigate the locale class. You will need to call
# locale.setlocale and locale.currency.


import locale

locale.setlocale(locale.LC_ALL, "")


class CashRegister:
    """This class has the following attributes: a list of prices, the number of prices on that list, and
    the sum of all the prices on that list."""

    def __init__(self):
        self.items = []
        self.count = int(0)
        self.total = float(0)

    def add_item(self, item_price):
        self.items.append(item_price)
        self.count = len(self.items)
        self.total = sum(self.items)
        print(locale.currency(item_price), 'added to list.')

    def get_total(self):
        return self.total

    def get_count(self):
        return self.count


# This function collects entries from the user and gives the user the option to finish by
# entering any alphabetic character(s).
def get_price(cr_object):
    run_loop = True
    while run_loop:
        price = input('Enter the price of an item or any letter to finish: ')
        if price.isalpha():
            print('Entry Complete!')
            run_loop = False
        else:
            try:
                price = float(price)
            except ValueError:
                print('Error: entries must be in standard numerical format.')
            else:
                if price < 0:
                    print('Error: entries must be positive numbers.')
                else:
                    price = round(price, 2)
                    cr_object.add_item(price)


def main():
    print('Welcome to our cash register program!')
    cost = CashRegister()
    get_price(cost)
    print('Total number of items on list: ', cost.get_count())
    print('Total cost of items on list: ', locale.currency(cost.get_total()))
    print('Thanks for using our cash register program!')


main()
