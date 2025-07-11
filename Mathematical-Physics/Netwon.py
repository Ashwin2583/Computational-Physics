import matplotlib.pyplot as plt
import numpy as np

# The function is defined here 
def f(x):
    f=x*np.sin(x) + np.cos(x)
    return f

# The derivative of the function is defined here
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