import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from scipy.special import lpmv
import math

l = int(input("Enter l: "))
m = int(input("Enter m: "))

theta_1d = np.linspace(0, np.pi, 200)
phi_1d = np.linspace(0, 2*np.pi, 200)
Phi, Theta = np.meshgrid(phi_1d, theta_1d, indexing='xy')

def spherical_harmonics(l, m, theta, phi):
    if m>=0:
        legendre_poly = lpmv(m, l, np.cos(theta))
        azimuthal_part = np.exp(1j * m * phi)
        norm_const = np.sqrt(((2*l+1)/(4*np.pi)) * (math.factorial(l-m)/math.factorial(l+m)))
        return norm_const * legendre_poly * azimuthal_part
    else:
        # Use relation Y_l^{-m} = (-1)^m * conjugate(Y_l^m)
        return (-1)**m * np.conjugate(spherical_harmonics(l, -m, theta, phi))

# Amplitude
Y_amp = np.real(spherical_harmonics(l, m, Theta, Phi))

# Probability density for coloring
Y_prob = Y_amp**2

# 3D surface coordinates (scaled by amplitude, not probability density)
x = Y_amp * np.sin(Theta) * np.cos(Phi)
y = Y_amp * np.sin(Theta) * np.sin(Phi)
z = Y_amp * np.cos(Theta)

# Color mapping based on probability density
cmap = cm.plasma
norm = colors.Normalize(vmin=0, vmax=Y_prob.max())
sm = cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
facecolors = sm.to_rgba(Y_prob)

fig = plt.figure(figsize=(15, 5))

# 3D plot
ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.plot_surface(x, y, z, facecolors=facecolors, linewidth=0, antialiased=False, shade=False)
fig.colorbar(sm, ax=ax, label="Probability density")
ax.set_title(f'Cartesian surface plot l={l} m={m}')
ax.set_xlabel("x axis"); ax.set_ylabel("y axis"); ax.set_zlabel("z axis")

# colourmap plot
ax2 = fig.add_subplot(1, 3, 2)
mesh = ax2.pcolormesh(phi_1d, theta_1d, Y_prob, cmap=cmap, norm=norm, shading='auto')
fig.colorbar(sm, ax=ax2, label="Probability density")
ax2.set_title("Angular probability (2D)")
ax2.set_xlabel("phi"); ax2.set_ylabel("theta")

#polar plot
ax3 = fig.add_subplot(1, 3, 3, projection='polar')
surf = ax3.pcolormesh(Phi, Theta, Y_prob, cmap=cmap, norm=norm, shading='auto')
fig.colorbar(sm, ax=ax3, label="Probability density")
ax.set_title(f'Polar plot l={l} m={m}')

plt.tight_layout()
plt.show()