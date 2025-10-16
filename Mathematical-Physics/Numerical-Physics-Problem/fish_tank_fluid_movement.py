import numpy as np
import matplotlib.pyplot as plt

# Tank parameters
Lx, Ly = 0.6, 0.4   # tank size in meters
nx, ny = 400, 300    # grid resolution
dx, dy = Lx/nx, Ly/ny

# Acoustic properties
c = 1480              # m/s, speed of sound in water
f = 1000              # frequency in Hz
omega = 2 * np.pi * f
k = omega / c         # wavenumber
alpha = 0.8           # damping coefficient (Np/m)

# Grid
x = np.linspace(0, Lx, nx)
y = np.linspace(0, Ly, ny)
X, Y = np.meshgrid(x, y)

# Source: centered or near wall
x0, y0 = Lx/2, Ly/2  # try (Lx*0.1, Ly/2) for side placement

# Distance from source
r = np.sqrt((X - x0)**2 + (Y - y0)**2) + 1e-6

# Pressure amplitude model: A(r) = (1/r)*exp(-alpha*r)*sin(kr)
A = (1/r) * np.exp(-alpha * r) * np.sin(k * r)

# Normalize and convert to dB
A_dB = 20 * np.log10(np.abs(A) / np.max(np.abs(A)))

# Visualization
plt.figure(figsize=(8, 5))
plt.imshow(A_dB, extent=[0, Lx, 0, Ly], origin='lower', cmap='plasma')
plt.colorbar(label='Relative Amplitude (dB)')
plt.title(f'Vibration Amplitude Map in Water (f={f} Hz)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()
