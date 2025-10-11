import numpy as np
from scipy import stats

# Example measured arrays (replace with your data)
r = np.array([0.05,0.1,0.15,0.2,0.25])    # distances (m)
P = np.array([0.8,0.4,0.26,0.18,0.12])   # measured RMS pressures (Pa) at a given f

# Choose geometric spreading exponent n (1 for spherical, 0.5 for cylindrical)
n = 1.0

# Geometrically correct the amplitude
P_corr = P * (r**n)

# Remove any zeros and take log
mask = P_corr>0
x = r[mask]
y = np.log(P_corr[mask])

# Linear fit: y = a + b*x  -> slope b = -alpha
slope, intercept, r_val, p_val, std_err = stats.linregress(x, y)
alpha = -slope       # in Np/m
alpha_db_per_m = alpha * 8.686  # convert to dB/m

print(f"Fitted alpha = {alpha:.6f} Np/m  = {alpha_db_per_m:.4f} dB/m")
print(f"Intercept ln(P0_corr) = {intercept:.3f}")

# Optional: compute fitted curve
r_fit = np.linspace(min(r), max(r), 100)
P_fit = np.exp(intercept) * np.exp(-alpha * r_fit) / (r_fit**n)  # /r^n to compare with raw P
