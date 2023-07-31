# Guess the Number Game
import random

print ('Hello, what is your name?')
name = input()

print ('Well ' + name + ', I am thinking of a number between 1 and 20')
secretnumber = random.randint(1,20)

for GuessesTaken in range (1,7):
    print ('Guess the number')
    guess = int(input())

    if guess < secretnumber:
        print ('Your guess is too low')
    elif guess > secretnumber:
        print ('Your guess is too high')
    else:
        break # This condition is for the correct guess!

if guess == secretnumber:
    print ('Good job!, you guessed my number in ' + str(GuessesTaken) + ' guesses!')
else:
    print ('Sorry, The number I was thinking of was ' + str(int(secretnumber)))

print ('You took ' + str(GuessesTaken) + ' guesses.')
