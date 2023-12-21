# This program says hello and asks for my name

print('Hello, World!')
print ('What is your name?') # ask for their name

# Requires an input from the user
myName = input()

print ('It is good to meet you,' + myName)

print('The length of your name is:')

# len signifies length of the variable
print(len(myName))

print('What is your age?') #ask for their age

# Another input from the user
myAge = input()

# str signifies that it will be a part of the quotation marks, int is the whole number, and 
# includes the variable that the user inputted. +1 for the total. 


print('You will be ' +str(int(myAge) +1) + ' in a year')