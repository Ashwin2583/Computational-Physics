import numpy as np

h_c = 1973
m = 0.511e6
e = 3.795
N = 1000
c = 3e8

r = np.linspace(2e-2,20,N)
dr = r[1] - r[0]
H = np.zeros((N,N))
V = -(e**2)/r
alpha = (h_c**2)/(2*m*(dr**2))

for i in range(N):
    H[i,i] = (2*alpha + V[i])
    if i>0:
        H[i,i-1] = -alpha
    if i<N-1:
        H[i,i+1] = -alpha

eigen_val, eigen_vector = np.linalg.eigh(H)
E_0 = eigen_val[0]
E_100 = eigen_val[100]

wave = (0 - E_0)/(h_c*(2*np.pi))
print("Ground state energy: ",E_0, "eV")
print("101th state energy: ",E_100, "ev")
print("Wavenumber: ",wave, "A")
print("The wavelength: ", (1/wave), "A")