# This program says hello and asks for my name.

print('Hello world!')
print('What is your name?') #ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print()
print('The length of your name is:')
print(len(myName))
print()

print('What is your age?') #ask for their age
myAge = input()
print('You will be ' + str(int(myAge)+1) + ' in a year.')
print() #print nextline
