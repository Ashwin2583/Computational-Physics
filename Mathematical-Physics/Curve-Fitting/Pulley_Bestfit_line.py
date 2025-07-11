import numpy as np
import matplotlib.pyplot as plt

p = [12,15,21,25]
w = [50,70,100,120]

n = len(w)
sum_p = sum(p)
sum_w = sum(w)
w_2 = 0
pw = 0
i = 0

while i < n:
     w_2 = w_2 + (w[i]**2)
     pw = pw + (p[i]*w[i])
     i = i + 1

A = np.array([[n,sum_w],[sum_w,w_2]])
B = np.array([[sum_p],[pw]])
R = np.linalg.inv(A)
X = np.matmul(R,B)

P = []
j = 0
while j < n:
     P.append(X[0] + X[1]*w[j])
     if w[j] == 150:
          print(P[j])
     j = j + 1
print(X[0] + X[1]*150)
plt.figure()
plt.scatter(w,p,label='Points',color='red')
plt.plot(w,P,label='Bestfit curve')
plt.legend()
plt.show()
     
