import numpy as np
import matplotlib.pyplot as plt
#
#   plot RMS value of a sinusoid
#
F = 60
w = 2*np.pi*F  # 60Hz
P = 1/F
Tmax = 3*P

T = np.linspace(0,Tmax, 250)
it = []
vt = []
pi = []
Im = 170
for t in T:
    i =  Im*np.cos(w*t)
    it.append( i )
fig = plt.figure(figsize=(10,7.5))
ax = plt.gca()
plt.plot(T,it)
irms = 0.707 * Im
plt.plot([0.0, Tmax],[irms, irms])

pi = np.pi
# tickpts = np.array(range(12))
# tickvals = pi/4 * tickpts
# ax.set_xticks(tickvals)
ax.set_xlabel('time (s)')
ax.set_ylabel('Amplitude')
ax.legend(['Wall outlet Voltage', 'RMS Value'])
plt.title('North American Houshold Voltage')
plt.grid()
plt.show()
