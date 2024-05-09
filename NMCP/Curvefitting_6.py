// PROGRAM FOR CURVE FITTING //
# Program for curve fitting using LSE approximation in python.
x=[]
y=[]
xy=[]
x2=[]
coeff=input('Enter x values separated by space ')
x=list(map(float,coeff.split()))
coeff=input('Enter y values separated by space ')
y=list (map(float,coeff.split()))
n=len(x)
for i in range(0,n):
 xy.append(x[i]*y[i])
 x2.append(x[i]*x[i])
sum_x=sum(x)
sum_y=sum(y)
sum_xy=sum(xy)
sum_x2=sum(x2)
b = (n*sum_xy - sum_x*sum_y)/(n*sum_x2 - (sum_x*sum_x));
a = (sum_y - b*sum_x)/n;
print("Required Equation is")
print("y = %0.4f + %0.4fx"%(a,b))
