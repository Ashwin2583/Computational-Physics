import numpy as np
import matplotlib.pyplot as plt

# physical parameters
m = 9.1e-31        # kg
V_o = 3.2e-19      # J
a = 1e-9           # full width (m)
h_cut = 1.0545e-34 # J*s

half_width = a/2
R = np.sqrt((m*V_o*a**2)/(2*h_cut**2))

def even_func(s, rho):
    return s - rho*np.cos(s)
def odd_func(s, rho):
    return s - rho*np.sin(s)

# bisection as before
def bisection(f, a0, b0, tol=1e-6, maxiter=100):
    fa, fb = f(a0), f(b0)
    if fa*fb > 0:
        return None
    a, b = a0, b0
    for _ in range(maxiter):
        c = 0.5*(a+b)
        fc = f(c)
        if abs(fc) < tol or (b-a)/2 < tol:
            return c
        if fa*fc <= 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return 0.5*(a+b)

def wavefunction(x, s, parity, k, K):
    if parity == "odd":
        if x <= -a/2:
            return -np.sin(k*a/2) * np.exp(K*(x + a/2))
        elif x >= a/2:
            return  np.sin(k*a/2) * np.exp(-K*(x - a/2))
        else:
            return np.sin(k*x)

    if parity == "even":
        if x <= -a/2:
            return np.cos(k*a/2) * np.exp(K*(x + a/2))
        elif x >= a/2:
            return np.cos(k*a/2) * np.exp(-K*(x - a/2))
        else:
            return np.cos(k*x)

roots = []
roots.append(("even", bisection(lambda s: even_func(s, R), 0.1, 1.5)))
roots.append(("odd", bisection(lambda s: odd_func(s, R), 1.58, 3.14)))
print("rho =", R)
print("Root in [0.1, 1.5]:", roots[0])
print("Root in [1.58, 3.14]:", roots[1])

plt.figure()
x_vals = np.linspace(-2*a, 2*a, 500)
for parity, s in roots:
    k = 2*s/a
    E = (h_cut**2 * k**2)/(2*m)
    print(f"Energy for {parity}: {E}")
    kappa = np.sqrt(2*m*(V_o - E))/h_cut
    if parity == "even":
        psi_even = [wavefunction(x, s, "even", k, kappa) for x in x_vals]
        plt.plot(x_vals, psi_even,linestyle='-', label="Even state")
    if parity == "odd":
        psi_odd = [wavefunction(x, s, "odd", k, kappa) for x in x_vals]
        plt.plot(x_vals, psi_odd, linestyle='--',label="Odd state")


plt.axvline(-a/2, color="k", linestyle="--")
plt.axvline(a/2, color="k", linestyle="--")
plt.title("Finite Well Eigenfunctions")
plt.xlabel("x (m)")
plt.ylabel("ψ(x)")
plt.grid(True)
plt.legend()
plt.show()