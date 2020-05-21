"""
File: assignment11_1.py
Author: Bhushan Suryawanshi
Date:Wednesday, May 18, 2020
Course: DSC510-T303 Introduction to Programming (2205-1)

Desc: The program will allow user to add items to Cash Register.
It has two methods -
getTotal – returns totalPrice
getCount – returns the itemCount of the cart

User can add as many items as they want before they quit by pressing Q/q.
After exit program will print number of items added and total price of items.

"""
import locale


class CashRegister:
    count = 0
    total = 0

    def get_total(self):
        locale.setlocale(locale.LC_ALL, 'en_US')
        return locale.currency(self.total, grouping=True)

    def get_count(self):
        return self.count

    def add_item(self, price):
        self.count += 1
        self.total = self.total + price


# Display the cash register details
def display(register_obj):
    print(f'Number of items you added : {register_obj.get_count()} and Total Price:{register_obj.get_total()}')


def main():
    print(f" Welcome to Cash Register.\nEnter Q/q to Exit.")

    # creating cash register object
    cash_register = CashRegister()

    while True:
        try:
            price = input(f"enter price of item: ")
            if 'Q' == price.upper():
                break
            else:
                # Add price to cash register
                cash_register.add_item(float(price))

        except Exception as err:
            print(f'Check the price Entered: {err}')

    display(cash_register)


if __name__ == '__main__':
    main()
