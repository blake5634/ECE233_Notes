import numpy as np


j = 0.0 + 1.0j

R = 20
w = 377
Vr = 120 # US house current
#
# print('C', 1/(7*w))
# print('L', 5/w)
C = 380E-6  # 380 uF
L = 13E-3   #13mH
Zc = 1.0/(j*w*C)
Zl = j*w*L
Zt = R+Zl+Zc

print('Zl', Zl)
print('Zc', Zc)
print('Zt', Zt)

S = np.abs(Vr)**2 / Zt

print('S: ', S)

A = np.abs(S)
print('Apparent Pwr: ', A)

PF = np.cos(np.angle(S))
print ('PF: ', PF)

Ir = Vr/Zt
print('Ir:', Ir)
Sr = Ir*np.conj(Ir)*R
Sl = Ir*np.conj(Ir)*Zl
Sc = Ir*np.conj(Ir)*Zc

print('Sr:', Sr, '  Sl:',Sl, '  Sc:', Sc)
