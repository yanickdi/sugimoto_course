import matplotlib.pyplot as plt
import numpy as np
import sys

x = np.arange(0 , 1.000, 0.001)
y = np.empty(len(x))
for i, x_val in enumerate(x):
    if 0 < x_val < 1:
        y[i] = (x_val / (1-x_val))**(1/2) 
    if x_val == 0:
        y[i] = 0

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, label='$f^-1(x)$')

#ax.set_aspect('equal')
plt.legend()
plt.ylim(0, 5)
plt.xlim(-0.5, 2)
plt.grid()
plt.show()