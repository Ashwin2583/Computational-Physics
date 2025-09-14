import numpy as np
import matplotlib.pyplot as plt

hbar = 1.05457e-34
m = 9.109e-31
a = 1e-9
N = 100

# Symmetric well
x = np.linspace(-a/2,a/2,N)
dx = x[1] - x[0]
coeff = (-1*hbar**2)/(2*m*dx**2)

H = np.zeros((N,N))
for i in range(N):
    H[i,i] = -2
    if i > 0:
        H[i,i-1] = 1
    if i < N-1:
        H[i,i+1] = 1

H = coeff*H
eigen_value, eigen_vector = np.linalg.eigh(H)

linestyles = ['-', '--', '-.', ':']
plt.figure()
for i in range(3):
    psi = eigen_vector[:,i]
    plt.plot(x, psi, linestyle=linestyles[i % len(linestyles)], label=f"State {i+1}")

plt.axvline(-a/2, color="k", linestyle="--")
plt.axvline(a/2, color="k", linestyle="--")
plt.xlabel("x (nm)")
plt.ylabel("Energy / ψ(x)")
plt.title("Infinite Square Well Eigenstates")
plt.legend()
plt.grid(True)
plt.show()
