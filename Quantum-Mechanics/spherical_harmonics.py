import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from scipy.special import lpmv
import math

l = int(input("Enter l: "))
m_in = int(input("Enter m: "))

def f(l, m, theta, phi):
    if l == 0 and m == 0:
        return (1/np.sqrt(4*np.pi))*np.ones_like(theta)
    if l == 1 and m == 0:
        return (3/(4*np.pi))*np.cos(theta)
    if l == 1 and m == -1:
        return math.sqrt((3/(8*np.pi))) * np.sin(theta) * np.exp(-1*1j*phi)
    if l == 1 and m == 1:
        return (-1)*math.sqrt((3/(8*np.pi))) * np.sin(theta) * np.exp(1*1j*phi)

theta_1d = np.linspace(0, np.pi, 200)      
phi_1d   = np.linspace(0, 2*np.pi, 200)    
Phi, Theta = np.meshgrid(phi_1d, theta_1d, indexing='xy')

Y = f(l, m_in,Theta, Phi)
Y_real = np.real(Y)

# Amplitude and probability density
Y_amp  = np.abs(Y_real)
Y_prob = Y_real**2

# 3D surface coordinates (radius from amplitude)
x = Y_amp * np.sin(Theta) * np.cos(Phi)
y = Y_amp * np.sin(Theta) * np.sin(Phi)
z = Y_amp * np.cos(Theta)

# Shared color mapping based on probability density
cmap = cm.plasma
norm = colors.Normalize(vmin=0.0, vmax=float(Y_prob.max()))
sm = cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])

facecolors = sm.to_rgba(Y_prob)

# Figure with three panels: 3D, 2D (theta vs phi), and polar (phi vs theta)
fig = plt.figure(figsize=(18, 5))

# 3D surface
ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.plot_surface(x, y, z, facecolors=facecolors, linewidth=0, antialiased=False, shade=False)
fig.colorbar(sm, ax=ax, label="Probability density (Y_real^2)")
ax.set_title(f'3D surface (real tesseral) l={l} m={m_in}')
ax.set_xlabel("x axis"); ax.set_ylabel("y axis"); ax.set_zlabel("z axis")

# 2D map (theta vs phi)
ax2 = fig.add_subplot(1, 3, 2)
ax2.pcolormesh(phi_1d, theta_1d, Y_prob, cmap=cmap, norm=norm, shading='auto')
fig.colorbar(sm, ax=ax2, label="Probability density (Y_real^2)")
ax2.set_title("Angular probability (2D)")
ax2.set_xlabel("phi"); ax2.set_ylabel("theta")

# Polar plot (angle=phi, radius=theta)
ax3 = fig.add_subplot(1, 3, 3, projection='polar')
ax3.pcolormesh(Phi, Theta, Y_prob, cmap=cmap, norm=norm, shading='auto')
fig.colorbar(sm, ax=ax3, label="Probability density (Y_real^2)")
ax3.set_title(f'Polar plot (real tesseral) l={l} m={m_in}')

plt.tight_layout()
plt.show()