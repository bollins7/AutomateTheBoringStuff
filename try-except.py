# Without the try and except statements, this code would fail at 0 and not go on. Since computers
# are stupid and can't divide by 0
# except ZeroDivisionError: lets the program know that if we receive that error, just skip instead of 
# crash

def div42by (divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print ('Error, you tried to divide by 0')

print (div42by(2))
print (div42by(12))
print (div42by(0))
print (div42by(1))