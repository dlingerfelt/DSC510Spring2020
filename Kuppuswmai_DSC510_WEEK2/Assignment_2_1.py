#Algoritham to get Quote from Fiber Optics installation Organization 
#Assignment Number 2.1
#Created by Rajkumar Kuppuswami
#Created on 03/21/2020
#Used tkinter package to deveop like a form

from tkinter import *
#Define Parameter

def calculatePayment():
# get the qty  
    amt = float(amount.get())
    payment = (amt * .87)
    lblTotal = Label(main, text='$ %.2f' % payment).grid(row=4, column=1, padx=0, pady=10)
#get the company name
    Company = intRate.get()
    lblMonthly = Label(main, text="Hello " + Company + " Welcome to fiber Optics").grid(row=3, column=0, padx=0,
                                                                                        pady=10)
    return
main = Tk()
main.title("Installation cost of fiber optic cable")
main.geometry('500x300')

#Variable to define the QTY and Company Name

amount = StringVar()
intRate = StringVar()

#Label to get the company name
lblIntRate = Label(main, text='Enter Your Company Name :').grid(row=0, column=0, padx=0, pady=10)
entIntRate = Entry(main, textvariable=intRate).grid(row=0, column=1)
#label to get the qty
lblAmount = Label(main, text='How many feet of fiber optic cable do you want install :').grid(row=1, column=0, padx=0, pady=10)
entAmount = Entry(main, textvariable=amount).grid(row=1, column=1)

# Button to calculate 

btn = Button(main, text='Calculate', command=calculatePayment).grid(row=5, column=1)

lblMonthly = Label(main).grid(row=3, column=0, padx=0, pady=10)
lblTotal = Label(main, text='The Total Cost of fiber optic cable is:').grid(row=4, column=0, padx=0, pady=10)

main.mainloop()
