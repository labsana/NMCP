import math

# Function Definition
func = input('Enter the given function: ')

def f(x):
    y = eval(func)
    return y

# Main Program
# Input Section
a = float(input('Enter the initial value of a: '))
b = float(input('Enter the initial value of b: '))
n = int(input('Enter the number of iterations n: '))

# Process and output section
if f(a) * f(b) < 0:
    print('Root lies in the interval [a, b] =', a, b)
    print('The iterative values of root c are:')
    for k in range(n):
        c = (a + b) / 2
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        print("c = %.4f" % c)
elif f(a) * f(b) == 0:
    print('Root is any one out of the initial guesses.')
else:
    print('No root lies in the interval [a, b] =', a, b)
