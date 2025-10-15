import numpy as np
import matplotlib.pyplot as plt

ncyc = 2
w = 100*2*np.pi
Tmax = ncyc*2*np.pi / w
t = np.linspace(0,Tmax, 250)

A1 = 1.0
w1 = w
ph1 = 0

A2 = 0.75
w2 = 1.5*w
ph2 = np.pi/4

y1 = A1*np.sin(w1*t+ ph1)
y2 = A2*np.sin(w2*t + ph2)

fig,ax = plt.subplots(1, figsize=(10,10))
plt.plot(t,y1,t,y2)
ax.set_xlim(0,Tmax)
ax.set_ylim(-1.5,1.5)
ax.set_xlabel('Time (sec)')
ax.set_ylabel('Amplitude')
ax.grid()
plt.show()
