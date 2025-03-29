import matplotlib.pyplot as plt
import numpy as np

#function 
def f(x):
    f=x*np.sin(x) + np.cos(x)
    return f
#derivative of the function
def df(x):
    f=x*np.cos(x)
    return f

x=int(input("Enter guess : "))
while True:
    a=x-(f(x)/df(x))
    if (abs(x-a)<0.0001):
        break
    x=a
print("The root of the equation is:-", a)



q=[]
w=[]
r=[]
for i in range (-50,50,1):
    q.append(i)
    w.append(f(i))
    
j = 0
while j < len(q) - 1:    
        y = q[j]
        while True:
             b = y -(f(y)/df(y))
             if (abs(y-b)<0.0001 or df(y) == 0):
                  r.append(b)
                  break
             y = b
        j = j + 1

plt.figure()
plt.plot(q,w)
plt.scatter(r,[0] * len(r),color='red', label= 'Roots')
plt.legend()
plt.grid(True)
plt.show()