import numpy as np
import matplotlib.pyplot as plt

hbar = 1973
m = 0.511e6
e = 3.795
n = 1000
ao = 0.529
r = np.linspace(2e-2,20,n,endpoint=False)
dx = r[1] - r[0]
V = -(e**2) / r

coeff = (hbar**2)/(2*m*dx**2)
H = np.zeros((n,n))

for i in range(n):
    H[i,i] = (2*coeff) + V[i]
    if i>0:
        H[i,i-1] = -coeff
    if i<n-1:
        H[i,i+1] = -coeff

eigen_value, eigen_vector = np.linalg.eigh(H)
energies = eigen_value[:3]

l_s = ['-','--','-.']
plt.figure()
for i in range(3):
    print(f"Energy state {i+1}: ",energies[i])
    u = eigen_vector[:,i]
    norm = np.sqrt(np.sum(u**2) * dx)
    u_normalized = u / norm
    if np.mean(u_normalized[:50]) < 0:
       u_normalized *= -1
    R = u/r
    if np.mean(R[:50]) < 0:
        R *= -1
    plt.plot(r/ao,R, label=f"state={i+1}", linestyle=l_s[i])

plt.xlabel("r/a_o")
plt.ylabel("R(r)")
plt.xlim(0,16)
plt.grid(True)
plt.legend()
plt.show()