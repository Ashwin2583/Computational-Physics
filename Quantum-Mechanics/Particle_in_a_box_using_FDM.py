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

fig = plt.figure(figsize=(18, 15))
linestyles = ['-', '--', '-.', ':']

ax = fig.add_subplot(1,2,1)
for i in range(3):
    psi = eigen_vector[:,i]
    norm = np.sqrt(np.trapezoid(np.abs(psi)**2, x))  # continuous normalization
    psi = psi / norm
    ax.plot(x*1e9, psi , linestyle=linestyles[i % len(linestyles)], label=f"State {i+1}")
ax.axvline(-a*1e9/2, color="k", linestyle="--")
ax.axvline(a*1e9/2, color="k", linestyle="--")
ax.set_xlabel("x (nm)")
ax.set_ylabel("ψ(x)")
ax.set_title("Infinite Square Well Eigenstates (finite-difference method)")
ax.legend()
ax.grid(True)

ax1 = fig.add_subplot(1,2,2)

ax1 = fig.add_subplot(1,2,2)
for n in range(1,4):
    if n % 2 == 0:  # even n → sine
        psi_n = np.sqrt(2/a) * np.sin(n*np.pi*x/a)
    else:           # odd n → cosine
        psi_n = np.sqrt(2/a) * np.cos(n*np.pi*x/a)
    ax1.plot(x*1e9,psi_n, linestyle=linestyles[n % len(linestyles)], label=f"State {n+1}")
ax1.axvline(-a*1e9/2, color="k", linestyle="--")
ax1.axvline(a*1e9/2, color="k", linestyle="--")
ax1.set_xlabel("x (nm)")
ax1.set_ylabel("ψ(x)")
ax1.set_title("Analytical Eigenstates")
ax1.legend()
ax1.grid(True)

plt.show()
