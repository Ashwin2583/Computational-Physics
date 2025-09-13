import numpy as np
import matplotlib.pyplot as plt

hbar = 1.05457e-34
m = 9.109e-31
L = 1e-9
N = 100
a = 10e-8

dx = L/(N-1)
coeff = (-1*hbar**2)/(2*m*dx)
# Symmetric well
x = np.linspace(-L,L,N)

H = np.zeros((N,N))
for i in range(N):
    H[i,i] = -2
    if i > 0:
        H[i,i-1] = 1
    if i < N-1:
        H[i,i+1] = 1

H = coeff*H
eigen_value, eigen_vector = np.linalg.eigh(H)

plt.figure()
for i in range(3):
    psi = eigen_vector[:,i]
    plt.plot(x,psi)

plt.grid(True)
plt.show()
