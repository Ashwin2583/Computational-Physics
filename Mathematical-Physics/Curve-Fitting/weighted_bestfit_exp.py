import numpy as np
import matplotlib.pyplot as plt

#Inputs
x = [1,1.2,1.4,1.6] #Add the x values here
y = [40.170,73.196,133.372,243.02] #Add the y values here
w = [1,1,10,1] #Add the weights here

Log_y = np.log(y)
n = len(x)
sum_w = sum(w)

sum_wx = 0
sum_wxx = 0
sum_wy = 0
sum_wxy = 0
for i in range(n):
    sum_wx = sum_wx + w[i]*x[i]
    sum_wxx = sum_wxx + w[i]*(x[i]**2)
    sum_wy = sum_wy + w[i]*Log_y[i]
    sum_wxy = sum_wxy + w[i]*x[i]*Log_y[i]

A = np.array([[sum_w,sum_wx],[sum_wx,sum_wxx]])
B = np.array([[sum_wy],[sum_wxy]])
R = np.linalg.inv(A)
X = np.matmul(R,B)

a = np.exp(X[0])
b = X[1]
new_x = np.linspace(0,2,100)
new_y = a * np.exp(b*(new_x))

plt.figure()
plt.scatter(x,y,label='Points',color='red')
plt.plot(new_x,new_y,label='Bestfit curve')
plt.legend()
plt.show()