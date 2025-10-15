import numpy as np
import matplotlib.pyplot as plt
#
#   Visualize sinusoidal voltage and current and power
#     for R, L, C


w = 1
C = 1
R = 2.0
L = 0.5

j = 0.0+1.0j

ZR = R
ZC = 1.0/(j*w*C)
ZL = j*w*L


# choose an element:

Z = ZC
# titlestr = 'Resistor'
titlestr = 'Capacitor'
# titlestr = 'Resistor'

phi = np.angle(Z)

T = np.linspace(0,5*np.pi/2, 50)
V = (1.0 + 0j) * np.e**(j*w*T)  # complex sinusoid voltage

I = V/Z

Vr = np.real(V)
Ir = np.real(I)

P = Vr*Ir

i=0
for t in T:
   print(t, Vr[i], Ir[i], P[i])
fig = plt.figure(figsize=(10,10))
ax = plt.gca()
data = [Ir, Vr, P]
colors=['k','b','r']
for i in range(3):
    plt.plot(T,data[i], color=colors[i])

pi = np.pi
tickpts = np.array(range(12))
tickvals = pi/4 * tickpts
ax.set_xticks(tickvals)
ax.set_xlabel('wt (rad)')
ax.set_ylabel('Amplitude')
ax.legend(['Current', 'Voltage', 'Inst. Pwr.'])
plt.title('Voltage, Current, Power: '+titlestr)
plt.grid()
plt.show()
