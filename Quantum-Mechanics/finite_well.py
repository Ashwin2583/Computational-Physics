import numpy as np
import matplotlib.pyplot as plt

# physical parameters
m = 9.1e-31        # kg
V_o = 3.2e-19      # J
a = 1e-9           # full width (m)
h_cut = 1.0545e-34 # J*s

# use half-width because well is -a/2 .. +a/2
half = a/2.0

# correct rho for centered well
rho = (a/h_cut)*np.sqrt(2*m*V_o)

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
        if x <= -a:
            return np.exp(K*x)
        elif x >= a:
            return np.exp(-K*x)
        else:
            return np.sin(k*x)
    
    if parity == "even":
        if x <= -a:
            return np.exp(K*x)
        elif x >= a:
            return np.exp(-K*x)
        else:
            return np.cos(k*x)

# eigenvalues
roots = []
roots.append(("even", bisection(lambda s: even_func(s, rho), 0.1, 1.5)))
roots.append(("odd", bisection(lambda s: odd_func(s, rho), 1.58, 3.14)))
print("rho =", rho)
print("Root in [0.1, 1.5]:", roots[0])
print("Root in [1.58, 3.14]:", roots[1])

x_vals = np.linspace(-3*a, 3*a, 500)
for parity, s in roots:
    k = s/a
    E = (h_cut**2 * k**2)/(2*m)
    kappa = np.sqrt(2*m*(V_o - E))/h_cut
    if parity == "even":
        psi_even = [wavefunction(x, s, "even", k, kappa) for x in x_vals]
        plt.plot(x_vals, psi_even, label="Even state")
    if parity == "odd":
        psi_odd = [wavefunction(x, s, "odd", k, kappa) for x in x_vals]
        plt.plot(x_vals, psi_odd, label="Odd state")

plt.axvline(-a, color="k", linestyle="--")
plt.axvline(a, color="k", linestyle="--")
plt.title("Finite Well Eigenfunctions")
plt.xlabel("x (m)")
plt.ylabel("ψ(x)")
plt.grid(True)
plt.legend()
plt.show()