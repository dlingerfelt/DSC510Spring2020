# File: Assignment_11_1.py
# Name: Roni Kaakaty
# Date: 05/23/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)

# This program will do the following:
# Have a welcome message for the user.
# Will contain a CashRegister class.
# Will have an instance method which takes one parameter for price and keep track of the number of items.
# Should contain 2 getter methods: getTotal and getCount.
# Should contain instance of the CashRegister class.
# Should contain a loop which allows the user to continue to add items to the cart until they request to quit.
# Should print total $ amount of the cart.
# Output should be formatted as currency using locale.setlocale and locale.currency.

import locale

class CashRegister:

    def __init__(self):
        self.__itemCount = 0
        self.__totalPrice = 0.00

    def getTotal(self):
        return self.__totalPrice

    def getCount(self):
        return self.__itemCount

    def add_item(self, cost):
        self.__itemCount += 1
        self.__totalPrice = self.__totalPrice + float(cost)

def main():
    print(f'{"*" * 77}')
    print("Welcome to the Online Cash Register. Once you're done, press T for the Total.")
    print(f'{"*" * 77}')
    register = CashRegister()
    locale.setlocale(locale.LC_ALL, 'en_US.utf-8')

    while True:
        try:
            cost = input("What's the price of the item?: ")
            if 'T' == cost.upper():
                break
            else:
                register.add_item(cost)
        except ValueError:
            print('Please check the entered price and try again.')

    total_Price: float = register.getTotal()
    total_itemCount: int = register.getCount()
    print('The total number of items in your shopping cart: {}'.format((total_itemCount)))
    print('The total price of the items in your shopping cart is: {}'.format(locale.currency(total_Price)))

main()





