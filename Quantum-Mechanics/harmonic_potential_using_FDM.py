import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite, factorial

hbar = 1.05457e-34
m = 9.109e-31
omega = 5.34e9
x_o = np.sqrt(hbar/(m*omega))
print(f"oscillator length: {round(x_o*1e9, 6)} nm")
N = 500
L = 12*x_o

x = np.linspace(-L/2, L/2, N)
dx = x[1] - x[0]
alpha = -(hbar**2) / (2*m*dx**2)

H = np.zeros((N,N))

for i in range(N):
    k = 0.5*m*(omega**2)*(x[i]**2)
    H[i,i] = k - 2*alpha
    if i > 0:
        H[i,i-1] = alpha
    if i < N-1:
        H[i, i+1] = alpha

eigen_value, eigen_vector = np.linalg.eigh(H)
energy_FDM = eigen_value[:3]
fig = plt.figure(figsize=(15,6))
linestyles = ['-', '--', '-.', ':']

ax = fig.add_subplot(1,2,1)
print("Energy values calculated using FDM", end='\n')
for i in range(3):
    print(f"state {i}",energy_FDM[i]/(1.602e-19))
    psi = eigen_vector[:,i]
    norm = np.sqrt(np.trapezoid(np.abs(psi)**2, x))
    psi_scaled = psi / norm
    max_index = np.argmax(np.abs(psi_scaled))
    if psi_scaled[max_index] < 0:
        psi_scaled *= -1
    ax.plot(x*1e9, psi_scaled, linestyle=linestyles[i % len(linestyles)], label=f"n={i}")

ax.set_xlabel("x (nm)")
ax.set_ylabel("ψ(x)")
ax.set_title("Harmonic Potential Eigenstates")
ax.legend()
ax.grid(True)

ax1 = fig.add_subplot(1,2,2)
print("Energy values calculated analytically", end='\n')
for n in range(3):
    E_n = (n+1/2)*hbar*omega
    print(f"state {n}",E_n/(1.602e-19))
    xi = x / x_o
    Hn = hermite(n)(xi)
    prefactor = 1.0 / (np.sqrt(2**n * factorial(n))) * (1.0/np.pi**0.25 / np.sqrt(x_o))
    psi_n = prefactor * Hn * np.exp(-xi**2/2)
    ax1.plot(x*1e9, psi_n, linestyle=linestyles[i % len(linestyles)], label=f"n={n}")

ax1.set_title("Analytical Harmonic Potential")
ax1.set_xlabel("x (nm)")
ax1.set_ylabel("ψ(x)")
ax1.legend()
ax1.grid(True)

plt.tight_layout()

plt.show()