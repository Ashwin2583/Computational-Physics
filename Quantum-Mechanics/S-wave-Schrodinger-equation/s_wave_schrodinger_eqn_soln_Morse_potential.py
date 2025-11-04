import numpy as np
import matplotlib.pyplot as plt

hbar = 1973
m = 940e6
n = 1000
D = 0.755501
a = 1.44
r_0 = 0.131349
r = np.linspace(2e-2,20,n,endpoint=False)
r_dash = (r-r_0)/r
dx = r[1] - r[0]
V = D*((np.exp(-2*a*r_dash))-(np.exp(-a*r_dash)))

coeff = (hbar**2)/(2*m*dx**2)
H = np.zeros((n,n))

for i in range(n):
    H[i,i] = (2*coeff) + V[i]
    if i>0:
        H[i,i-1] = -coeff
    if i<n-1:
        H[i,i+1] = -coeff

eigen_value, eigen_vector = np.linalg.eigh(H)
energies = eigen_value[:2]

l_s = ['-','--','-.']

fig = plt.figure(figsize=(18,10))

ax_u = fig.add_subplot(1,2,1)
u_2 = []
for i in range(2):
    print(f"Energy state {i+1}: ",round(energies[i],3))
    u = eigen_vector[:,i]
    norm = np.sqrt(np.sum(u**2) * dx)
    u_normalized = u / norm
    if np.mean(u_normalized[:50]) < 0:
       u_normalized *= -1
    u_2.append(u_normalized**2)
    ax_u.plot(r,u_normalized, label=f"state={i+1}", linestyle=l_s[i])

ax_u.set_xlabel("r")
ax_u.set_ylabel("u(r)")
ax_u.set_xlim(0,7)
ax_u.set_title("Eigenstates u(r)")
ax_u.grid(True)
ax_u.legend()

ax_u2 = fig.add_subplot(1,2,2)
for j in range(2):
    ax_u2.plot(r,u_2[j], label=f"state={j+1}", linestyle=l_s[j])

ax_u2.set_xlabel("r")
ax_u2.set_ylabel("u(r)**2")
ax_u2.set_xlim(0,6)
ax_u2.set_title("Probability density P(r)")
ax_u2.grid(True)
ax_u2.legend()

plt.tight_layout()
plt.show()