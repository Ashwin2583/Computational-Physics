import numpy as np
import matplotlib.pyplot as plt

#Inputs
x = [0.147,0.166,0.192,0.210] #Add the x values here
y = [1.86,1.98,1.99,2.72] #Add the y values here
w = [1,1,1,10] #Add the weights here

n = len(x)
sum_w = sum(w)

sum_wx = 0
sum_wxx = 0
sum_wy = 0
sum_wxy = 0
for i in range(n):
    sum_wx = sum_wx + w[i]*x[i]
    sum_wxx = sum_wxx + w[i]*(x[i]**2)
    sum_wy = sum_wy + w[i]*y[i]
    sum_wxy = sum_wxy + w[i]*x[i]*y[i]

A = np.array([[sum_w,sum_wx],[sum_wx,sum_wxx]])
B = np.array([[sum_wy],[sum_wxy]])
R = np.linalg.inv(A)
X = np.matmul(R,B)

new_x = np.linspace(0,10,100)
new_y = X[0] + X[1]*(new_x)
print(X)
plt.figure()
plt.scatter(x,y,label='Points',color='red')
plt.plot(new_x,new_y,label='Bestfit curve')
plt.legend()
plt.show()

