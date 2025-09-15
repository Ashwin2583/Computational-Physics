import numpy as np
import matplotlib.pyplot as plt
import scipy

hbar = 1.05457e-34
m = 9.109e-31
omega = 5.34e21
x_o = np.sqrt(hbar/(m*omega))
N = 500
L = 12*x_o

x = np.linspace(-L/2, L/2, N)
dx = x[1] - x[0]
alpha = -(hbar**2) / (2*m*dx**2)

H = np.zeros((N,N))

for i in range(N):
    #eta = (dx**2)*(x[i]**2)/(x_o**4)
    k = 0.5*m*(omega**2)*(x[i]**2)
    #H[i,i] = -alpha*(2+eta)
    H[i,i] = k - 2*alpha
    if i > 0:
        H[i,i-1] = alpha
    if i < N-1:
        H[i, i+1] = alpha

eigen_value, eigen_vector = np.linalg.eigh(H)

plt.figure()
for i in range(3):
    psi = eigen_vector[:,i]
    norm = np.sqrt(np.trapezoid(np.abs(psi)**2, x))
    psi_scaled = psi / norm
    plt.plot(x, psi_scaled + eigen_value[i], label=f"n={i}") #*0.2 + eigen_value[i]

plt.axvline(-x_o, color="k", linestyle="--")
plt.axvline(x_o, color="k", linestyle="--")
plt.xlabel("x (nm)")
plt.ylabel("Energy / ψ(x)")
plt.title("finite Square Well Eigenstates")
plt.legend()
plt.grid(True)
plt.show()