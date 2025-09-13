import numpy as np
import matplotlib.pyplot as plt

hbar = 1.05457e-34
m = 9.109e-31
L = 2e-9        # half-domain length
N = 500         # number of grid points
a = 1e-9        # finite well width
V0 = 50 * 1.602e-19   # well depth (50 eV in Joules)

# Grid
x = np.linspace(-L, L, N)
dx = x[1] - x[0]

# Kinetic prefactor
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

plt.figure()
for i in range(3):
    psi = eigen_vector[:,i]
    plt.plot(x,psi, label=f"n={i}")

plt.axvline(-a/2, color="k", linestyle="--")
plt.axvline(a/2, color="k", linestyle="--")
plt.xlabel("x (nm)")
plt.ylabel("Energy / ψ(x)")
plt.title("finite Square Well Eigenstates")
plt.legend()
plt.grid(True)
plt.show()