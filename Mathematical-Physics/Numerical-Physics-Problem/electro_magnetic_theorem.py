import numpy as np
import matplotlib.pyplot as plt

v_o = 4.5

def f_eta(eps, v_o):
    return np.sqrt(np.clip(v_o**2 - eps**2, 0, None))

def f_sym(eps, v_o):
    return eps * np.tan(eps)

def f_asym(eps, v_o):
    return -eps / np.tan(eps)


eps = np.linspace(0.001, 2 * np.pi, 1000)


sym_vals = np.where(np.abs(np.cos(eps)) > 1e-3, f_sym(eps, v_o), np.nan)
asym_vals = np.where(np.abs(np.sin(eps)) > 1e-3, f_asym(eps, v_o), np.nan)

plt.figure(figsize=(8,6))
plt.plot(eps, sym_vals, label='Symmetric (ε tan ε)')
plt.plot(eps, asym_vals, label='Antisymmetric (-ε cot ε)')
plt.plot(eps, f_eta(eps, v_o), '--', label='RHS √(V² - ε²)')
plt.xlabel('ε')
plt.ylabel('Function value')
plt.title(f'Symmetric and Antisymmetric TE modes (V₀ = {v_o})')
plt.grid(True)
plt.legend()
plt.ylim(-v_o, v_o)
plt.show()
