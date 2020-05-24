# File: Assignment_11.1
# Name: Hanh Tran
# Due Date: 5/24/2020
# Course: DSC510-T303 Introduction to Programming (2205-1)
# Desc: This program will do the following:
# Create a simple cash register by creating an instance of the CashRegister class.
# Have a loop which allows the user to continue to add items to the cart until they request to quit.
# Print the total number of items in cart.
# Print the total cost of items in cart. Output is formatted as currency.

# imported package to format total as USD local currency
import locale

# created class
class CashRegister:
    # we will start at nothing
    num_of_items = 0
    total = 0
    # created instance method called addItem which takes parameter for price
    def addItem(self, price):
        self.num_of_items += 1
        self.total = self.total + float(price)
    # created getter method that returns total price
    def getTotal(self):
        return self.total
    # created getter method that returns number of items in cart
    def getCount(self):
        return self.num_of_items
# created main function that contains a loop to allow user to add as many items to cart as they want
def main():
    print('Welcome to the Cash Register!')
    cash_register = CashRegister()
    locale.setlocale(locale.LC_ALL, 'en_US')
    while True:
        price = input('Please enter a price to add an item to cart or C to complete and view total:\n')
        try:
            cash_register.addItem(float(price))
        # the sentinel value C or c allows user to quit adding items
        except:
            price == 'C' or 'c'
            break

    # assigned instance of class for number of items to variable for printing
    items_cart = int(cash_register.getCount())
    # assigned instance of class for total cost to variable for printing
    total_cost = float(cash_register.getTotal())
    print('This is the total number of items in your cart: {}'.format((items_cart)))
    # printed total cost of items in local currency USD
    print('Your total amounts to: {}'.format(locale.currency(total_cost)))
main()
