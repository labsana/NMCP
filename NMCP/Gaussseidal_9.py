#Program for Gauss seidel method
#Function Definition
import math
def X1(x2,x3):
 return((20 +3*(x2) - 2*(x3))/8)
def X2(x1,x3):
 return((33 -4*(x1) + (x3))/11)
def X3(x1,x2):
 return((35 - 6*(x1) - 3*(x2))/12)
x1=float(input('Enter the value of x1:'))
x2=float(input('Enter the value of x2:'))
x3=float(input('Enter the value of x3:'))
print('display all values x1, x2, x3 ')
print(' %0.3f'%x1, '%0.3f'%x2, '%0.3f'%x3,);
n=5
for k in range(0,n):
 y1=X1(x2,x3);
 y2=X2(y1,x3);
 y3=X3(y1,y2);
 x1 = y1;
 x2 = y2;
 x3 = y3;
 print(' %0.3f'%x1, '%0.3f'%x2, '%0.3f'%x3,);
