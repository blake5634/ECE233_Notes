import numpy as np
L = 0.001
C = 1.0E-3
R = 10
j = 0.0+1.0j
ww = [ 10, 100, 5E2, 1000, 5e3, 1.0e4, 1.0e5]
print(' w             X      |Z|        /_Z (deg)       Z')
for w in ww:
   X = j*w*L + 1.0/(j*w*C)
   Z =  R + j*w*L + 1.0/(j*w*C)
   ang = 360 * np.angle(Z)/(2*np.pi)
   print(f'{w:.2e} {np.imag(X):>8.2f}  {np.abs(Z):>8.2f}  {ang:>8.2f}   {np.real(Z):8.2f} + {np.imag(Z):8.2f}j' )

