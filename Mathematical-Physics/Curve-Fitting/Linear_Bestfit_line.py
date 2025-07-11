import numpy as np
import matplotlib.pyplot as plt

x = [0.147,0.166,0.192,0.210] # Add the x-values here
y = [1.86,1.98,1.99,2.72] # Add the y-values here

n = len(x)
sum_x = sum(x)
sum_y = sum(y)
mult = 0  #X_i * y_i
sq = 0    #X_i^2

i = 0
while i < n:
    mult = mult + (x[i]*y[i])
    sq = sq + (x[i]**2)
    i = i + 1

A = np.array([[n,sum_x],[sum_x,sq]])
B = np.array([[sum_y],[mult]])
R = np.linalg.inv(A)
X = np.matmul(R,B)
yy = []
j = 0
while j < n:
    yy.append(X[0] + X[1]*x[j])
    j = j + 1

print(X)
plt.figure()
plt.scatter(x,y,label='Points',color='red')
plt.plot(x,yy,label='Bestfit line')
plt.legend()
plt.show()
