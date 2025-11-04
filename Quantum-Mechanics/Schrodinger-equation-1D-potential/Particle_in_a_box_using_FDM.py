import numpy as np
import matplotlib.pyplot as plt

hbar = 1.05457e-34
m = 9.109e-31
a = 1e-9
N = 100

x = np.linspace(-a/2, a/2, N)
dx = x[1] - x[0]
coeff = (-1 * hbar**2) / (2 * m * dx**2)

H = np.zeros((N-2, N-2))
for i in range(N-2):
    H[i, i] = -2
    if i > 0:
        H[i, i-1] = 1
    if i < N-3:
        H[i, i+1] = 1

H = coeff * H
eigen_value, eigen_vector = np.linalg.eigh(H)
energy_FDM = eigen_value[:3]

fig = plt.figure(figsize=(18, 15))
linestyles = ['-', '--', '-.', ':']

ax = fig.add_subplot(1,2,1)
print("Energy values calculated using FDM", end='\n')
for i in range(3):
    print(f"state {i+1}",energy_FDM[i]/1.602e-19)
    psi_inner = eigen_vector[:, i]
    norm = np.sqrt(np.trapezoid(np.abs(psi_inner)**2, x[1:-1]))
    psi_inner = psi_inner / norm

    psi = np.zeros(N)
    psi[1:-1] = psi_inner

    max_index = np.argmax(np.abs(psi[1:-1])) + 1 
    if psi[max_index] < 0:
        psi *= -1

    ax.plot(x*1e9, psi, linestyle=linestyles[i % len(linestyles)], label=f"State {i+1}")
ax.axvline(-a*1e9/2, color="k", linestyle="--")
ax.axvline(a*1e9/2, color="k", linestyle="--")
ax.set_xlabel("x (nm)")
ax.set_ylabel("ψ(x)")
ax.set_title("Infinite Square Well Eigenstates (finite-difference method)")
ax.legend()
ax.grid(True)

ax1 = fig.add_subplot(1,2,2)
print("Energy values calculated analytically", end='\n')
for n in range(1, 4):
    E_n = ((hbar**2)*(np.pi**2)*(n**2))/(2*m*(a**2))
    print(f"state {n}",E_n/(1.602e-19))
    psi_n = np.sqrt(2/a) * np.sin(n * np.pi * (x + a/2) / a)
    ax1.plot(x*1e9, psi_n, linestyle=linestyles[n % len(linestyles)], label=f"State {n+1}")
ax1.axvline(-a*1e9/2, color="k", linestyle="--")
ax1.axvline(a*1e9/2, color="k", linestyle="--")
ax1.set_xlabel("x (nm)")
ax1.set_ylabel("ψ(x)")
ax1.set_title("Analytical Eigenstates")
ax1.legend()
ax1.grid(True)

plt.show()