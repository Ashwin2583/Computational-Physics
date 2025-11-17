import numpy as np

h_cut = 1973
m = 0.511e6
e = 3.795
N = 1000
c = 3e8

r = np.linspace(2e-2,20,N)
dr = r[1] - r[0]
H = np.zeros((N,N))
V = -(e**2)/r
alpha = (h_cut**2)/(2*m*(dr**2))

for i in range(N):
    H[i,i] = (2*alpha + V[i])
    if i>0:
        H[i,i-1] = -alpha
    if i<N-1:
        H[i,i+1] = -alpha

eigen_val, eigen_vector = np.linalg.eigh(H)
E_0 = eigen_val[0]
E_100 = eigen_val[100]

wave = (E_100 - E_0)/(h_cut*(2*np.pi)*c)
print(E_0)
print(wave)