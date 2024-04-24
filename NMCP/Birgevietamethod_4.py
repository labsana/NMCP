a = []
p = []
n = int(input('Enter order of the equation: '))
a = list(map(float, input("Enter coefficients separated by space: ").split()))
p = list(map(float, input('Enter initial guess separated by space: ').split()))
it = int(input('Enter the number of iterations required: '))

for k in range(it):
    b = []
    c = []
    b.append(a[0])
    c.append(b[0])
    for j in range(1, n + 1):
        b.append(a[j] + p[k] * b[j - 1])
        c.append(b[j] + p[k] * c[j - 1])

    p.append(p[k] - b[n] / c[n - 1])
    print("Root of the equation at iteration", k + 1, "is %.4f" % p[k + 1])