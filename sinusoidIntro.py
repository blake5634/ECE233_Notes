import numpy as np
import matplotlib.pyplot as plt

#
#  Play with one or more sinusoids
#
ncyc = 3  # how many cycles to plot

w = 60*2*np.pi   # North American power Standard

Tmax = ncyc*2*np.pi / w
t = np.linspace(0,Tmax, 250)

A1 = 170
w1 = w
ph1 = 0
#
# A2 =  160
# w2 = 2
# ph2 = np.pi/4

y1 = A1*np.sin(w1*t+ ph1)
# y2 = A2*np.sin(w2*t + ph2)

fig,ax = plt.subplots(1, figsize=(10,10))
plt.plot(t,y1)# ,t,y2)

# show the level of "RMS" value
rms = A1/np.sqrt(2)
plt.plot([t[0],t[-1]], [rms, rms])

ax.set_xlim(0,Tmax)
ax.set_ylim(-200,200)
ax.set_xlabel('Time (sec)')
ax.set_ylabel('Amplitude')
ax.grid()
plt.show()
