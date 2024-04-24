# Program for R-K 4th order method

# Function Definition
def f(x, y):
    z = x*x + y*y
    return z

# Main Program
# Input Section
xn = float(input('Enter the value of xn: '))
h = float(input('Enter the value of h: '))
n = int(xn / h)
x0 = 0
y0 = 0

for k in range(n):
    k1 = f(x0, y0)
    k2 = f(x0 + h / 2, y0 + k1 / 2)
    k3 = f(x0 + h / 2, y0 + k2 / 2)
    k4 = f(x0 + h, y0 + k3)
    
    k = (k1 + 2 * k2 + 2 * k3 + k4) * (h / 6)
    y0 += k
    x0 += h

print('Values of x and y: %.4f %.4f' % (x0, y0))
