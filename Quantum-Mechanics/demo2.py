import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm, colors
from scipy.special import lpmv
import math

# Inputs
l = int(input("Enter l: "))
m_in = int(input("Enter m: "))

# Basic validation
if l < 0 or abs(m_in) > l:
    raise ValueError("Require l >= 0 and |m| <= l.")

# Angular grids
theta_1d = np.linspace(0, np.pi, 200)      # polar angle θ in [0, π]
phi_1d   = np.linspace(0, 2*np.pi, 200)    # azimuth φ in [0, 2π]
# Mesh with phi as "x" and theta as "y" so shapes are (len(theta), len(phi))
Phi, Theta = np.meshgrid(phi_1d, theta_1d, indexing='xy')

def norm_const(l, m_abs):
    # Normalization without an extra (-1)^m; lpmv includes Condon–Shortley in P_l^m.
    return math.sqrt(((2*l + 1) / (4*math.pi)) * (math.factorial(l - m_abs) / math.factorial(l + m_abs)))

def real_tesseral_harmonic(l, m, theta, phi):
    """
    Real spherical harmonics (tesseral) built from lpmv.
    - m == 0: Y = N P_l^0(cosθ)           (real)
    - m  > 0: Y = √2 N P_l^m(cosθ) cos(mφ)  (cos-branch; e.g., p_x for l=1,m=1)
    - m  < 0: Y = √2 N P_l^{|m|}(cosθ) sin(|m|φ) (sin-branch; e.g., p_y for l=1,m=-1)
    These are orthonormal on the sphere with the same normalization as complex Y_l^m.
    """
    m_abs = abs(m)
    N = norm_const(l, m_abs)
    P = lpmv(m_abs, l, np.cos(theta))  # includes Condon–Shortley (-1)^m internally for m_abs>0
    if m == 0:
        return N * P
    elif m > 0:
        return math.sqrt(2.0) * N * P * np.cos(m * phi)
    else:  # m < 0
        return math.sqrt(2.0) * N * P * np.sin(m_abs * phi)

# Build the real tesseral field
Y_real = real_tesseral_harmonic(l, m_in, Theta, Phi)

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