# Program for intermediate value theorem
# Function Definition
import math

func = input('Enter given function: ')
a = float(input('Enter lower range value a: '))
b = float(input('Enter upper range value b: '))

def f(x):
    y = eval(func)
    return y

# Process and output section
print('As per Intermediate Value Theorem:')
if f(a) * f(b) < 0:
    print('At least one root lies in the interval [a, b] =', a, b)
elif f(a) * f(b) == 0:
    print('Any one initial value may be the root')
else:
    print('No root lies in the interval [a, b] =', a, b)
