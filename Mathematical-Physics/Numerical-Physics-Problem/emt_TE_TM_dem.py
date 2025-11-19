import numpy as np
import matplotlib.pyplot as plt

V_0 = 4.2
eps_min = 1e-6
eps_max = V_0

eps = np.linspace(eps_min,eps_max,1000)
eps2 = np.linspace(eps_min,2*np.pi,1000)
tan_val = eps*np.tan(eps2)
cot_val = -eps*(1/np.tan(eps2))
circ = np.sqrt(V_0**2 - eps**2)

M = 50.0 

tan_mask = np.abs(tan_val) > M
cot_mask = np.abs(cot_val) > M

tan_val[tan_mask] = np.nan
cot_val[cot_mask] = np.nan

plt.figure()
plt.plot(eps2,tan_val, label="Symmetric")
plt.plot(eps2,cot_val, label="Antisymmetric")
plt.plot(eps,circ)
plt.ylim(0, V_0 + 0.5)
plt.xlim(0,5.5)
plt.ylabel("Function value")
plt.xlabel("ε")
plt.legend()
plt.show()