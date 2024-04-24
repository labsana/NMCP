a = []
b = []
proots = 0
nroots = 0

coeff = input('Enter polynomial coefficients separated by space: ')
a = list(map(float, coeff.split()))

for j in range(0, len(a)-1):
    if a[j] * a[j+1] < 0:
        proots += 1

for j in range(0, len(a)):
    b.append(a[j] * ((-1) ** j))

for j in range(0, len(a)-1):
    if b[j] * b[j+1] < 0:
        nroots += 1

croots = len(a) - 1 - proots - nroots

print("\nApplying Descartes Rule of Signs, we get:")
print("No of +ve real roots: at most", proots)
print("No of -ve real roots: at most", nroots)
print("No of complex roots: at least", croots)
