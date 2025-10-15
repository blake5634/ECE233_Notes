import numpy as np
import matplotlib.pyplot as plt

ncyc = 2
w = 157
Tmax = ncyc*2*np.pi / w
t = np.linspace(0,Tmax, 250)

# draw a rotating vector for
#     V(t) = 16 sin(wt+phi)
#     where w = 157, wt = 3pi/4 and phi = -pi/4
#

A1 = 16.0
w1 = 157
ph1 = 3*np.pi/4


y1 = A1*np.sin(w1*t+ ph1)

# plt.subplots(1, 2, figsize=figsize, gridspec_kw={'width_ratios': [1, 3]})

# sinusoid plot
fig, (axRot, axSin) = plt.subplots(1, 2, figsize=(10,7))
axSin.plot(t,y1)
axSin.set_xlim(0,Tmax)
axSin.set_ylim(-20,20)
axSin.set_xlabel('Time (sec)')
axSin.set_ylabel('Amplitude')
axSin.grid()


# rotating vector plot
wr = ph1
x = A1*np.cos(wr)
y = A1*np.sin(wr)
# axRot.plot([0, x], [0, y])

# Draw arrow from (0,0) to (x,y)
axRot.annotate('', xy=(x,y), xytext=(0,0),
            arrowprops=dict(arrowstyle='->', lw=2, color='blue'))

# # You can customize the arrow style
ra = 0.35
axRot.annotate('', xy=(-ra*A1, 0), xytext=(ra*x, ra*y),
               arrowprops=dict(arrowstyle='->',
                             connectionstyle=f'arc3,rad={ra}',
                             color='blue', lw=2))

# axRot.arrow(0,0,x,y,width=0.5)
axRot.plot([x, 20], [y,y], linestyle='dashed')
# plot circle
circ = plt.Circle((0, 0), A1, fill=False, color='blue', linewidth=2, alpha=0.5)
axRot.add_artist(circ)
axRot.set_xlim(-20,20)
axRot.set_ylim(-20,20)
axRot.set_xlabel('X')
axRot.set_ylabel('Y')
axRot.grid()
# Remove space between subplots
plt.subplots_adjust(wspace=0.0)
plt.show()
