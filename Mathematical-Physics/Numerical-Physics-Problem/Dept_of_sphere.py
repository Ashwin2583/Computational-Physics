import numpy as np
import matplotlib.pyplot as plt

d = 0.001
r = float(input("Enter the radius of sphere: "))
d_s = float(input("Enter the density of sphere: "))
d_f = float(input("Enter the density of fluid: "))

# The equation of dept of the sphere
def f(x):
    return ((x**2)*(3*r - x)*d_f) - (4*d_s*(r**3))

while True:
      a = float(input("First num: "))
      b = float(input("second num: "))
      if f(a) * f(b) > 0:
             continue
      else:
          break
          
# Using Bisection algorithm to find the root
while True:
      c = (a+b)/2
      if abs(f(c)) < d:
             break
      if f(a)*f(c) < 0:
             b = c
      else:
             a = c

print("The depth to which object sinks ",c)


      
    

