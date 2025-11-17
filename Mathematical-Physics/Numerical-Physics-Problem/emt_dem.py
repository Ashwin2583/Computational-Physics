import numpy as np
import matplotlib.pyplot as plt
from math import pi

V0 = 4.5 
eps_min = 1e-6
eps_max = V0 - 1e-6

def rhs(eps):
    return np.sqrt(np.clip(V0**2 - eps**2, 0, None))

def f_sym(eps):
    return eps * np.tan(eps) - rhs(eps)

def f_asym(eps):
    return -eps / np.tan(eps) - rhs(eps)

eps_grid = np.linspace(eps_min, eps_max, 4000)
tan_vals = np.tan(eps_grid)

sym_curve = np.where(np.abs(np.cos(eps_grid))>1e-6, f_sym(eps_grid), np.nan) #eps_grid * tan_vals
asym_curve = np.where(np.abs(np.sin(eps_grid))>1e-6, f_asym(eps_grid), np.nan) #-eps_grid/np.tan(eps_grid)
rhs_curve = rhs(eps_grid)

plt.figure(figsize=(9,6))
plt.plot(eps_grid, sym_curve, label=r'$\epsilon\tan\epsilon$ (LHS symmetric)')
plt.plot(eps_grid, asym_curve, label=r'$-\epsilon\cot\epsilon$ (LHS antisymmetric)')
plt.plot(eps_grid, rhs_curve, '--', label=r'$\sqrt{V^2-\epsilon^2}$ (RHS)')
plt.ylim(-V0, V0)
plt.xlim(0, eps_max)
plt.xlabel(r'$\epsilon$')
plt.ylabel('Function value')
plt.title(f'Slab waveguide mode equations (V = {V0})')
plt.grid(True)
plt.legend()
plt.show()