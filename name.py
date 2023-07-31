# First elif that is true will print
name = 'Bob'
age = 3000
if name == 'Alice':
    print('Hi Alice')
elif age < 12:
    print('You are not Alice kiddo')
elif age > 2000:
    print('Unlike you, Alice is not immortal')
elif age > 100:
    print ('Alice is not a grandma')

# Truthey and Falsey values
print('Enter a name.')
name = input()
if name:
    print('Nice to meet you, ' + name)
else:
    print('You did not enter anything')