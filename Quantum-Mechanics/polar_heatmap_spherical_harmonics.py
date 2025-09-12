import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import cm

theta = np.linspace(0, np.pi, 200)
phi = np.linspace(0, 2*np.pi, 200)
phi, theta = np.meshgrid(phi, theta)

def spherical_harmonics(theta, phi):
    return (-1)*np.sqrt(3/(8*np.pi))*np.sin(theta)*np.exp(1j*phi)

Y = (abs(spherical_harmonics(theta, phi)))**2
fig, ax = plt.subplots(subplot_kw={"projection":"polar"})

surf = ax.pcolormesh(phi, theta, Y, cmap='plasma', shading='auto')
fig.colorbar(surf, ax=ax)
plt.show()
