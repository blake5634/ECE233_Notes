import numpy as np
import matplotlib.pyplot as plt
w = 1
C = 1
R = 2.0
L = 0.5
j = 0.0+1.0j
Zc = 1/(j*w*C)
# phi = np.angle(Zc)
Zl = j*w*L
phi = np.angle(Zl)

T = np.linspace(0,5*np.pi/2, 200)
it = []
vt = []
pi = []
for t in T:
    i =  1.0*np.cos(w*t)
    v =  0.8*np.cos(w*t+ phi)
    # v =  i*R
    it.append( i  )
    vt.append( v  )
    pi.append( i*v)
fig = plt.figure(figsize=(10,10))
ax = plt.gca()
data = [it,vt,pi]
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
plt.title('Inductor')
plt.grid()
plt.show()
