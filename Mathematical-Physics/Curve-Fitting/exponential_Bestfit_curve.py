import numpy as np
import matplotlib.pyplot as plt

x = [2,4,6,8,10]
y = [4.077,11.084,30.128,81.897,222.62]
log_y = np.log(y)
sum_logy = sum(log_y)  
n = len(x)
sum_x = sum(x)
xlogy = 0
x_2 = 0
i = 0

while i < n:
     xlogy = xlogy + (x[i]*log_y[i])
     x_2 = x_2 + (x[i]**2)
     i = i + 1

A = np.array([[n,sum_x],[sum_x,x_2]])
B = np.array([[sum_logy],[xlogy]])
R = np.linalg.inv(A)
X = np.matmul(R,B)

a = np.exp(X[0])
b = X[1]
new_x = np.linspace(1,10,100)
new_y = a * np.exp(b*new_x)

plt.figure()
plt.scatter(x,y,label='Points',color='red')
plt.plot(new_x,new_y,label='Bestfit line')
plt.legend()
plt.show()
