import numpy as np
import matplotlib.pyplot as plt

V_0 = 5
eps_min = 1e-6
eps_max = 2*np.pi

eps = np.linspace(eps_min,eps_max,1000)
tan_val = eps*np.tan(eps)
cot_val = -eps*(1/np.tan(eps))
circ = np.sqrt(V_0**2 - eps**2)

M = 50.0 

tan_mask = np.abs(tan_val) > M
cot_mask = np.abs(cot_val) > M

tan_val[tan_mask] = np.nan
cot_val[cot_mask] = np.nan

plt.figure()
plt.plot(eps,tan_val, label="Symmetric")
plt.plot(eps,cot_val, label="Antisymmetric")
plt.plot(eps,circ)
plt.ylim(0, V_0 + 0.5)
plt.xlim(0,5.5)
plt.ylabel("Function value")
plt.xlabel("ε")
plt.legend()
plt.show()