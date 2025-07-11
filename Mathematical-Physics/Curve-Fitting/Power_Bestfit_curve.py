import numpy as np
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,5.66,10.39,16,22.36]

n = len(x)
sum_x = sum(x)
log_y = np.log(y)
log_x = np.log(x)
sum_logy = sum(log_y)
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
b = np.exp(X[1])
new_x = np.linspace(1,5,100)
new_y = a * b**(new_x)

plt.figure()
plt.scatter(x,y,label='Points',color='red')
plt.plot(new_x,new_y,label='Bestfit curve')
plt.legend()
plt.show()
