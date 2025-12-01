import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from scipy.special import sph_harm

# -------------------------------
#  Real Spherical Harmonic
# -------------------------------
def real_Y(l, m, theta, phi):
    Yc = sph_harm(m, l, phi, theta)

    if m > 0:
        return np.sqrt(2) * (-1)**m * np.real(Yc)
    elif m < 0:
        return np.sqrt(2) * (-1)**m * np.imag(sph_harm(-m, l, phi, theta))
    else:
        return np.real(Yc)

# -------------------------------
# User input
# -------------------------------
l = int(input("Enter l: "))
m_in = int(input("Enter m: "))

# -------------------------------
# Mesh grid
# -------------------------------
theta_1d = np.linspace(0, np.pi, 200)
phi_1d   = np.linspace(0, 2*np.pi, 200)

Phi, Theta = np.meshgrid(phi_1d, theta_1d, indexing='xy')

# -------------------------------
# Harmonic + densities
# -------------------------------
Y = real_Y(l, m_in, Theta, Phi)
Y_amp  = np.abs(Y)
Y_prob = Y_amp**2

# -------------------------------
# 3D coordinates from amplitude
# -------------------------------
x = Y_amp * np.sin(Theta) * np.cos(Phi)
y = Y_amp * np.sin(Theta) * np.sin(Phi)
z = Y_amp * np.cos(Theta)

# -------------------------------
# Color map
# -------------------------------
cmap = cm.plasma
norm = colors.Normalize(vmin=0.0, vmax=float(Y_prob.max()))
sm = cm.ScalarMappable(norm=norm, cmap=cmap)
facecolors = cmap(norm(Y_prob))

# -------------------------------
# FIGURE
# -------------------------------
fig = plt.figure(figsize=(18, 5))

# -------------------------------------
# (1) 3D Surface plot
# -------------------------------------
ax = fig.add_subplot(1, 3, 1, projection='3d')
ax.plot_surface(x, y, z, facecolors=facecolors, linewidth=0)
fig.colorbar(sm, ax=ax, label="Probability density")
ax.set_title(f"3D Real Spherical Harmonic (l={l}, m={m_in})")
ax.set_xlabel("x"); ax.set_ylabel("y"); ax.set_zlabel("z")

# -------------------------------------
# (2) 2D θ–φ probability map
# -------------------------------------
ax2 = fig.add_subplot(1, 3, 2)
ax2.pcolormesh(phi_1d, theta_1d, Y_prob, cmap=cmap, norm=norm, shading='auto')
fig.colorbar(sm, ax=ax2, label="Probability density")
ax2.set_title("Probability Map (θ vs φ)")
ax2.set_xlabel("phi"); ax2.set_ylabel("theta")

# -------------------------------------
# (3) Polar plot — fixed version
# -------------------------------------
ax3 = fig.add_subplot(1, 3, 3, projection='polar')

# radius = normalized θ
ax3.pcolormesh(Phi, Theta / np.pi, Y_prob, cmap=cmap, norm=norm, shading='auto')

fig.colorbar(sm, ax=ax3, label="Probability density")
ax3.set_title("Polar Probability Plot")

plt.tight_layout()
plt.show()

