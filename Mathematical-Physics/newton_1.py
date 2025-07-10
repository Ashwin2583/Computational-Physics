import matplotlib.pyplot as plt
import numpy as np

#function 
def f(x):
    f=x**3 - 2*x - 5
    return f
#derivative of the function
def df(x):
    f=3*x**2 - 2
    return f

roots = []
for i in range(1,100):
    x=i
    while True:
        a=x-(f(x)/df(x))
        if (abs(x-a)<0.0001):
            break
        x=a
    roots.append(round(a,4))

print(np.average(roots))
plt.figure()
plt.plot(range(1,100),roots)
plt.grid()
plt.show()

