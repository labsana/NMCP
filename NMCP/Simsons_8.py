#Program in python for Simpson's 1/3 rd rule of integration
#Function Definition
def y(x):
 z=1/(1+x)
 return z
# Main Program
# Input Section
x0=float(input('Enter the value of x0:'))
xn=float(input('Enter the value of xn:'))
n=int(input('Enter the value of subintervals n:'))
#process section
h=(xn-x0)/n ;
print('step size h=',h)
print('Formula = (h/3)*[(y0+yn)+2*(y2+y4+...) +4*(y1+y3+y5..)] ')
sum=y(x0)+y(xn)+4*y(x0+h);
for k in range(3,n+1,2):
 sum=sum+4*y(x0+k*h)+2*y(x0+(k-1)*h);
result=(h/3)*(sum);
print("The result of integration is=%.3f"%result);
