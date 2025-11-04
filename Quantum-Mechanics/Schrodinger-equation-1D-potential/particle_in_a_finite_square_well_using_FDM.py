import numpy as np
import matplotlib.pyplot as plt

hbar = 1.05457e-34
m = 9.109e-31
L = 1.5e-9        # domain length
N = 500         # number of grid points
a = 1e-9        # finite well width
V0 = 3.2e-19 #2 * 1.602e-19   # well depth (50 eV in Joules)

x = np.linspace(-L, L, N)
dx = x[1] - x[0]

coeff = -(hbar**2) / (2*m*dx**2)

H = np.zeros((N,N))

for i in range(N):
    if abs(x[i]) < a/2:
        V_i = -V0
    else:
        V_i = 0
    H[i,i] = -2*coeff + V_i
    if i > 0:
        H[i,i-1] = coeff
    if i < N-1:
        H[i, i+1] = coeff

eigen_value, eigen_vector = np.linalg.eigh(H)
energy_FDM = eigen_value[:3]

plt.figure(figsize=(15,9))
linestyles = ['-', '--', '-.', ':']
print("Energy values calculated using FDM", end='\n')
for i in range(3):
    print(f"state {i}",energy_FDM[i]/(1.602e-19))
    psi = eigen_vector[:,i]
    norm = np.sqrt(np.trapezoid(np.abs(psi)**2, x))  # continuous normalization
    psi = psi / norm
    plt.plot(x*1e9,psi, linestyle=linestyles[i % len(linestyles)], label=f"State {i+1}")

plt.axvline(-a*1e9/2, color="k", linestyle="--")
plt.axvline(a*1e9/2, color="k", linestyle="--")
plt.xlabel("x (nm)")
plt.ylabel("ψ(x)") 
plt.title("finite Square Well Eigenstates (finite-difference method)")
plt.legend()
plt.grid(True)
plt.show()